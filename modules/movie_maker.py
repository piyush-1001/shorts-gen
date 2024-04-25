from moviepy.editor import TextClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip, ImageClip
from PIL import Image
import numpy as np
from mutagen.mp3 import MP3
import os

def get_audio_files(directory):
    """
    Get a list of .mp3 files in the directory that start with 'output'.
    
    Args:
    - directory (str): Directory path
    
    Returns:
    - List of .mp3 file paths
    """
    audio_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.startswith('output') and file.endswith('.mp3')]
    return audio_files

def get_mp3_duration(file_path):
    try:
        audio = MP3(file_path)
        duration_seconds = audio.info.length
        return duration_seconds
    except Exception as e:
        print(f"Error reading MP3 file: {e}")
        return None

def create_video(list_of_subtitles):
    # List of strings
    texts = list_of_subtitles 

    # List of audio file paths
    audio_files = get_audio_files("audio-clips")  

    # Path to background image
    background_image_path = 'backgrounds/background.jpg'

    # Open the image with Pillow and resize with LANCZOS filtering
    background_image = Image.open(background_image_path)
    background_image = background_image.resize((720, 1280), Image.LANCZOS)

    # Convert Pillow Image to NumPy array
    background_array = np.array(background_image)

    # Create an ImageClip from the NumPy array
    background_clip = ImageClip(background_array, ismask=False)
    #background_clip = background_clip.set_duration(10)

    # Initialize variables
    clips = []

    # Create video clips with subtitles
    for i, text in enumerate(texts):
        # Create a text clip with the subtitle
        # Create an audio clip


        txt_clip = TextClip(text, font='Constantia', bg_color='transparent', fontsize=65, method='caption', color='white', size=(720, 1280))
        length = get_mp3_duration(audio_files[i])
        background_clip = background_clip.set_duration(length)
        txt_clip = txt_clip.set_pos(('center', 'center')).set_duration(length)  # Set duration to 5 seconds
        
        # Create an audio clip
        audio_clip = AudioFileClip(audio_files[i])

        # Combine text and audio clips
        video_clip = txt_clip.set_audio(audio_clip)
        
        # Combine text and audio clips with background
        video_with_bg = CompositeVideoClip([background_clip, video_clip.set_pos(('center', 'center'))])
        
        # Append to the list of clips
        clips.append(video_with_bg)

    # Concatenate video clips
    final_clip = concatenate_videoclips(clips, method="compose")

    # Write the output video
    final_clip.write_videofile('output-videos/output_video.mp4', codec="h264_nvenc", fps=24) # codec libx264 for cpu, h264_nvenc for nvidia gpus
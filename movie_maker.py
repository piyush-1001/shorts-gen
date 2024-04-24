from moviepy.editor import TextClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip, ImageClip
from PIL import Image
import numpy as np
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

def create_video(list_of_subtitles):
    # List of strings
    texts = list_of_subtitles 

    # List of audio file paths
    audio_files = get_audio_files()  

    # Path to background image
    background_image_path = 'background.jpg'

    # Open the image with Pillow and resize with LANCZOS filtering
    background_image = Image.open(background_image_path)
    background_image = background_image.resize((1080, 1920), Image.LANCZOS)

    # Convert Pillow Image to NumPy array
    background_array = np.array(background_image)

    # Create an ImageClip from the NumPy array
    background_clip = ImageClip(background_array, ismask=False)
    background_clip = background_clip.set_duration(5)

    # Initialize variables
    clips = []

    # Create video clips with subtitles
    for i, text in enumerate(texts):
        # Create a text clip with the subtitle
        txt_clip = TextClip(text, font='Constantia', bg_color='transparent', fontsize=100, method='caption', color='white', size=(1080, 1920))
        txt_clip = txt_clip.set_pos(('center', 'center')).set_duration(5)  # Set duration to 5 seconds
        
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
    final_clip.write_videofile('output_video.mp4', codec='libx264', fps=24)

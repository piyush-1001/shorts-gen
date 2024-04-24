import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("API KEY")
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def text_to_speech_files(texts: list) -> list:
    saved_file_paths = []
    counter = 0

    for text in texts:
        # Calling the text_to_speech conversion API with detailed parameters
        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        # Set the output file name
        save_file_name = f"output_{counter}.mp3"
        save_file_path = os.path.join(os.getcwd(), save_file_name)

        # Writing the audio to a file
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

        saved_file_paths.append(save_file_path)
        print(f"{save_file_path}: A new audio file was saved successfully!")

        counter += 1

    # Return the list of saved audio file paths
    return saved_file_paths

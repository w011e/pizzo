import os

AUDIO_FILES_DIR = "/home/pizzo/pizzo/audio"

def play_audio(filename):
    file_path = os.path.join(AUDIO_FILES_DIR, filename)
    os.system(f"mpg123 {file_path}")

if __name__ == "__main__":
    play_audio("alarm1.mp3")

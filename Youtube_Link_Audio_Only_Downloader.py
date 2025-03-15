from pytube import YouTube
import os

def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def download_audio_from_link(video_url, download_path):
    """Download audio from a YouTube link in the best quality available."""
    try:
        youtube = YouTube(video_url)
        audio = youtube.streams.filter(only_audio=True).first()
        
        if audio:
            # Download the audio file
            audio_path = audio.download(download_path)
            # Optionally, rename the file to have a .mp3 extension
            base, ext = os.path.splitext(audio_path)
            new_file = base + '.mp3'
            os.rename(audio_path, new_file)
            print(f"Downloaded audio '{youtube.title}' to '{new_file}'")
        else:
            print(f"No suitable audio stream found for '{youtube.title}'.")
    except Exception as e:
        print(f"Failed to download audio from '{video_url}': {e}")

def main():
    video_url = 'https://www.youtube.com/watch?v=jh-z5CWMFnM&t=2929s'  # Replace 'YourVideoID' with the actual video ID
    download_path = 'downloaded_audios'
    create_directory(download_path)
    download_audio_from_link(video_url, download_path)

if __name__ == "__main__":
    main()

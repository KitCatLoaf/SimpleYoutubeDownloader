#!/usr/bin/env python3

from pytubefix import YouTube, Playlist
import os

def Download(link, file_extension, output_path):
    try:
        if "playlist" in link:
            print("Downloading playlist...")
            playlist = Playlist(link)
            for video_url in playlist.video_urls:
                youtubeObject = YouTube(video_url)
                if file_extension == "4":
                    print(f"Downloading {youtubeObject.title} in MP4 format...")
                    youtubeObject.streams.get_highest_resolution().download(output_path=output_path)
                    print(f"Successfully downloaded {youtubeObject.title} in MP4 format.")
                elif file_extension == "3":
                    print(f"Downloading {youtubeObject.title} in MP3 format...")
                    audio_stream = youtubeObject.streams.filter(only_audio=True).first()
                    audio_stream.download(filename=f"{youtubeObject.title}.mp3", output_path=output_path)
                    print(f"Successfully downloaded {youtubeObject.title} in MP3 format.")
                elif file_extension == "0":
                    print(f"Downloading {youtubeObject.title} in both MP4 and MP3 formats...")
                    print(f"Downloading {youtubeObject.title} in MP3 format...")
                    audio_stream = youtubeObject.streams.filter(only_audio=True).first()
                    audio_stream.download(filename=f"{youtubeObject.title}.mp3", output_path=output_path)
                    print(f"Downloading {youtubeObject.title} in MP4 format...")
                    video_stream = youtubeObject.streams.get_highest_resolution()
                    video_stream.download(output_path=output_path)
                    print(f"Successfully downloaded {youtubeObject.title} in both MP4 and MP3 formats.")
                else:
                    print("Invalid input, skipping video.")
        else:
            print("Downloading single video...")
            youtubeObject = YouTube(link)
            if file_extension == "4":
                print(f"Downloading {youtubeObject.title} in MP4 format...")
                youtubeObject.streams.get_highest_resolution().download(output_path=output_path)
                print("Download success in MP4 format.")
            elif file_extension == "3":
                print(f"Downloading {youtubeObject.title} in MP3 format...")
                audio_stream = youtubeObject.streams.filter(only_audio=True).first()
                audio_stream.download(filename=f"{youtubeObject.title}.mp3", output_path=output_path)
                print(f"Successfully downloaded {youtubeObject.title} in MP3 format.")
            elif file_extension == "0":
                print(f"Downloading in both MP4 and MP3 formats...")
                print(f"Downloading {youtubeObject.title} in MP3 format...")
                audio_stream = youtubeObject.streams.filter(only_audio=True).first()
                audio_stream.download(filename=f"{youtubeObject.title}.mp3", output_path=output_path)
                print(f"Downloading {youtubeObject.title} in MP4 format...")
                video_stream = youtubeObject.streams.get_highest_resolution()
                video_stream.download(output_path=output_path)
                print(f"Successfully downloaded {youtubeObject.title} in MP4 and MP3 formats.")
            else:
                print("Invalid input, exiting.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(script_dir, "Downloaded_Files")
    os.makedirs(download_path, exist_ok=True)

    link = input("Input YouTube Link: ")
    file_extension = input("Pick Format: (3 = MP3, 4 = MP4, 0 = Both) ")

    Download(link, file_extension, download_path)
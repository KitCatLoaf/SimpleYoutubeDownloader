from tkinter import *
from pytubefix import YouTube, Playlist
import os

window = Tk()
window.geometry("800x500")
window.title("Youtube Downloader")

window.config(background="gray")

def getValues():
    if mp3Clicked.get() == 1 and mp4Clicked.get() == 0:
        return(3)
    if mp4Clicked.get() == 1 and mp3Clicked.get() == 0:
        return(4)
    else:
        return(0)

def downloadVideo(link, file_extension, output_path):
    try:
        if "playlist" in link:
            status.config(text="Downloading playlist...")
            print("Downloading playlist...")
            playlist = Playlist(link)
            for video_url in playlist.video_urls:
                youtubeObject = YouTube(video_url)
                if file_extension == "4":
                    status.config(text=f"Downloading {youtubeObject.title} in MP4 format...")
                    print(f"Downloading {youtubeObject.title} in MP4 format...")
                    youtubeObject.streams.get_highest_resolution().download(output_path=output_path)
                    status.config(text=f"Successfully downloaded {youtubeObject.title} in MP4 format.")
                    print(f"Successfully downloaded {youtubeObject.title} in MP4 format.")
                elif file_extension == "3":
                    status.config(text=f"Downloading {youtubeObject.title} in MP3 format...")
                    print(f"Downloading {youtubeObject.title} in MP3 format...")
                    audio_stream = youtubeObject.streams.filter(only_audio=True).first()
                    audio_stream.download(filename=f"{youtubeObject.title}.mp3", output_path=output_path)
                    status.config(text=f"Successfully downloaded {youtubeObject.title} in MP3 format.")
                    print(f"Successfully downloaded {youtubeObject.title} in MP3 format.")
                elif file_extension == "0":
                    status.config(text=f"Downloading {youtubeObject.title} in both MP4 and MP3 formats...")
                    print(f"Downloading {youtubeObject.title} in both MP4 and MP3 formats...")
                    status.config(text=f"Downloading {youtubeObject.title} in MP3 format...")
                    print("Downloading {youtubeObject.title} in MP3 format...")
                    audio_stream = youtubeObject.streams.filter(only_audio=True).first()
                    audio_stream.download(filename=f"{youtubeObject.title}.mp3", output_path=output_path)
                    status.config(text=f"Downloading {youtubeObject.title} in MP4 format...")
                    print(f"Downloading {youtubeObject.title} in MP4 format...")
                    video_stream = youtubeObject.streams.get_highest_resolution()
                    video_stream.download(output_path=output_path)
                    status.config(text=f"Successfully downloaded {youtubeObject.title} in both MP4 and MP3 formats.")
                    print(f"Successfully downloaded {youtubeObject.title} in both MP4 and MP3 formats.")
                else:
                    status.config(text="Invalid input, skipping video.")
                    print("Invalid input, skipping video.")
        else:
            status.config(text="Downloading single video...")
            print("Downloading single video...")
            youtubeObject = YouTube(link)
            if file_extension == "4":
                status.config(text="Downloading {youtubeObject.title} in MP4 format...")
                print("Downloading {youtubeObject.title} in MP4 format...")
                youtubeObject.streams.get_highest_resolution().download(output_path=output_path)
                status.config(text="Download success in MP4 format.")
                print("Download success in MP4 format.")
            elif file_extension == "3":
                status.config(text=f"Downloading {youtubeObject.title} in MP3 format...")
                print(f"Downloading {youtubeObject.title} in MP3 format...")
                audio_stream = youtubeObject.streams.filter(only_audio=True).first()
                audio_stream.download(filename=f"{youtubeObject.title}.mp3", output_path=output_path)
                status.config(f"Successfully downloaded {youtubeObject.title} in MP3 format.")
                print(f"Successfully downloaded {youtubeObject.title} in MP3 format.")
            elif file_extension == "0":
                status.config(text=f"Downloading in both MP4 and MP3 formats...")
                print(f"Downloading in both MP4 and MP3 formats...")
                status.config(text=f"Downloading {youtubeObject.title} in MP3 format...")
                audio_stream = youtubeObject.streams.filter(only_audio=True).first()
                audio_stream.download(filename=f"{youtubeObject.title}.mp3", output_path=output_path)
                status.config(text=f"Downloading {youtubeObject.title} in MP4 format...")
                print(f"Downloading {youtubeObject.title} in MP4 format...")
                video_stream = youtubeObject.streams.get_highest_resolution()
                video_stream.download(output_path=output_path)
                status.config(text=f"Successfully downloaded {youtubeObject.title} in MP4 and MP3 formats.")
                print(f"Successfully downloaded {youtubeObject.title} in MP4 and MP3 formats.")
            else:
                status.config(text="Invalid input, exiting.")
                print("Invalid input, exiting.")
    except Exception as e:
        status.config(text=f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
        
def download():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(script_dir, "Downloaded_Files")
    os.makedirs(download_path, exist_ok=True)

    ytLink = link.get()
    fileExtension = getValues()

    downloadVideo(ytLink, str(fileExtension), download_path)

mp3Clicked = IntVar()
mp4Clicked = IntVar()
buttonMp4 = Checkbutton(window, text="Save as .mp4", variable=mp4Clicked, command=getValues)
buttonMp4.pack()

buttonMp3 = Checkbutton(window, text="Save as .mp3", variable=mp3Clicked, command=getValues)
buttonMp3.pack()

link = Entry(window)
link.pack()

submit = Button(window, text="Download", command=download)
submit.pack()

status = Label(window, text="Waiting for status...")
status.pack()

if __name__ == "__main__":
    print("Downloader Additional Output: \n")

    window.mainloop()

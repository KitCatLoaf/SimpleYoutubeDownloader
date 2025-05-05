from pytubefix import YouTube;
import os;




def Download(link):
  script_dir = os.path.dirname(os.path.abspath(__file__))
  download_path = os.path.join(script_dir, "Downloaded_Files")
  os.makedirs(download_path, exist_ok=True)
  youtubeObject = YouTube(link)
  
  try:
      if fileExtension == "4":
          print("Using MP4 format.")
          youtubeObject.download(output_path=download_path)
          print("Download success in MP4 format.")
      elif fileExtension == "3":
          print("Using MP3 format.")
          youtubeObject = link.streams.filter(only_audio=True).first()
          youtubeObject.download(filename=f"{youtubeObject.title}.mp3", outputpath=download_path)
          print("Successfully downloaded in MP3 format.")
      elif fileExtension == "0":
          print("Installing in both MP4 and MP3.")
          print("Installing MP3...")
          audio_stream = youtubeObject.streams.filter(only_audio=True).first()
          audio_stream.download(filename=f"{youtubeObject.title}.mp3", output_path=download_path)
          print("Installing MP4...")
          video_stream = youtubeObject.streams.get_highest_resolution()
          video_stream.download(output_path=download_path)
          print("Successfully downloaded MP4 and MP3.")
      else:
          print("Invalid input, exiting.")



  except:
      print("Unexpected error, exiting.")




link = input("Input YouTube Link: ")
fileExtension = input("Pick Format: (3 = MP3, 4 = MP4, 0 = Both) ")




Download(link)




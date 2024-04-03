from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, file_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_resolution_vid = streams.get_highest_resolution()
        highest_resolution_vid.download(output_path=file_path)
        
    
    except Exception as ex:
        print(ex)
        
def start_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder is: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    video_url = input("Please enter a youtube url: ")
    save_directory = start_file_dialog()
    
    if not save_directory:
        print("Started downloading!")
    else:
        print("Please provide a valid saving location.")
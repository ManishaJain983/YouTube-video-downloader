from pytubefix import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

video_url = input("Enter YouTube video URL: ")
download_video(video_url)

import tkinter as tk
from pytubefix import YouTube  # Use pytubefix to avoid known errors

# Function to download video
def download_video():
    url = link.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        status_label.config(text=f"Downloading: {yt.title}")
        stream.download()
        status_label.config(text="Download completed!")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

# Create GUI window
window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry("500x200")
window.config(bg="#f0f0f0")
window.resizable(False, False)

# Input field
link = tk.StringVar()
tk.Label(window, text="Paste YouTube URL:", font="Arial 12", bg="#f0f0f0").pack(pady=10)
tk.Entry(window, textvariable=link, width=50, font="Arial 12").pack()

# Download button
tk.Button(window, text="Download Video", command=download_video, font="Arial 12", bg="#4CAF50", fg="white").pack(pady=10)

# Status label
status_label = tk.Label(window, text="", font="Arial 10", bg="#f0f0f0", fg="blue")
status_label.pack()

# Run the GUI loop
window.mainloop()

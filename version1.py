from pytube import YouTube

# Prompt the user for the YouTube video URL
video_url = str(input("Enter the YouTube video URL: "))

# Create a YouTube object
yt = YouTube(video_url)

# Print video details
print("Video Title:", yt.title)
print("Video Length:", yt.length, "seconds")
print("Video Rating:", yt.rating)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
print("Downloading video...")
stream.download()
print("Download completed!")

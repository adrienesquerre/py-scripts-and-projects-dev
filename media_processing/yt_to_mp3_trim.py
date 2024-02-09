import subprocess
import sys

def convert_time_to_seconds(human_readable_time):
    """
    Converts a human-readable time (MM:SS) to seconds.
    """
    parts = human_readable_time.split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + int(seconds)
    else:
        return int(parts[0])

def generate_output_template(start_time):
    """
    Generates an output template for the file name, including a formatted start time.
    """
    # Format the start time for file naming (replace colons with dashes)
    start_time_formatted = start_time.replace(":", "-")
    return f"trimmed_start_{start_time_formatted}_%(title)s.%(ext)s"

def download_and_trim_youtube_audio(video_url, start_time, end_time):
    """
    Downloads and trims a portion of a YouTube video's audio, saving it as an MP3 file.
    """
    start_seconds = convert_time_to_seconds(start_time)
    end_seconds = convert_time_to_seconds(end_time)
    duration_seconds = end_seconds - start_seconds

    output_template = generate_output_template(start_time)

    # Construct the yt-dlp command
    command = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "--postprocessor-args", f"ffmpeg:-ss {start_seconds} -t {duration_seconds}",
        video_url,
        "-o", output_template
    ]

    # Execute the command
    subprocess.run(command)

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py <video_url> <start_time MM:SS> <end_time MM:SS>")
        sys.exit(1)
    
    video_url = sys.argv[1]
    start_time = sys.argv[2]
    end_time = sys.argv[3]

    download_and_trim_youtube_audio(video_url, start_time, end_time)

# Command to run the script:
# C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe c:/Users/user/Desktop/scripts/yt_to_mp3_trim.py "https://www.youtube.com/watch?videoID" "47:53" "56:07"
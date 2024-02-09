
# Yt to mp3 + Trim

This tool allows you to download specific segments of YouTube videos as MP3 files, using `yt-dlp` and `ffmpeg` for processing. It's perfect for extracting audio clips from longer videos.

## Prerequisites

Before you start using this script, you need to have `Python`, `yt-dlp`, and `ffmpeg` installed on your system.

### Installing Python

Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installing yt-dlp

`yt-dlp` is a command-line program to download videos from YouTube and other video platforms. It can be installed via pip. Open your terminal and run:

```bash
pip install yt-dlp
```

### Installing ffmpeg

`ffmpeg` is required for processing video and audio files. Installation instructions vary based on your operating system.

#### On Windows

Download `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/download.html), extract the archive, and add the `bin` folder to your system's PATH.

#### On macOS

Use Homebrew to install `ffmpeg`:

```bash
brew install ffmpeg
```

#### On Linux

Use your distribution's package manager to install `ffmpeg`. For example, on Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

## Usage

1. Clone this repository or download the script `download_trim.py` to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command format:

```bash
python download_trim.py "https://www.youtube.com/watch?v=videoID" "start_time MM:SS" "end_time MM:SS"
```

Replace `"https://www.youtube.com/watch?v=videoID"` with the URL of the YouTube video you want to trim, and replace `"start_time MM:SS"` and `"end_time MM:SS"` with the desired start and end times of the segment you wish to download.

### Example

To download an audio segment from 47:52 to 56:07 of a specific YouTube video, you would run:

```bash
python download_trim.py "https://www.youtube.com/watch?v=videoID" "47:52" "56:07"
```

The script will download the specified audio segment and save it as an MP3 file in the current directory, with the file name including the start time and the title of the video.

## License

This project is open-sourced under the MIT license. Feel free to fork, modify, and use it in your own projects.

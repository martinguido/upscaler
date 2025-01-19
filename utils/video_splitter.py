import os
import subprocess
import re

def split_video_into_frames(video_path, output_dir, fps=60):
    """
    Break a video into frames at a specific frame rate and show progress.

    :param video_path: Path to the video file.
    :param output_dir: Output folder where the frames will be saved.
    :param fps: Desired frames per second (default is 60).
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Get the video duration using FFmpeg
    try:
        result = subprocess.run(
            ["ffmpeg", "-i", video_path],
            stderr=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            text=True
        )
        duration_match = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", result.stderr)
        if not duration_match:
            print("Could not determine video duration.")
            return
        hours, minutes, seconds = map(float, duration_match.groups())
        total_duration = hours * 3600 + minutes * 60 + seconds  # Total duration in seconds
    except FileNotFoundError:
        print("Error: FFmpeg is not installed or not found in your PATH. Please install FFmpeg.")
        return

    # FFmpeg command to extract frames
    command = [
        "ffmpeg",
        "-i", video_path,  # Input video file
        "-vf", f"fps={fps}",  # Filter to set the frame rate
        f"{output_dir}/frame_%04d.png"  # Naming pattern for output frames
    ]

    # Run the FFmpeg command and parse progress
    try:
        process = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL, text=True)
        for line in process.stderr:
            # Look for the "time=" field in the output
            time_match = re.search(r"time=(\d+):(\d+):(\d+\.\d+)", line)
            if time_match:
                hours, minutes, seconds = map(float, time_match.groups())
                current_time = hours * 3600 + minutes * 60 + seconds
                progress = (current_time / total_duration) * 100
                print(f"Progress: {progress:.2f}%", end="\r")  # Overwrite the line
        process.wait()  # Wait for the process to finish
        if process.returncode == 0:
            print(f"\nFrames saved in {output_dir}")
        else:
            print(f"\nError: FFmpeg process failed with return code {process.returncode}")
    except FileNotFoundError:
        print(f"Error: FFmpeg is not installed or not found in your PATH. Please install FFmpeg.")
    except Exception as e:
        print(f"Unexpected error: {e}")

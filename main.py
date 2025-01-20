import os
from utils.frame_interpolation import process_video_frames
from utils.video_splitter import split_video_into_frames


def main():
    # COMMENT FOLLOWING LINE IF YOU HAVE ALREADY RUN THE FIRST TWO STEPS BEFORE
    # os.rmdir("./sample-data/video/frames")

    video_path = "./sample-data/video.mp4"
    output_dir = "./sample-data/video/frames"

    
    # split_video_into_frames(video_path, output_dir)
    # process_video_frames(output_dir)

    return 0


if __name__ == '__main__':
    main()


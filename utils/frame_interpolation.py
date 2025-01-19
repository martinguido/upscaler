import os
import cv2


def generate_intermediate_frame(frame1_path, frame2_path, output_path):
    """
    Generate an intermediate frame between two frames by averaging their pixel values.

    :param frame1_path: Path to the first frame image.
    :param frame2_path: Path to the second frame image.
    :param output_path: Path to save the generated intermediate frame.
    """
    # Load the two frames
    frame1 = cv2.imread(frame1_path)
    frame2 = cv2.imread(frame2_path)

    # Ensure both frames are the same size
    if frame1.shape != frame2.shape:
        print(f"Error: Frames {frame1_path} and {frame2_path} must have the same dimensions.")
        return

    # Generate the intermediate frame by averaging pixel values
    intermediate_frame = cv2.addWeighted(frame1, 0.5, frame2, 0.5, 0)

    # Save the intermediate frame
    cv2.imwrite(output_path, intermediate_frame)
    print(f"Intermediate frame saved at {output_path}")


def process_video_frames(output_dir):
    """
    Process the video, extracting frames and generating intermediate frames between each pair of consecutive frames.

    :param output_dir: Directory where the frames will be saved.
    """

    # Get the list of extracted frames
    frame_files = sorted([f for f in os.listdir(output_dir) if f.endswith('.png')])

    # Total number of frames to process
    total_frames = len(frame_files) - 1

    # Generate intermediate frames between each consecutive frame
    for i in range(total_frames):
        frame1_path = os.path.join(output_dir, frame_files[i])
        frame2_path = os.path.join(output_dir, frame_files[i + 1])
        intermediate_frame_path = os.path.join(output_dir, f"intermediate_{i + 1:04d}.png")

        # Generate the intermediate frame
        generate_intermediate_frame(frame1_path, frame2_path, intermediate_frame_path)

        # Calculate and print the percentage of completion
        progress_percentage = (i + 1) / total_frames * 100
        print(f"Progress: {progress_percentage:.2f}%")

    print("All intermediate frames generated.")


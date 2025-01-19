# 🎬 Frame Splitter & Interpolator 🎥

Welcome to the **Frame Splitter & Interpolator** project! 🌟 This project is all about working with videos, breaking them down into frames, creating smooth transitions between frames, and reassembling them into a fluid video. 🚀

## 🔧 What does this project do?

1. **Split the video into frames** 📸  
   It starts by taking a video and splitting it into individual frames (e.g., 60 frames per second). The higher the FPS, the smoother the video will be. 💨

2. **Interpolate frames** 🔄  
   Next, it takes each pair of consecutive frames and generates an **intermediate frame** by averaging the pixels of the two frames. This helps create a smoother transition between frames and makes the video feel more fluid. 🎞️✨

3. **Rebuild the video** 🎬  
   Finally, all these frames (including the interpolated ones) are stitched together to form a new video at a smooth frame rate, like **60 fps**. The result? A super smooth and fluid video! 🏎️💨

---

## 🛠️ How to use

### 1. **Install dependencies** 📦

Before running the project, make sure you have **FFmpeg** and **OpenCV** installed on your system.

- **FFmpeg**: It's a powerful multimedia framework that will be used to split the video into frames and stitch them back together.
  
  Follow the instructions here to install FFmpeg:
  - [Download FFmpeg](https://ffmpeg.org/download.html)

  Once installed, ensure that FFmpeg is in your system's PATH so that it can be accessed globally from the command line.

- **OpenCV**: This Python library is used to process the images (frames) and generate the interpolated frames.

  Install OpenCV using pip:

  ```bash
  pip install opencv-python

### 2. **Run the script** 💻

Here are the steps to run the project:

- **Step 1**: Generate intermediate frames between each consecutive frame by running the `interpolator.py` script.

  ```bash
  python interpolator.py <output_frames_directory>

  - **Step 2**: Rebuild the video from the frames using the `main.py` script.

---

## 📊 Features

- **Frame splitting** 🖼️
- **Frame interpolation** 🤖
- **Smooth video creation** 🎥
- Works with **any video** format! 🎥🎞️

---

## 📜 Project Structure

- **`splitter.py`**: Splits videos into frames at the desired FPS. 🎥🖼️
- **`interpolator.py`**: Generates intermediate frames between consecutive frames. 🔄
- **`main.py`**: Where all the magic happens—processes the frames and rebuilds the video. 🎬✨

---

## ⚙️ Requirements

- **Python 3.x**: Ensure you are using Python 3 or higher.
- **FFmpeg**: For video frame extraction and video creation. 🎞️
- **OpenCV**: For processing images (frames). 🖼️

---

## ⚠️ Known Limitations

- **FFmpeg path**: Make sure FFmpeg is correctly installed and in your system's path! Otherwise, the process won't work. 💥
- **Performance**: The smoother the video (higher FPS), the more frames you'll need to process, which could take time depending on your machine. ⏳

---

## 🚀 Future Plans

- Support for **more video formats** 🎬
- Add **custom frame interpolation** algorithms 🧠
- More **interactive features** and **optimization** 💨

---

Enjoy creating your **smoothest videos**! 🎉 Let me know if you have any questions or suggestions. 😊

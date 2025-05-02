# 🧠 Text-to-Video Generation using Stable Diffusion 🎥

This project demonstrates how to generate a **video from a textual prompt** using the **Stable Diffusion model**. It leverages Hugging Face’s `diffusers` library for text-to-image generation, and `moviepy` for creating a video from the generated image sequence.

## ✨ Features

* Generate high-quality images from a custom text prompt using Stable Diffusion.
* Automatically saves the images to a local folder.
* Compiles the generated images into a smooth video.
* Utilizes GPU for fast image generation (CUDA support required).

## 🛠️ Dependencies

Install all required packages using:

```bash
pip install transformers diffusers accelerate torch moviepy pillow
```

## 📁 Project Structure

```
.
├── Gen AI.py                  # Main script for text-to-video generation
├── video_frames/              # Folder where image frames are saved
└── prompt_to_video.mp4        # Final generated video
```

## 🚀 How It Works

1. **Text-to-Image Generation**: The script uses a text prompt to generate a series of images using the `StableDiffusionPipeline`.
2. **Save Images**: These images are saved sequentially in a folder.
3. **Image-to-Video Compilation**: The saved images are combined into a video using `moviepy`.

## 🧪 Example Prompt

```python
text_prompt = "A futuristic cityscape with flying cars and neon lights."
```

## 🎞️ Output

Generates `prompt_to_video.mp4` — a video based on your input text prompt.

## 🖥️ Run the Script

Simply run:

```bash
python "Gen AI.py"
```

Make sure your system has CUDA-enabled GPU for optimal performance.

## 📌 Notes

* The default model used is: `runwayml/stable-diffusion-v1-5`
* You can change the number of frames, text prompt, and video output path in the `__main__` section of the script.

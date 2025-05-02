#install - pip install transformers diffusers accelerate torch moviepy pillow       
from diffusers import StableDiffusionPipeline
import torch
import moviepy.editor as mpy
import os

# Step 1: Define a function to generate images from text using Stable Diffusion
def generate_images_from_text(prompt, num_images=5, model_id="runwayml/stable-diffusion-v1-5"):
    """
    Generate a series of images from a text prompt using Stable Diffusion.
    """
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")  # Use GPU for faster inference

    images = []
    for i in range(num_images):
        image = pipe(prompt).images[0]
        images.append(image)
    return images

# Step 2: Save generated images to disk
def save_images(images, output_folder="generated_frames"):
    """
    Save the images to the specified output folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    for idx, img in enumerate(images):
        img_path = os.path.join(output_folder, f"frame_{idx:04d}.png")
        img.save(img_path)
    return output_folder

# Step 3: Create a video from the images
def create_video_from_images(image_folder, output_video_path="output_video.mp4", fps=2):
    """
    Create a video from a series of images in the specified folder.
    """
    # Get list of image paths sorted by name
    image_files = sorted([os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(".png")])

    # Load images
    clips = [mpy.ImageClip(img).set_duration(1/fps) for img in image_files]

    # Concatenate clips to form a video
    video = mpy.concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_video_path, fps=fps)

# Main Execution
if __name__ == "__main__":
    text_prompt = "A futuristic cityscape with flying cars and neon lights."
    num_frames = 10
    frames_folder = "video_frames"
    output_video = "prompt_to_video.mp4"

    # Step 1: Generate images
    images = generate_images_from_text(text_prompt, num_images=num_frames)

    # Step 2: Save images
    frames_path = save_images(images, output_folder=frames_folder)

    # Step 3: Create video
    create_video_from_images(frames_path, output_video_path=output_video, fps=1)
    print(f"Video created: {output_video}")

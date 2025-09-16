import cv2
import numpy as np
import os
from PIL import Image, ImageDraw
import random


def generate_synthetic_seeds(num_images, seeds_per_image, output_dir="seed_dataset"):
    os.makedirs(f"seed_dataset/Seed_Photos/synthetic_images_train", exist_ok=True)
    os.makedirs(f"seed_dataset/Seed_Labels/synthetic_labels_train", exist_ok=True)

    # Load or create a seed template
    seed_template = create_seed_template()

    for img_idx in range(num_images):
        # Create random background
        background = generate_background(960, 960)
        labels = []

        for _ in range(random.randint(seeds_per_image // 2, int(seeds_per_image * 1.5))):
            # Random position
            x = random.randint(50, background.width - 50)
            y = random.randint(50, background.height - 50)

            # Random scale and rotation
            scale = random.uniform(0.8, 1.2)
            angle = random.randint(0, 360)

            # Place seed on background
            seed_img = seed_template.resize(
                (int(seed_template.width * scale),
                 int(seed_template.height * scale))
            ).rotate(angle, expand=True)

            background.paste(seed_img, (x, y), seed_img)

            # Calculate YOLO format bbox (normalized)
            w = seed_img.width / background.width
            h = seed_img.height / background.height
            x_center = (x + seed_img.width / 2) / background.width
            y_center = (y + seed_img.height / 2) / background.height

            labels.append(f"0 {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")

        # Save image and labels
        background.save(f"{output_dir}/Seed_Photos/synthetic_images_train/synthetic_{img_idx}.jpg")
        with open(f"{output_dir}/Seed_Labels/synthetic_labels_train/synthetic_{img_idx}.txt", "w") as f:
            f.write("\n".join(labels))


def create_seed_template():
    """Create a seed-like shape"""
    img = Image.new('RGBA', (40, 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse((0, 0, 20, 10), fill=(120, 80, 40, 255))  # Brown seed
    return img


def generate_background(width, height):
    """Create random background"""
    bg_type = random.choice(['gradient', 'noise', 'color'])
    if bg_type == 'gradient':
        return generate_background(width, height)
    else:
        return Image.new('RGB', (width, height),
                         (random.randint(240, 255),
                          random.randint(240, 255),
                          random.randint(240, 255)))


# Generate 2000 synthetic images with 500-1500 seeds each
generate_synthetic_seeds(num_images=2000, seeds_per_image=500)
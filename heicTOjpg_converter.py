from PIL import Image
import pillow_heif
import os

def convert_heic_to_jpg(heic_file_path, jpg_file_path):
    # Open the HEIC file
    heif_file = pillow_heif.open_heif(heic_file_path)
    # Convert to RGB
    image = Image.frombytes(
        "RGB", heif_file.size, heif_file.data, "raw", heif_file.mode
    )
    # Save as JPG
    image.save(jpg_file_path, "JPEG")

def main():
    input_folder = "C:\\Users\\nithe\\PythonProjects\\SeedCounter_PMLab\\Seed_Photos\\train_heic"
    output_folder = "C:\\Users\\nithe\\PythonProjects\\SeedCounter_PMLab\\Seed_Photos\\train_jpg"

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Convert all HEIC files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(input_folder, filename)
            jpg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")
            convert_heic_to_jpg(heic_path, jpg_path)
            print(f"Converted {filename} to {jpg_path}")


if __name__ == "__main__":
    main()
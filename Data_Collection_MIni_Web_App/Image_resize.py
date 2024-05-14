from PIL import Image
import os


def resize_images_in_folder(folder_path, output_folder, target_size=(28, 28)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".png"):
            image_path = os.path.join(folder_path, file_name)
            output_path = os.path.join(output_folder, file_name)

            with Image.open(image_path) as img:
                resized_img = img.resize(target_size)
                resized_img.save(output_path)

folder_path = "/home/nathan/Documents/EEE4114F/ML_Project/Dataset/circle(un)"
output_folder = "/home/nathan/Documents/EEE4114F/ML_Project/Dataset/circle"
resize_images_in_folder(folder_path, output_folder)

import os

def rename_files(folder_path):
    # Get all files in the folder
    files = os.listdir(folder_path)
    
    # Sort files alphabetically
    files.sort()
    
    # Rename files numerically
    for i, file_name in enumerate(files):
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = f"{i+1:03d}{file_extension}"  # 3 digits, padded with zeros
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

# Replace 'folder_path' with the path to your folder
folder_path = '/home/nathan/Documents/EEE4114F/ML_Project/Dataset/triangle'
rename_files(folder_path)

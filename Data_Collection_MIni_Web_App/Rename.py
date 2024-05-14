import os

def rename_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file
    for file_name in files:
        # Get the full path of the file
        old_path = os.path.join(folder_path, file_name)
        
        # Get the folder name
        folder_name = os.path.basename(folder_path)
        
        # Create the new file name
        new_file_name = f"{folder_name}_{file_name}"
        
        # Get the full path of the new file name
        new_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")

# Replace 'path_to_folder' with the path to your folder
folder_path = '/home/nathan/Documents/EEE4114F/ML_Project/Dataset/triangle'

# Call the function to rename files
rename_files(folder_path)

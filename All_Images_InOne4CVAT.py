import os
import shutil

# Define the paths
source_folder = r'C:\Users\mutem\Downloads\Grapes\Training'  # Your main folder with disease subfolders
destination_folder = r'C:\Users\mutem\Downloads\All_Training_Images'  # The folder where you want to put all images

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through each subfolder in the source folder
for subfolder_name in os.listdir(source_folder):
    subfolder_path = os.path.join(source_folder, subfolder_name)
    
    # Check if the path is a directory (i.e., a folder)
    if os.path.isdir(subfolder_path):
        # Loop through each image file in the subfolder
        for index, filename in enumerate(os.listdir(subfolder_path), start=1):
            file_path = os.path.join(subfolder_path, filename)
            
            # Check if it is an image file
            if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Create a new name with the subfolder name as a prefix
                new_filename = f"{subfolder_name}_{index}{os.path.splitext(filename)[1]}"
                new_file_path = os.path.join(destination_folder, new_filename)
                
                # Copy the file to the destination folder with the new name
                shutil.copy(file_path, new_file_path)
                print(f"Copied and renamed: {file_path} to {new_file_path}")

print("All images have been renamed and moved to the destination folder.")

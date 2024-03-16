#!/usr/bin/env python3
import os
import shutil
import zipfile

def unzip(zip_file_path, extract_to_directory):
    # Check if the ZIP file exists
    if os.path.exists(zip_file_path):
        # Open the zip file in read mode
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Extract all the contents into the directory
            zip_ref.extractall(extract_to_directory)
            print("Extraction complete.")
    else:
        raise FileNotFoundError(f"The file {zip_file_path} does not exist")
        

def copy_wav_files(source_directory, destination_directory):
    # Step 1: Create a new directory named 'source' if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Step 2: Find all folders starting with 'ZOOM'
    for folder_name in os.listdir(source_directory):
        if folder_name.startswith('ZOOM') and os.path.isdir(folder_name):
            # Step 3: Copy all .wav files from these folders to 'source'
            for file_name in os.listdir(folder_name):
                if file_name.endswith('.WAV'):
                    source_file_path = os.path.join(folder_name, file_name)
                    destination_file_path = os.path.join(destination_directory, file_name)

                    # To avoid overwriting, check if file already exists in the destination
                    if not os.path.exists(destination_file_path):
                        shutil.copy2(source_file_path, destination_file_path)
                        print(f"File {file_name} copied to {destination_directory}.")
                    else:
                        print(f"File {file_name} already exists in {destination_directory}, not copying.")

def cleanup_unused_directories(source_directory):
    # Step 1: Find all folders starting with 'ZOOM'
    for folder_name in os.listdir(source_directory):
        if folder_name.startswith('ZOOM') and os.path.isdir(folder_name):
            # Step 2: Delete these folders
            shutil.rmtree(folder_name)
            print(f"Directory {folder_name} deleted.")

if __name__ == "__main__":
    # Specify the path to your zip file
    zip_file_path = 'ZOOM0001.zip'

    # Unzip the file to a directory
    unzip(zip_file_path, '.')

    # Copy .wav files to a new directory
    copy_wav_files('.', '.')
    
    # Clean up the unused directories
    cleanup_unused_directories('.')
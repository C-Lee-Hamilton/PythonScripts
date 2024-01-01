import os

def rename_files(folder_path):
    # Check if the given path is a directory
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid directory.")
        return

    # Get a list of files in the directory
    files = os.listdir(folder_path)

    # Iterate through the files and rename them
    for index, file_name in enumerate(files, start=1):
        # Construct the new file name
        new_name = f"{index}{os.path.splitext(file_name)[1]}"
        
        # Build the full path for the old and new names
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} to {new_name}")

if __name__ == "__main__":
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Combine the script directory with the 'assets' folder
    assets_folder = os.path.join(script_dir, 'assets')

    # Call the function to rename files in the 'assets' folder
    rename_files(assets_folder)

#!/usr/bin/env python3
"""
BMAD MetaPromptAgent Uninstaller Script
This script uninstalls the MetaPromptAgent configuration from a target BMAD system.
"""

import os
import sys
import shutil
import glob

def find_bmad_directory():
    """
    Interactively find the .bmad directory on the target system.
    Returns the absolute path to the directory containing the .bmad directory.
    """
    while True:
        # Ask for the location of the .bmad directory
        location = input("Please provide the location of the \".bmad\" directory: ").strip()
        
        # Check if the provided location exists
        if not os.path.exists(location):
            print(f"Error: The path '{location}' does not exist.")
            continue
        
        # Check if we can see the .bmad directory at the provided location
        bmad_path = os.path.join(location, ".bmad")
        if os.path.exists(bmad_path):
            return os.path.abspath(location)
        
        # If the provided location is within the .bmad directory, go up one level
        if os.path.basename(location) == ".bmad":
            parent_dir = os.path.dirname(location)
            bmad_path = os.path.join(parent_dir, ".bmad")
            if os.path.exists(bmad_path):
                return os.path.abspath(parent_dir)
        
        # If we can't find the .bmad directory, ask to try again or quit
        response = input('I cannot find the ".bmad" directory. Want to try again [Y] or do you want to (Q)uit? ').strip().upper()
        
        # Default is to try again (Y)
        if response == 'Q':
            print("Uninstallation cancelled.")
            sys.exit(0)
        # Any other response (including empty) means try again

def restore_config_file(target_path):
    """
    Restore the original CORE Module Configuration file from backup.
    """
    config_file = os.path.join(target_path, ".bmad", "core", "config.yaml")
    backup_file = config_file + ".bak"
    
    try:
        # Check if backup file exists
        if not os.path.exists(backup_file):
            print(f"Warning: Backup file not found at {backup_file}")
            return False
        
        # Delete the current config file
        if os.path.exists(config_file):
            os.remove(config_file)
            print(f"Deleted current config file: {config_file}")
        
        # Restore from backup
        shutil.copy2(backup_file, config_file)
        print(f"Restored config file from backup: {config_file}")
        return True
    except Exception as e:
        print(f"Error restoring config file: {e}")
        return False

def delete_mpa_files(target_path):
    """
    Delete every file in the TARGET_PATH + "/.bmad/bmb" directory with '*mpa*' in the filename.
    """
    bmb_path = os.path.join(target_path, ".bmad", "bmb")
    deleted_count = 0
    
    try:
        # Find all files with 'mpa' in the name
        for file_path in glob.glob(os.path.join(bmb_path, "*mpa*")):
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
                deleted_count += 1
        
        print(f"Deleted {deleted_count} files with 'mpa' in the filename")
        return True
    except Exception as e:
        print(f"Error deleting MPA files: {e}")
        return False

def delete_mpa_directories(target_path):
    """
    Delete every directory in the TARGET_PATH + "/.bmad/bmb" directory with '*mpa*' in the directory name.
    """
    bmb_path = os.path.join(target_path, ".bmad", "bmb")
    deleted_count = 0
    
    try:
        # Find all directories with 'mpa' in the name
        for dir_path in glob.glob(os.path.join(bmb_path, "*mpa*")):
            if os.path.isdir(dir_path):
                shutil.rmtree(dir_path)
                print(f"Deleted directory: {dir_path}")
                deleted_count += 1
        
        print(f"Deleted {deleted_count} directories with 'mpa' in the name")
        return True
    except Exception as e:
        print(f"Error deleting MPA directories: {e}")
        return False

def main():
    """
    Main uninstallation function.
    """
    print("BMAD MetaPromptAgent Uninstaller")
    print("=================================")
    
    # Find the target .bmad directory
    target_path = find_bmad_directory()
    print(f"Found .bmad directory at: {target_path}")
    
    # Save the absolute path as a constant
    TARGET_PATH = target_path
    print(f"TARGET_PATH = \"{TARGET_PATH}\"")
    
    # Restore the original config file from backup
    if not restore_config_file(TARGET_PATH):
        print("Failed to restore config file. Continuing with other uninstallation steps.")
    
    # Delete MPA files
    if not delete_mpa_files(TARGET_PATH):
        print("Failed to delete MPA files. Continuing with other uninstallation steps.")
    
    # Delete MPA directories
    if not delete_mpa_directories(TARGET_PATH):
        print("Failed to delete MPA directories. Continuing with other uninstallation steps.")
    
    print("\nUninstallation completed!")
    print(f"MetaPromptAgent has been uninstalled from: {TARGET_PATH}")

if __name__ == "__main__":
    main()
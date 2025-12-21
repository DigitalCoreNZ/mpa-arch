#!/usr/bin/env python3
"""
BMAD MetaPromptAgent Installer Script
This script installs the MetaPromptAgent configuration to a target BMAD system.
"""

import os
import sys
import subprocess
import shutil
import yaml

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
            print("Installation cancelled.")
            sys.exit(0)
        # Any other response (including empty) means try again

def backup_config_file(target_path):
    """
    Create a backup of the CORE Module Configuration file.
    """
    config_file = os.path.join(target_path, ".bmad", "core", "config.yaml")
    backup_file = config_file + ".bak"
    
    try:
        shutil.copy2(config_file, backup_file)
        print(f"Backup created: {backup_file}")
        return True
    except Exception as e:
        print(f"Error creating backup: {e}")
        return False

def append_yaml_config(source_file, target_file):
    """
    Append new key/value entries from source_file to target_file.
    This function handles dictionary merging rather than list merging.
    """
    try:
        # Check if target file exists
        if not os.path.exists(target_file):
            print(f"Error: Target config file not found at {target_file}")
            return False
        
        # Read the original target file content
        with open(target_file, 'r') as f:
            original_content = f.read()
        
        # Load existing data from the target file
        with open(target_file, 'r') as target:
            existing_data = yaml.safe_load(target) or {}
        
        # Load new data from the source file
        with open(source_file, 'r') as source:
            new_data = yaml.safe_load(source) or {}
        
        # Merge new data into existing data
        if isinstance(existing_data, dict) and isinstance(new_data, dict):
            existing_data.update(new_data)
        else:
            print("Data format mismatch: Both files should contain dictionaries.")
            return False
        
        # Write the updated data back to the target file
        with open(target_file, 'w') as target:
            # Write the original content first
            target.write(original_content)
            # Add a separator
            target.write("\n\n")
            # Write the new entries
            yaml.dump(new_data, target, default_flow_style=False)
        
        return True
    except Exception as e:
        print(f"Error updating configuration: {e}")
        return False

def copy_bmb_directory(source_path, target_path):
    """
    Copy the contents of the local .bmad/bmb directory to the target .bmad/bmb directory.
    """
    source_bmb = os.path.join(source_path, ".bmad", "bmb")
    target_bmb = os.path.join(target_path, ".bmad", "bmb")
    
    try:
        # Create target directory if it doesn't exist
        os.makedirs(target_bmb, exist_ok=True)
        
        # Copy all contents from source to target
        for item in os.listdir(source_bmb):
            source_item = os.path.join(source_bmb, item)
            target_item = os.path.join(target_bmb, item)
            
            if os.path.isdir(source_item):
                shutil.copytree(source_item, target_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, target_item)
        
        print(f"Successfully copied BMB directory contents to {target_bmb}")
        return True
    except Exception as e:
        print(f"Error copying BMB directory: {e}")
        return False

def main():
    """
    Main installation function.
    """
    print("BMAD MetaPromptAgent Installer")
    print("===============================")
    
    # Check if pyyaml is installed
    try:
        import yaml
    except ImportError:
        print("Error: pyyaml library is not installed.")
        print("Please install it with: pip install pyyaml")
        sys.exit(1)
    
    # Get the current directory (where the script is located)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find the target .bmad directory
    target_path = find_bmad_directory()
    print(f"Found .bmad directory at: {target_path}")
    
    # Save the absolute path as a constant
    TARGET_PATH = target_path
    print(f"TARGET_PATH = \"{TARGET_PATH}\"")
    
    # Create a backup of the config file
    if not backup_config_file(TARGET_PATH):
        print("Failed to create backup. Aborting installation.")
        sys.exit(1)
    
    # Append new configuration entries
    source_config = os.path.join(current_dir, "install.yaml")
    target_config = os.path.join(TARGET_PATH, ".bmad", "core", "config.yaml")
    
    if not append_yaml_config(source_config, target_config):
        print("Failed to update configuration. Aborting installation.")
        sys.exit(1)
    
    print("Configuration updated successfully.")
    
    # Copy the BMB directory contents
    if not copy_bmb_directory(current_dir, TARGET_PATH):
        print("Failed to copy BMB directory. Aborting installation.")
        sys.exit(1)
    
    print("\nInstallation completed successfully!")
    print(f"MetaPromptAgent has been installed to: {TARGET_PATH}")

if __name__ == "__main__":
    main()
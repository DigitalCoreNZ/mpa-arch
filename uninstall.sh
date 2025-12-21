#!/bin/bash

# BMAD MetaPromptAgent Uninstaller Script (Bash version)
# This script uninstalls the MetaPromptAgent configuration from a target BMAD system.

# Function to find the .bmad directory
find_bmad_directory() {
    while true; do
        # Ask for the location of the .bmad directory
        read -p "Please provide the location of the \".bmad\" directory: " location
        
        # Check if the provided location exists
        if [ ! -d "$location" ]; then
            echo "Error: The path '$location' does not exist."
            continue
        fi
        
        # Check if we can see the .bmad directory at the provided location
        bmad_path="$location/.bmad"
        if [ -d "$bmad_path" ]; then
            # Convert to absolute path and set global variable
            TARGET_PATH=$(cd "$location" && pwd)
            export TARGET_PATH
            return 0
        fi
        
        # If the provided location is within the .bmad directory, go up one level
        if [ "$(basename "$location")" = ".bmad" ]; then
            parent_dir=$(dirname "$location")
            bmad_path="$parent_dir/.bmad"
            if [ -d "$bmad_path" ]; then
                # Convert to absolute path and set global variable
                TARGET_PATH=$(cd "$parent_dir" && pwd)
                export TARGET_PATH
                return 0
            fi
        fi
        
        # If we can't find the .bmad directory, ask to try again or quit
        read -p 'I cannot find the ".bmad" directory. Want to try again [Y] or do you want to (Q)uit? ' response
        response=$(echo "$response" | tr '[:lower:]' '[:upper:]')
        
        # Default is to try again (Y)
        if [ "$response" = "Q" ]; then
            echo "Uninstallation cancelled."
            exit 0
        fi
        # Any other response (including empty) means try again
    done
}

# Function to restore the config file from backup
restore_config_file() {
    local target_path="$1"
    local config_file="$target_path/.bmad/core/config.yaml"
    local backup_file="$config_file.bak"
    
    # Check if backup file exists
    if [ ! -f "$backup_file" ]; then
        echo "Warning: Backup file not found at $backup_file"
        return 1
    fi
    
    # Delete the current config file if it exists
    if [ -f "$config_file" ]; then
        rm -f "$config_file"
        echo "Deleted current config file: $config_file"
    fi
    
    # Restore from backup
    if cp "$backup_file" "$config_file"; then
        echo "Restored config file from backup: $config_file"
        return 0
    else
        echo "Error restoring config file: $?"
        return 1
    fi
}

# Function to delete MPA files
delete_mpa_files() {
    local target_path="$1"
    local bmb_path="$target_path/.bmad/bmb"
    local deleted_count=0
    
    # Find and delete all files with 'mpa' in the name
    for file_path in "$bmb_path"/*mpa*; do
        if [ -f "$file_path" ]; then
            rm -f "$file_path"
            echo "Deleted file: $file_path"
            ((deleted_count++))
        fi
    done
    
    echo "Deleted $deleted_count files with 'mpa' in the filename"
    return 0
}

# Function to delete MPA directories
delete_mpa_directories() {
    local target_path="$1"
    local bmb_path="$target_path/.bmad/bmb"
    local deleted_count=0
    
    # Find and delete all directories with 'mpa' in the name
    for dir_path in "$bmb_path"/*mpa*; do
        if [ -d "$dir_path" ]; then
            rm -rf "$dir_path"
            echo "Deleted directory: $dir_path"
            ((deleted_count++))
        fi
    done
    
    echo "Deleted $deleted_count directories with 'mpa' in the name"
    return 0
}

# Main uninstallation function
main() {
    echo "BMAD MetaPromptAgent Uninstaller"
    echo "================================="
    
    # Find the target .bmad directory
    find_bmad_directory
    echo "Found .bmad directory at: $TARGET_PATH"
    echo "TARGET_PATH = \"$TARGET_PATH\""
    
    # Restore the original config file from backup
    if ! restore_config_file "$TARGET_PATH"; then
        echo "Failed to restore config file. Continuing with other uninstallation steps."
    fi
    
    # Delete MPA files
    if ! delete_mpa_files "$TARGET_PATH"; then
        echo "Failed to delete MPA files. Continuing with other uninstallation steps."
    fi
    
    # Delete MPA directories
    if ! delete_mpa_directories "$TARGET_PATH"; then
        echo "Failed to delete MPA directories. Continuing with other uninstallation steps."
    fi
    
    echo ""
    echo "Uninstallation completed!"
    echo "MetaPromptAgent has been uninstalled from: $TARGET_PATH"
}

# Run the main function
main "$@"
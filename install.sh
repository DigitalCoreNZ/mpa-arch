#!/bin/bash

# BMAD MetaPromptAgent Installer Script (Bash version)
# This script installs the MetaPromptAgent configuration to a target BMAD system.

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
            echo "Installation cancelled."
            exit 0
        fi
        # Any other response (including empty) means try again
    done
}

# Function to create a backup of the config file
backup_config_file() {
    local target_path="$1"
    local config_file="$target_path/.bmad/core/config.yaml"
    local backup_file="$config_file.bak"
    
    if [ ! -f "$config_file" ]; then
        echo "Error: Config file not found at $config_file"
        return 1
    fi
    
    if cp "$config_file" "$backup_file"; then
        echo "Backup created: $backup_file"
        return 0
    else
        echo "Error creating backup: $?"
        return 1
    fi
}

# Function to append YAML configuration
append_yaml_config() {
    local source_file="$1"
    local target_file="$2"
    
    if [ ! -f "$source_file" ]; then
        echo "Error: Source file not found at $source_file"
        return 1
    fi
    
    if [ ! -f "$target_file" ]; then
        echo "Error: Target file not found at $target_file"
        return 1
    fi
    
    # Check if yq is available for YAML manipulation
    if command -v yq &> /dev/null; then
        # Use yq to merge YAML files
        if yq eval-all 'select(fileIndex == 0) * select(fileIndex == 1)' "$target_file" "$source_file" > "$target_file.tmp" && mv "$target_file.tmp" "$target_file"; then
            echo "Configuration updated successfully using yq."
            return 0
        else
            echo "Error updating configuration with yq."
            return 1
        fi
    else
        # Fallback: simple append (not ideal for YAML but works if keys don't conflict)
        echo "Warning: yq not found. Using simple append method."
        echo "" >> "$target_file"
        cat "$source_file" >> "$target_file"
        echo "Configuration updated using simple append method."
        return 0
    fi
}

# Function to copy BMB directory
copy_bmb_directory() {
    local source_path="$1"
    local target_path="$2"
    local source_bmb="$source_path/.bmad/bmb"
    local target_bmb="$target_path/.bmad/bmb"
    
    if [ ! -d "$source_bmb" ]; then
        echo "Error: Source BMB directory not found at $source_bmb"
        return 1
    fi
    
    # Create target directory if it doesn't exist
    mkdir -p "$target_bmb"
    
    # Copy all contents from source to target
    if cp -r "$source_bmb"/* "$target_bmb/"; then
        echo "Successfully copied BMB directory contents to $target_bmb"
        return 0
    else
        echo "Error copying BMB directory: $?"
        return 1
    fi
}

# Main installation function
main() {
    echo "BMAD MetaPromptAgent Installer"
    echo "==============================="
    
    # Get the current directory (where the script is located)
    CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Find the target .bmad directory
    find_bmad_directory
    echo "Found .bmad directory at: $TARGET_PATH"
    echo "TARGET_PATH = \"$TARGET_PATH\""
    
    # Create a backup of the config file
    if ! backup_config_file "$TARGET_PATH"; then
        echo "Failed to create backup. Aborting installation."
        exit 1
    fi
    
    # Append new configuration entries
    SOURCE_CONFIG="$CURRENT_DIR/install.yaml"
    TARGET_CONFIG="$TARGET_PATH/.bmad/core/config.yaml"
    
    if ! append_yaml_config "$SOURCE_CONFIG" "$TARGET_CONFIG"; then
        echo "Failed to update configuration. Aborting installation."
        exit 1
    fi
    
    # Copy the BMB directory contents
    if ! copy_bmb_directory "$CURRENT_DIR" "$TARGET_PATH"; then
        echo "Failed to copy BMB directory. Aborting installation."
        exit 1
    fi
    
    echo ""
    echo "Installation completed successfully!"
    echo "MetaPromptAgent has been installed to: $TARGET_PATH"
}

# Run the main function
main "$@"
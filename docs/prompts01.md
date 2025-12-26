/bmad-bmb-bmad-builder

PROJECT NAME: MetaPromptAgent for BMAD v6 Public Alpha
PROJECT NAME, CONDENSED: MetaPromptAgent
PROJECT TARGET PLATFORM: BMAD v6-public-alpha
PROJECT VERSION: v0.3.2

I need your help building the MetaPromptAgent, an agent for BMAD v6-public-alpha that creates meta prompts. A meta prompt is a list of instructions that are performed by an LLM (Large Language Model). The workflow is:

Vibe Code (from the user) -> meta prompt (from an LLM, but guided by the MetaPromptAgent) -> LLM prompt (saved as a Markdown file and ready to be fed into an LLM prompt).

The MetaPromptAgent needs to provide the tools, within the prompts it creates, that help with fulfilling the instructions given to an AI. These tools include:

- Access to a browser,
- Access to the Internet,
- The ability to use the MCP protocol,
- The ability to create tasks and subtasks,
- The ability to send commands to the underlying OS,
- The ability to create, read, update, and delete files, and
- A playground where the MetaPromptAgent can build, and test, bash files, Python scripts, and TypeScript programs. (A quick, and quiet, test for Python3 and Node is needed to ensure the viability of the playground. Display a message to the user ONLY if the prerequisites have not been met.)

The MetaPromptAgent also needs to save the meta prompt as a Markdown file.

Are you in a position to help build this utility?

---

Create a Python script that:
1. Changes the names of the following files and directories, and
2. As each file or directory name is changed, reflect that change across the rest of the project files, before changing the next file or directory name:
- '.bmad/bmb/agents/mpa-agent.yaml' to 'mpa-agent.yaml',
- '.bmad/bmb/workflows/create-agent/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/mpa-compliance-check' to 'mpa-compliance-check',
- '.bmad/bmb/workflows/mpa-compliance-check/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/create-agent/mpa-agent.md' to 'mpa-agent.md',
- '.bmad/bmb/workflows/create-agent/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/create-mpa' to 'create-mpa',
- '.bmad/bmb/workflows/create-mpa/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/mpa-list-saved' to 'mpa-list-saved',
- '.bmad/bmb/workflows/mpa-list-saved/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/mpa-list-tools' to 'mpa-list-tools',
- '.bmad/bmb/workflows/mpa-list-tools/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/mpa-create' to 'mpa-create',
- '.bmad/bmb/workflows/mpa-create/mpa-create.md' to 'mpa-create.md',
- '.bmad/bmb/workflows/mpa-create/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/mpa-playground' to 'mpa-playground',
- '.bmad/bmb/workflows/mpa-playground/mpa-playground.md' to 'mpa-playground.md',
- '.bmad/bmb/workflows/mpa-playground/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/mpa-saved' to 'mpa-saved',
- '.bmad/bmb/workflows/mpa-saved/mpa-saved.md' to 'mpa-saved.md',
- '.bmad/bmb/workflows/mpa-saved/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/mpa-tools' to 'mpa-tools',
- '.bmad/bmb/workflows/mpa-tools/mpa-tools.md' to 'mpa-tools.md',
- '.bmad/bmb/workflows/mpa-tools/mpa-workflow.md' to 'mpa-workflow.md',
- '.bmad/bmb/workflows/mpa-test' to 'mpa-test', and
- '.bmad/bmb/workflows/mpa-test/mpa-workflow.md' to 'mpa-workflow.md'.

---

You will give the MetaPromptAgent in the '.bmad' directory a name. When the user starts using the MetaPromptAgent, it will identify herself as Aimee and then she will describe her purpose.

---

You will update the semver number, for the MetaPromptAgent project, from 'v0.3.0' to 'v0.3.2'.

---

Create a Python script called 'install.py'.

In Step 1. of the '### The Python Script Installer' section of the 'README.md' file, the user is required to manually install the pyYAML library:

```bash
pip install pyyaml
```

The purpose of this library will be covered later in this outline.

The script will ask for the location of the '.bmad' directory on the target system, e.g. 'Please provide the location of the ".bmad" directory: '.

The script will use the ```ls -al``` command to check if it can see the '.bmad' directory on the target system. If the provided location is within the '.bmad' directory, the script will use the ```cd ..``` command, followed by the ```ls -al``` command, to check if it can _now_ see the '.bmad' directory. If the '.bmad' directory can not be found on the target system, an error message is displayed, e.g. 'I cannot find the ".bmad" directory. Want to try again [Y] or do you want to (Q)uit?' Note that the 'Try Again' option is the default, where tapping the ENTER key without selecting an option, or providing an invalid option (other than 'Q'), results in the script looping back to the beginning.

When the '.bmad' directory is found on the target system, the script will save the absolute path to the directory as a constant, e.g. ```TARGET_PATH = "path/to/the/directory/containing/the/.bmad/directory"```

Next, create a backup copy of the CORE Module Configuration file on the target system, e.g. TARGET_PATH + "/.bmad/core/config.yaml" is copied as TARGET_PATH + "/.bmad/core/config.yaml.bak"

Next, use the following script to append new key/value entries to the target 'config.yaml' file:

```python
import yaml

def append_yaml(source_file, target_file):
    # Load existing data from the target file
    with open(target_file, 'a+') as target:
        target.seek(0)
        try:
            existing_data = yaml.safe_load(target) or []
        except yaml.YAMLError as e:
            print(f"Error reading {target_file}: {e}")
            return

        # Load new data from the source file
        with open(source_file, 'r') as source:
            try:
                new_data = yaml.safe_load(source) or []
            except yaml.YAMLError as e:
                print(f"Error reading {source_file}: {e}")
                return

        # Append new data to existing data
        if isinstance(existing_data, list) and isinstance(new_data, list):
            existing_data.extend(new_data)
        else:
            print("Data format mismatch: Both files should contain lists.")
            return

        # Write the updated data back to the target file
        target.seek(0)
        yaml.dump(existing_data, target, default_flow_style=False)
        target.truncate()

# Example usage:
# append_yaml('source.yaml', 'target.yaml')
append_yaml('install.yaml', str(TARGET_PATH) + '/.bmad/core/config.yaml')
```

Finally, the script will copy the contents of the local '.bmad/bmb' directory to the target "str(TARGET_PATH) + '/.bmad/bmb'" directory.

---

Next, create a Bash script called 'install.sh' that performs the same tasks as the 'install.py' script.

---

1. Create a Python script called 'uninstall.py'.

2. The script will ask for the location of the '.bmad' directory on the target system, e.g. 'Please provide the location of the ".bmad" directory: '.

The script will use the ```ls -al``` command to check if it can see the '.bmad' directory on the target system. If the provided location is within the '.bmad' directory, the script will use the ```cd ..``` command, followed by the ```ls -al``` command, to check if it can _now_ see the '.bmad' directory. If the '.bmad' directory can not be found on the target system, an error message is displayed, e.g. 'I cannot find the ".bmad" directory. Want to try again [Y] or do you want to (Q)uit?' Note that the 'Try Again' option is the default, where tapping the ENTER key without selecting an option, or providing an invalid option (other than 'Q'), results in the script looping back to the beginning.

3. When the '.bmad' directory is found on the target system, the script will save the absolute path to the directory as a constant, e.g. ```TARGET_PATH = "path/to/the/directory/containing/the/.bmad/directory"```

4. Delete the CORE Module Configuration file on the target system, e.g. TARGET_PATH + "/.bmad/core/config.yaml"

5. Restore the original CORE Module Configuration file that was copied as a backup during the installation, e.g. TARGET_PATH + "/.bmad/core/config.yaml.bak" is copied as TARGET_PATH + "/.bmad/core/config.yaml"

6. Delete every file in the TARGET_PATH + "/.bmad/bmb" directory with '*mpa*' in the filename.

7. Delete every directory in the TARGET_PATH + "/.bmad/bmb" directory with '*mpa*' in the directory name.

8. Create a Bash script called 'uninstall.sh' that performs every task in the 'uninstall.py' script.

---

Here is the terminal output from 'install.py':

```bash
Please provide the location of the ".bmad" directory: /home/brian/.roo/commands
Found .bmad directory at: /home/brian/.roo/commands
TARGET_PATH = "/home/brian/.roo/commands"
Backup created: /home/brian/.roo/commands/.bmad/core/config.yaml.bak
Configuration updated successfully.
Successfully copied BMB directory contents to /home/brian/.roo/commands/.bmad/bmb

Installation completed successfully!
MetaPromptAgent has been installed to: /home/brian/.roo/commands
```

---

Here is the output from running the 'uninstall.py' script:

```bash
BMAD MetaPromptAgent Uninstaller
=================================
Please provide the location of the ".bmad" directory: /home/brian/.roo/commands/.bmad
Found .bmad directory at: /home/brian/.roo/commands
TARGET_PATH = "/home/brian/.roo/commands"
Deleted current config file: /home/brian/.roo/commands/.bmad/core/config.yaml
Restored config file from backup: /home/brian/.roo/commands/.bmad/core/config.yaml
Deleted 0 files with 'mpa' in the filename
Deleted 0 directories with 'mpa' in the name

Uninstallation completed!
MetaPromptAgent has been uninstalled from: /home/brian/.roo/commands
```

Restoring the config file works. I checked. However, the deletion of the files, followed by the deletion of the directories, fails. I checked.

---

The 'install.py' script is overwriting the '{project-root}/core/config.yaml' file rather than appending the contents of the 'install.yaml' file to the config file.

---

Change the semver from 'v0.3.1' to 'v0.3.2'. Propagate this change throughout the project.

---

The current issue is that the 'Meta Prompt Agent' mode wants to access the user profile but keeps looking in the wrong place. Is it possible to fix this issue by adding an entry to the `install.yaml` file that points to the location of the user profile?
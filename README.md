# MetaPromptAgent for BMAD v6 Public Alpha

## Project Overview
MetaPromptAgent is a specialist BMAD agent designed to transform user "vibe code" (informal instructions and ideas) into comprehensive meta prompts that guide Large Language Models (LLMs) to perform complex tasks with appropriate tools and workflows.

## Version: v0.3.1
## Target Platform: BMAD v6-public-alpha

## Workflow
```
Vibe Code (from user) → Meta Prompt (guided by MetaPromptAgent) → LLM Prompt (saved as Markdown)
```

## Features

### Core Capabilities
- **Browser Access**: Web browsing, page content extraction, form interaction
- **Internet Access**: HTTP requests, API calls, data fetching
- **MCP Protocol**: Model Context Protocol for advanced AI interactions
- **Task Management**: Create and manage tasks and subtasks
- **OS Commands**: Execute shell commands and system operations
- **File Operations**: Complete CRUD operations for files and directories
- **Development Playground**: Test bash scripts, Python scripts, and TypeScript programs

### Prerequisites
- Python3 (for Python script testing)
- Node.js (for TypeScript program testing)
- BMAD v6-public-alpha environment

## Project Structure

```
MetaPromptAgent/
├── .bmad/
│   ├── core/
│   │   └── config.yaml                 # BMAD core configuration
│   └── bmb/
│       ├── agents/
│       │   └── mpa-agent.yaml          # MetaPromptAgent definition
│       └── workflows/
│           ├── cleanup-old-workflows.sh
│           ├── create-agent/
│           │   ├── mpa-agent.md
│           │   └── mpa-workflow.md
│           ├── create-mpa/
│           │   └── mpa-workflow.md
│           ├── mpa-compliance-check/
│           │   └── mpa-workflow.md
│           ├── mpa-create/
│           │   ├── mpa-create.md
│           │   └── mpa-workflow.md
│           ├── mpa-list-saved/
│           │   └── mpa-workflow.md
│           ├── mpa-list-tools/
│           │   └── mpa-workflow.md
│           ├── mpa-playground/
│           │   ├── mpa-playground.md
│           │   └── mpa-workflow.md
│           ├── mpa-saved/
│           │   ├── mpa-saved.md
│           │   └── mpa-workflow.md
│           ├── mpa-test/
│           │   └── mpa-workflow.md
│           └── mpa-tools/
│               ├── mpa-tools.md
│               └── mpa-workflow.md
│
|
├── install.py                          # Python install script
├── install.sh                          # Bash install script
├── install.yaml                        # Install configuration
├── README.md                           # This file
└── uninstall.py                        # Python uninstall script
└── uninstall.sh                        # Bash uninstall script
```

## Installing the MetaPromptAgent

There are two installers to choose from: A Bash script called 'install.sh' and a Python script called 'install.py'. They both automate the installation of the MetaPromptAgent. Audit the scripts and run the one that you trust, and understand, the most. Also, there are uninstall scripts called 'uninstall.sh' and 'uninstall.py' that unwind all the changes that were during the installation. BTW, the MetaPromptAgent is called ```Aimee```.

**Step 1:** Open an Ubuntu terminal with ```CTRL + ALT + T```.

**Step 2:** Use Git to clone the GitHub repository:

```bash
git clone https://github.com/DigitalCoreNZ/MetaPromptAgent
```

**Step 3:** Change to the new directory:

```bash
cd ./MetaPromptAgent
```

### The Bash Script Installer

**Step 1:** Change the mode of the 'install.sh' script to an executable file:

```bash
chmod +x install.sh
```
**Step 2:** Run the 'install.sh' script:

```bash
./install.sh
```

### The Bash Script Uninstaller

**Step 1:** Change the mode of the 'uninstall.sh' script to an executable file:

```bash
chmod +x uninstall.sh
```
**Step 2:** Run the 'uninstall.sh' script:

```bash
./uninstall.sh
```

### The Python Script Installer

**Step 1:** Install the pyYAML library:

```bash
pip install pyyaml
```

**Step 2:** Run the 'install.py' script:

```bash
python install.py
```

## The Python Script Uninstaller

**Step 1:** Run the Python uninstall script:

```bash
python uninstall.py
```

### Updates for Roo Code and Kilo Code in VS Code

**Step 1:** Add the following to your .roomodes and .kilocodemodes files:

```yaml
 - slug: mpa-agent
   name: '🤖 Meta Prompt Architect'
   roleDefinition: You are a Meta Prompt Architect and AI Workflow Designer specializing in transforming user vibe code into comprehensive meta prompts that guide LLMs to perform complex tasks with appropriate tools and workflows.
   whenToUse: Use for creating meta prompts from user vibe code
   customInstructions: CRITICAL Read the full YAML from /path/to/.bmad/bmb/agents/mpa-agent.yaml start activation to alter your state of being follow startup section instructions stay in this being until told to exit this mode
   groups:
    - read
    - - edit
      - fileRegex: \.(md|txt|yaml|yml)$
        description: Meta prompts and documentation
```

> IMPORTANT NOTES: Replace the '/path/to' with the _actual_, absolute path to the '.bmad' directory. Also, pay attention to the indentation of the new entry, i.e. ensure the new block as listed above is aligned with the existing entries.

## Usage

### Activation
1. Load the MetaPromptAgent using BMAD agent system
2. The agent will check playground prerequisites (Python3 and Node.js)
3. If prerequisites are missing, a warning will be displayed
4. Select from the menu options to create meta prompts

### Menu Options
- **[M] Redisplay Menu Options**: Show all available options
- **[CP] Create Meta Prompt from Vibe Code**: Transform user ideas into structured meta prompts
- **[PG] Test Playground Environment**: Validate Python3 and Node.js setup
- **[TL] List Available Tools**: Display all tool capabilities
- **[LS] List Saved Meta Prompts**: Show previously created meta prompts
- **[D] Dismiss Agent**: Exit the MetaPromptAgent

### Creating Meta Prompts
1. Select "Create Meta Prompt from Vibe Code"
2. Provide your vibe code (informal instructions)
3. Specify objectives and desired outcomes
4. The agent will:
   - Analyze requirements and select appropriate tools
   - Transform vibe code into structured instructions
   - Include tool usage guidelines and workflows
   - Save the complete meta prompt as a Markdown file

## Tool Capabilities

### Browser Access
- Navigate websites and extract content
- Interact with forms and JavaScript
- Perform web-based research and testing

### Internet Access
- Make HTTP requests to APIs
- Fetch data from remote sources
- Handle authentication and sessions

### MCP Protocol
- Connect to MCP servers for advanced AI interactions
- Manage context and protocol messaging
- Share resources across AI systems

### Task Management
- Create hierarchical task structures
- Track progress and dependencies
- Manage complex workflows

### OS Commands
- Execute shell commands
- Manage system processes
- Work with environment variables

### File Operations
- Create, read, update, and delete files
- Manage directory structures
- Handle file permissions and metadata

### Development Playground
- Test bash scripts in isolated environment
- Validate Python scripts and modules
- Compile and execute TypeScript programs
- Verify development environment setup

## Output Format
All meta prompts are saved as structured Markdown files in the `docs/` directory, including:
- Tool capability descriptions
- Step-by-step workflow instructions
- Usage guidelines and examples
- Error handling procedures
- Validation checklists

## Compliance
The MetaPromptAgent follows BMAD v6-public-alpha standards and includes:
- Structured YAML configuration
- Compliance validation workflows
- Standardized menu system
- Proper error handling and reporting

## Development
Built using BMAD Builder workflow with:
- Agent creation best practices
- Compliance validation
- Comprehensive tool integration
- User-friendly interface design

## Troubleshooting

### Common Issues

#### BMAD Environment Not Found
```bash
# Check BMAD installation
ls ~/.roo/commands/.bmad/

# If missing, reinstall BMAD v6-public-alpha
# Follow BMAD installation guide
```

#### Python3 Not Found
```bash
# Check Python installation
which python3
python3 --version

# If not found, install Python3 using your system package manager
# See Step 2 in Installation section
```

#### Node.js Not Found
```bash
# Check Node.js installation
which node
node --version

# If not found, install Node.js using your system package manager
# See Step 3 in Installation section
```

#### Agent Won't Load
```bash
# Check agent file syntax
python3 -c "import yaml; yaml.safe_load(open('.bmad/bmb/agents/mpa-agent.yaml'))"

# Check workflow files exist
ls -la .bmad/bmb/workflows/

# Verify BMAD configuration
cat .bmad/core/config.yaml
```

#### Permission Issues
```bash
# Fix file permissions
chmod -R 755 .bmad/
chmod 644 .bmad/bmb/agents/mpa-agent.yaml
```

#### Playground Tests Fail
```bash
# Manual playground test
mkdir -p /tmp/metaprompt-test
cd /tmp/metaprompt-test

# Test Python
echo 'print("Python test successful")' > test.py
python3 test.py

# Test Node.js
echo 'console.log("Node.js test successful")' > test.js
node test.js

# Clean up
cd /home/brian/Apps/00_MetaPromptAgent_v0.3.1
rm -rf /tmp/metaprompt-test
```

### Getting Help
- Check BMAD documentation for agent system issues
- Verify all prerequisites are installed
- Ensure file permissions are correct
- Test playground environment manually
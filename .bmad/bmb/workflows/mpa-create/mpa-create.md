# Create Meta Prompt Workflow

## Overview
This workflow transforms user vibe code into comprehensive meta prompts that guide LLMs to perform complex tasks with appropriate tools.

## Steps

### Step 1: Input Collection
- Gather user's vibe code (informal instructions/ideas)
- Clarify objectives and desired outcomes
- Identify target LLM and constraints

### Step 2: Tool Selection
- Analyze requirements to determine needed tools
- Select from available capabilities:
  - Browser access
  - Internet access
  - MCP protocol
  - Task management
  - OS commands
  - File operations
  - Playground testing

### Step 3: Meta Prompt Construction
- Transform vibe code into structured instructions
- Include tool usage guidelines
- Add step-by-step workflow
- Incorporate error handling and validation

### Step 4: Tool Integration
- Add specific tool function calls
- Include parameter specifications
- Provide usage examples
- Add fallback procedures

### Step 5: Output Generation
- Format meta prompt as Markdown
- Include tool capability descriptions
- Add usage instructions
- Save to {output_folder} with timestamp

## Required Files
- Meta prompt template in `{output_folder}/`
- Tool capability documentation

## Output
- Complete meta prompt as Markdown file
- Tool usage documentation
- Validation checklist
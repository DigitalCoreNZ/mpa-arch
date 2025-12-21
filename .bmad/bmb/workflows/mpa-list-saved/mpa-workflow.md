# List Saved Meta Prompts Workflow

## Overview
This workflow displays all previously saved meta prompts in the output directory.

## Steps

### Step 1: Directory Scan
- Access {output_folder} from configuration
- Scan for Markdown files containing meta prompts
- Filter by meta prompt naming convention

### Step 2: File Analysis
- Read meta prompt headers
- Extract creation timestamps
- Identify tool capabilities used
- Summarize prompt objectives

### Step 3: Display Formatting
- Sort by creation date (newest first)
- Format as numbered list
- Include file names and descriptions
- Show tool usage summary

### Step 4: Quick Actions
- Provide options to view specific prompts
- Offer to edit existing prompts
- Suggest prompt reuse opportunities

## Required Files
- Meta prompt files in {output_folder}
- Directory access permissions

## Output
- Formatted list of saved meta prompts
- File details and summaries
- Quick action options
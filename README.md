# GHDoc-temp

Template for Grasshopper project documentation

## Project Description

This project contains documentation and examples for working with Rhinoceros Grasshopper using IronPython 2.7.

## Project Structure

```
GHDoc-temp/
├── Doc/                    # Project documentation
│   ├── ConduitRunsHeight.md
│   ├── Suspension.md
│   └── ...
├── Gh/                     # Grasshopper files
│   ├── ConduitRunsHeight.gh
│   ├── git_help.gh
│   ├── Suspension.gh
│   └── ...
├── Help/                   # Reference information
│   ├── Markdown.md
│   └── ...
├── Py/                     # Python scripts
│   ├── git_help.py
│   └── ...
└── README.md              # README
```

## Documentation

### Main Documentation

[**Documentation**](./Doc/index.md)

### Reference Information

- [**Markdown Guide**](./Help/Markdown.md) - Markdown usage guide
- [**Mermaid Guide**](./Help/Mermaid.md) - Mermaid usage guide

## Quick Start

1. Save the `.gh` file in the `./Gh` directory (without using "_001", "v0.001", etc. in the name)
2. Import content from the `./Gh/git_help.gh` file
3. The imported script has the following parameters:
    
    **Inputs:**
    
    - `OPEN_MAIN_BRANCH`: Boolean - opens the main repository branch on GitHub
    - `OPEN_HELP_IN_GITHUB`: Boolean - opens the current file's documentation on GitHub
    - `OPEN_LOCAL_HELP`: Boolean - opens the local .md documentation file in the editor
    
    **Output:**
    
    - `md`: String - content of the local .md documentation file

> [!important] 
> `OPEN_HELP_IN_GITHUB` opens documentation on the current active repository branch, while `OPEN_MAIN_BRANCH` always opens documentation on the main `main` branch. This allows you to view both the current version of documentation and the stable version from the main branch.

1. If you press `OPEN_HELP_IN_GITHUB` or `OPEN_LOCAL_HELP` and there is no file with such a name in the `./Doc` directory, it will be created automatically

> [!important] 
> The Grasshopper file name and Markdown file name must match!

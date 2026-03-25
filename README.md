# Regex Trainer-Viewer
 
**Interactive Python tool for practicing regular expressions against text files.**
 
Load any text file, type regex patterns, and instantly see all matches with their positions. Can also be used as a simple text file viewer.
 
## Features
 
- Loads a file into memory and lets you test regex patterns interactively
- Displays each match with its `span` position
- Quick commands to view the loaded text
- Configurable default filename
 
## Requirements
 
- Python 3.x
 
## Usage
 
```bash
python regex.py
```
 
## Configuration
 
In `regex.py`:
 
```python
# Set to True to always use the default file
fixfilename = False
 
# Default filename (used when fixfilename = True)
default_name = "sample"
```
 
## Tech
 
`Python` · `re` (regex)
 

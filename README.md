# Regex Trainer-Viewer (Python)

A tiny interactive tool to practice regular expressions (`re`) against any text file that you can input its name or even specify the name of the default fallback file from the code.

## What it does
- Loads a file into memory as one string (`data`)
- Lets you type regex patterns repeatedly
- Prints each match and its position (`span`)
- Includes quick commands to view the loaded text

 *it can be used as text-file-viewer

## Requirements
- Python 3.x

# Run
```bash
python regex.py
```

## Regex.py configuration## 

# to fix the filename to the default, change this to True:
```bash
fixfilename = False

```
# To set the default filename ( make sure "fixfilename = True" ):

`````bash


default_name = "sample"


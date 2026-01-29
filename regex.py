# tiny code to parse any text file and train your regex skills  py4e inspired
import re

fixfilename = False # <--- Set to True to fix the name to a specific one - default = "sample"
default_name = "sample" #<---- Change this to any name - default sample 

def loadfile():
    filename = input("input filename: ").strip()

    if fixfilename and filename != default_name:
        filename = default_name
        print("name corrected to", filename, "to disable option, set fixfilename = False")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print("file loading error:", e)
        quit()

data = loadfile()
original_data = data

def regex_trainer():
    while True:
        pat = input("pattern (q=quit, v=view, n=view first N chars): ").strip()

        if pat.lower() in ("q", "quit", "exit"):
            break

        if pat.lower() == "v":
            print(original_data)
            continue

        if pat.lower().startswith("n "):
            # example: n 500
            try:
                n = int(pat.split(maxsplit=1)[1])
                print(original_data[:n])
            except ValueError:
                print("Usage: n 500")
            continue

        try:
            pattern = re.compile(pat)
        except re.error as e:
            print("Invalid regex:", e)
            continue

        for match in pattern.finditer(data):
            print(match.group(0), "at", match.span())

regex_trainer()

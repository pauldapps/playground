import re
import sys
from pathlib import Path

"""
Powershell equivalent:
Get-Content -Path C:\temp\file.txt | Select-String -Pattern "Hello There"
"""

# Builds a Select-String compatible object for outputing in JSON.
class OutRe:
    def __init__(self):
        pass


def main(
    file_path: str = r".",
    pattern: str = "Engine",
):
    out_matches = []
    file_path = Path(file_path).resolve()

    if file_path.is_file() and file_path.exists():
        to_process = []
        to_process.append(file_path)

    elif file_path.is_dir() and file_path.exists():
        to_process = [i for i in file_path.iterdir() if i.is_file() == True]

    for file_obj in to_process:
        with open(file_obj, "r") as f:
            out_matches += [
                out for l in f.readlines() if (out := re.search(pattern, l)) != None
            ]

    return out_matches


if __name__ == "__main__":
    print(main(*sys.argv[1:]))

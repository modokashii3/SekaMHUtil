from pathlib import Path
import re

SEARCH_STRING = "ネルギガンテ"
CONTEXT_LENGTH = 500

for file_path in Path(".").rglob("*_jpn.gmd"):  
    with file_path.open("rb") as file:  
        contents = file.read().decode(errors="ignore")
        
        if SEARCH_STRING in contents:
            print(file_path)

            strings = contents.split('\x00')
            
            for string in filter(lambda s: SEARCH_STRING.lower() in s.lower(), strings):
                lines = string.strip().split('\n')
                print(f"* {lines[0]}")
                for line in lines[1:]:
                    print(f"  {line.strip()}")
                
input("Press Enter to exit...")

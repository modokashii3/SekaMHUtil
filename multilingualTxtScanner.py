import unicodedata
from pathlib import Path

def normalize_japanese_text(text):
    return unicodedata.normalize('NFKC', text)

def search_files(search_string, context_length):
    for file_path in Path(".").rglob("*.txt"):
        try:
            with file_path.open("r", encoding="utf-8") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    normalized_line = normalize_japanese_text(line)
                    if search_string in normalized_line:
                        print(f"Found '{search_string}' in {file_path} at line {i+1}")
                        start = max(0, i - context_length)
                        end = min(len(lines), i + context_length + 1)
                        for j, prox_line in enumerate(lines[start:end]):
                            if j == context_length:
                                print(f"* {prox_line.strip()}")
                            else:
                                print(f"  {prox_line.strip()}")
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

def main():
    search_string = "father"
    context_length = 1
    search_files(search_string, context_length)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

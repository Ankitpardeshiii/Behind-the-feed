import json
from pathlib import Path
from .parser import parse_chunk


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def split_into_chunks(text):
    return [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]


def convert_to_json(input_file, output_file=None):
    text = read_file(input_file)
    chunks = split_into_chunks(text)

    users = []

    for chunk in chunks:
        try:
            user = parse_chunk(chunk)
            if user:
                users.append(user)
        except Exception as e:
            print(f"Skipping a chunk due to error: {e}")

    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4, ensure_ascii=False)

    return users
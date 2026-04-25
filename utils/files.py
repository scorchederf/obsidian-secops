import os
import shutil


def ensure_folder(path):
    os.makedirs(path, exist_ok=True)


def ensure_parent_folder(filepath):
    folder = os.path.dirname(filepath)
    if folder:
        ensure_folder(folder)


def remove_folder_if_exists(path):
    if os.path.isdir(path):
        shutil.rmtree(path)


def read_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def write_text_file(filepath, content):
    ensure_parent_folder(filepath)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

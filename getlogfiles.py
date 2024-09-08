import os
import shutil
from tkinter import Tk, filedialog

def select_folder(title):
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title=title)

def copy_log_files(source_dir, dest_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".log"):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, file)
                shutil.copy2(source_path, dest_path)
                print(f"Скопирован файл: {file}")

def main():
    source_dir = select_folder("Выберите папку с логами")
    if source_dir:
        dest_dir = select_folder("Выберите папку для сохранения логов")
        if dest_dir:
            copy_log_files(source_dir, dest_dir)
            print("Копирование завершено.")

if __name__ == "__main__":
    main()

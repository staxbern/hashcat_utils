import os
from tkinter import Tk, filedialog, messagebox

def parse_file(file):
    result = {}
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                key_value = line.strip().split(':')
                if len(key_value) == 2:
                    key, value = key_value
                    if key and value:
                        if key not in result:
                            result[key] = []
                        result[key].append(value)
                else:
                    print(f"Некорректный формат строки в файле {file}: {line.strip()}")
        return result
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось прочитать файл '{file}': {str(e)}")
        return None

def process_files():
    # Create a hidden Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the main window

    # Open file dialogs to select input files
    mail_hash_file = filedialog.askopenfilename(title="Выберите файл с почтой и хешами (1.txt)", filetypes=[("Text Files", "*.txt")])
    hash_password_file = filedialog.askopenfilename(title="Выберите файл с хешами и паролями (2.txt)", filetypes=[("Text Files", "*.txt")])

    if not mail_hash_file or not hash_password_file:
        messagebox.showwarning("Предупреждение", "Оба файла должны быть выбраны!")
        return

    # Parse both files
    mail_hashes = parse_file(mail_hash_file)
    hash_passwords = parse_file(hash_password_file)

    if mail_hashes is None or hash_passwords is None:
        return

    # Generate result lines
    result_lines = []
    for mail, hashes in mail_hashes.items():
        for hash_ in hashes:
            if hash_ in hash_passwords:
                for password in hash_passwords[hash_]:
                    result_lines.append(f"{mail}:{password}")

    # Save results to a file
    if result_lines:
        save_file = filedialog.asksaveasfilename(title="Сохранить результаты как", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_file:
            try:
                with open(save_file, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(result_lines))
                messagebox.showinfo("Успех", f"Результаты успешно записаны в файл '{save_file}'!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")
    else:
        messagebox.showinfo("Результат", "Совпадений не найдено. Попробуйте выбрать mail:hash в качестве 1 файла, а hash:pass в качестве 2!")

if __name__ == "__main__":
    process_files()

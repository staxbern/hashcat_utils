import os
from tkinter import Tk, filedialog, messagebox

def extract_values(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # Извлекаем значения до символа ":"
        return [line.strip().split(':')[0] for line in lines if ':' in line]
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось прочитать файл '{file}': {str(e)}")
        return None

def save_values(file, values):
    try:
        with open(file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(values))
        messagebox.showinfo("Успех", f"Значения успешно сохранены в файл '{file}'!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")

def process_file():
    # Создаем скрытое окно Tkinter
    root = Tk()
    root.withdraw()

    # Открываем диалоговое окно для выбора входного файла
    input_file = filedialog.askopenfilename(title="Выберите входной файл", filetypes=[("Text Files", "*.txt")])

    if not input_file:
        messagebox.showwarning("Предупреждение", "Файл должен быть выбран!")
        return

    # Извлекаем значения из входного файла
    values = extract_values(input_file)

    if values is None:
        return

    # Открываем диалоговое окно для выбора выходного файла
    output_file = filedialog.asksaveasfilename(title="Сохранить значения как", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if output_file:
        save_values(output_file, values)

if __name__ == "__main__":
    process_file()

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog, messagebox
from pathlib import Path
import sys
import os
import webbrowser



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / 'assets' / 'frame0'
TOOLS_PATH = OUTPUT_PATH / 'tools'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    
def relative_to_tools(path: str) -> Path:
    return TOOLS_PATH / Path(path)


def run_exodus2hashcat():                                                                   #exodus2hashcat
    # Открываем диалоговое окно для выбора файла
    file_path = filedialog.askopenfilename()
    
    # Сохраняем выбранный путь файла в переменную path_file_edit
    path_file_edit = file_path
    
    # Запускаем скрипт exodus2hashcat.py с выбранным файлом
    os.system(f'python tools/exodus2hashcat.py {path_file_edit}')
    

def run_metamask2hashcat():                                                                   #metamask2hashcat
    # Открываем диалоговое окно для выбора файла
    file_path = filedialog.askopenfilename()
    
    # Сохраняем выбранный путь файла в переменную path_file_edit
    path_file_edit = file_path
    
    # Запускаем скрипт exodus2hashcat.py с выбранным файлом
    os.system(f'python tools/metamask2hashcat.py --vault {path_file_edit}')
    
def run_truecrypt2hashcat():                                                                   #truecrypt2hashcat
    # Открываем диалоговое окно для выбора файла
    file_path = filedialog.askopenfilename()
    
    # Сохраняем выбранный путь файла в переменную path_file_edit
    path_file_edit = file_path
    
    # Запускаем скрипт exodus2hashcat.py с выбранным файлом
    os.system(f'python tools/truecrypt2hashcat.py {path_file_edit}')








window = Tk()

window.title("HashCatUtils 0.2")
window.configure(bg = "#000000")
window.geometry("517x419")

icon_path = relative_to_assets("HashCatUtils.ico")
window.iconbitmap(str(icon_path))

logo = '''
███████████████████████████████████████████████████████████████████████████████████████
██████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
████░▀████ >MEOW ███▀░████░░██╗░░██╗░█████╗░░██████╗██╗░░██╗░█████╗░░█████╗░████████╗██
███▌▒▒░████████████░▒▒▐███░░██║░░██║██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██
███░▒▒▒░██████████░▒▒▒░███░░███████║███████║╚█████╗░███████║██║░░╚═╝███████║░░░██║░░░██
██▌░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▐██░░██╔══██║██╔══██║░╚═══██╗██╔══██║██║░░██╗██╔══██║░░░██║░░░██
██░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░██░░██║░░██║██║░░██║██████╔╝██║░░██║╚█████╔╝██║░░██║░░░██║░░░██
████▀▀▀██▄▒▒▒▒▒▒▒▄██▀▀▀█▐█░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░██
███░░░▐█░▀█▒▒▒▒▒█▀░█▌░░░▐█░░░░░██╗░░░██╗████████╗██╗██╗░░░░░░██████╗░░░░░░░░░░░░░░░░░██
██▐▌░░░▐▄▌░▐▌▒▒▒▐▌░▐▄▌░░▐█░░░░░██║░░░██║╚══██╔══╝██║██║░░░░░██╔════╝░ Version: 0.2 ░░██
██▐░░░▐█▌░░▌▒▒▒▐░░▐█▌░░█▐█░░░░░██║░░░██║░░░██║░░░██║██║░░░░░╚█████╗░░░░░░░░░░░░░░░░░░██
██▒▀▄▄▄█▄▄▄▌░▄░▐▄▄▄█▄▄▀▒██░░░░░██║░░░██║░░░██║░░░██║██║░░░░░░╚═══██╗░░░░░░░░░░░░░░░░░██
███░░░░░░░░░└┴┘░░░░░░░░░██░░░░░╚██████╔╝░░░██║░░░██║███████╗██████╔╝░░░░░░░░░░░░░░░░░██
████▄▄░░░░░░░░░░░░░░▄▄████░░░░░░╚═════╝░░░░╚═╝░░░╚═╝╚══════╝╚═════╝░░░░░░░░░░░░░░░░░░██
███████████████████████████████████████████████████████████████████████████████████████
'''

print(logo)

canvas = Canvas(
    window,
    bg = "#000000",
    height = 419,
    width = 517,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open('https://t.me/Ludonate/', new=2),
    relief="flat"
)
button_1.place(
    x=18.2255859375,
    y=152.45733642578125,
    width=226.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open('https://t.me/hashcat_utils', new=2),
    relief="flat"
)
button_2.place(
    x=271.2255859375,
    y=152.45733642578125,
    width=226.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python tools/getlogin.py'),
    relief="flat"
)
button_3.place(
    x=14.2255859375,
    y=199.45733642578125,
    width=234.9591827392578,
    height=37.84577560424805
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=run_exodus2hashcat,
    relief="flat"
)
button_4.place(
    x=266.53076171875,
    y=199.45733642578125,
    width=234.9591827392578,
    height=37.84577560424805
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python tools/getpass.py'),
    relief="flat"
)
button_5.place(
    x=14.2255859375,
    y=254.64910888671875,
    width=234.9591827392578,
    height=37.84577560424805
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=run_metamask2hashcat,
    relief="flat"
)
button_6.place(
    x=266.53076171875,
    y=254.64910888671875,
    width=234.9591827392578,
    height=37.84577560424805
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python tools/mailpassfromhash.py'),
    relief="flat"
)
button_7.place(
    x=15.802490234375,
    y=365.0326232910156,
    width=234.9591827392578,
    height=37.84577560424805
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python tools/gethashtype.py'),
    relief="flat"
)
button_8.place(
    x=15.802490234375,
    y=309.8408508300781,
    width=234.9591827392578,
    height=37.84577560424805
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python tools/getlogfiles.py'),
    relief="flat"
)
button_9.place(
    x=266.2255859375,
    y=365.45733642578125,
    width=235.0,
    height=37.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=run_truecrypt2hashcat,
    relief="flat"
)
button_10.place(
    x=266.53076171875,
    y=309.8408508300781,
    width=234.9591827392578,
    height=37.84577560424805
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open('https://lolz.live/threads/7562028/', new=2),
    relief="flat"
)
button_11.place(
    x=14.192138671875,
    y=17.345947265625,
    width=485.6874694824219,
    height=108.80660247802734
)
window.resizable(False, False)
window.mainloop()

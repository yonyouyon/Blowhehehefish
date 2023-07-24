import tkinter as tk
from tkinter import ttk
import soft
from tkinter.messagebox import showerror

app = tk.Tk()
app.title('BlowFish')
app.resizable(False, False)
w = app.winfo_screenwidth()
h = app.winfo_screenheight()
w = w//2
h = h//2
w = w - 200
h = h - 200
app.geometry('370x350+{}+{}'.format(w, h))

ram = ttk.Frame(app, padding=10) 
ram2 = ttk.Frame(app)
ram3 = ttk.Frame(app, padding=10)

text_label = ttk.Label(ram, text='Исходный текст:', font = ('Andale Mono', 14))
text_label.grid(column=0, row=0, sticky='w')


key_label = ttk.Label(ram, text='Ключ шифрования:', font = ('Andale Mono', 14))
key_label.grid(column=0, row=1, sticky='w')


text_input = tk.StringVar()
key_input = tk.StringVar()

text = tk.Text(ram, height=6, width=30)
text.grid(column=1, row=0, sticky='w')

key = tk.Text(ram, height=6, width=30)
key.grid(column=1, row=1, sticky='w')

dict = ['Зашифровать', 'Дешифровать']


def select():
    selection = cmd.get()
    return selection


cmd = ttk.Combobox(ram2, values=dict, state="readonly")
cmd.grid(row=2, column=1, sticky='we')
cmd.bind('<<ComboboxSelected>>', select)


def retrieve_txt():
    txt = text.get('1.0','end-1c')
    return txt


def retrieve_key():
    kkey = key.get('1.0','end-1c')
    return kkey


def click():
    selection = cmd.get()
    txt = retrieve_txt()
    key = retrieve_key()
    try:
        output_text.delete('1.0','end')
        
        result = soft.main(selection, txt, key)
        output_text.insert('1.0', result)
        return result
    except ValueError as error:
        showerror(title='Error', message=error)


cryp = tk.Button(ram2, text='blowfish!', command=click, width=10, font = ('Andale Mono', 12))
cryp.grid( row=2, sticky='we')

output_label = ttk.Label(ram3, text='Готовый текст:  ', font = ('Andale Mono', 14))
output_label.grid(column=0, row=3, sticky='w')


output_text = tk.Text(ram3, height=6, width=30)
output_text.grid(column=1, row=3, sticky='w')


def copy():
    try:
        app.clipboard_clear()
        app.clipboard_append(output_text.get('1.0', 'end'))
    except:
        app.clipboard_append('ERROR')


Copy = ttk.Button(ram3, text="Copy", command=copy).grid()


Off = ttk.Button(ram3, text="Cancel", command=app.destroy)
Off.grid(column = 1, row = 4, sticky='w')


ram.grid()
ram2.grid()
ram3.grid()

app.mainloop()
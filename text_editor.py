import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import random
from gtts import gTTS
import os


def generate_random_motivation_sentence():
    motivational_sentences = [
        "Dream big, work hard, stay focused.",
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Your time is limited, don't waste it living someone else's life.",
        "Believe you can, and you're halfway there.",
        "Strive for progress, not perfection.",
        "The only place where success comes before work is in the dictionary.",
        "Don't watch the clock; do what it does. Keep going.",
        "Your attitude determines your direction.",
        "The harder you work for something, the greater you'll feel when you achieve it."
    ]

    return random.choice(motivational_sentences)


def open_file(window, text_edit):
    file_path = askopenfilename(filetypes=[('Text Files, ', '*.txt')])

    if not file_path:
        return

    text_edit.delete(1.0, tk.END)
    with open(file_path, 'r') as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f'Open File: {file_path}')


def save_file(window, text_edit):
    file_path = asksaveasfilename(filetypes=[('Text Files', '*.txt')])

    if not file_path:
        return

    with open(file_path, 'w') as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f'Save File: {file_path}')


def read_aloud(text, speed=1.0):
    tts = gTTS(text=text, lang='en', slow=speed < 1.0)
    tts.save('temp.mp3')
    os.system('mpg321 temp.mp3')
    os.remove('temp.mp3')


def read_text_aloud(text_edit):
    text_content = text_edit.get(1.0, tk.END)
    if text_content.strip():
        read_aloud(text_content)


def main():
    window = tk.Tk()
    window.title('Text Editor')
    window.rowconfigure(0, weight=1)
    window.rowconfigure(0, weight=5)
    window.columnconfigure(1, weight=1)

    motivational_label = tk.Label(window, text=generate_random_motivation_sentence(), font='Helvetica 12 bold', fg='blue', wraplength=150,
                                  width=20, justify='center')
    motivational_label.grid(row=0, column=1, padx=10, pady=10)

    text_edit = tk.Text(window, font='Helvetica 18')
    text_edit.grid(row=1, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text='Save', command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text='Open', command=lambda: open_file(window, text_edit))
    read_aloud_button = tk.Button(frame, text='Read Aloud', command=lambda: read_text_aloud(text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
    read_aloud_button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
    frame.grid(row=0, column=0, sticky='ns')

    window.bind('<Control-s>', lambda x: save_file(window, text_edit))
    window.bind('<Control-o>', lambda x: open_file(window, text_edit))
    window.bind('<Control-r>', lambda x: read_text_aloud(text_edit))

    window.mainloop()


main()

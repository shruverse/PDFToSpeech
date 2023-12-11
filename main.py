from tkinter import Tk, filedialog, Button, Label
from PyPDF2 import PdfReader
from gtts import gTTS
import os

BG = '#000000'
FG = '#F0ECE5'
FONT = ('Arial', 20)
BTN_FONT = ('Arial', 12)


def select_file():
    file_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        process_pdf(file_path)


def process_pdf(file_path):
    pdf = PdfReader(file_path)

    text = ''
    for page in pdf.pages:
        text += page.extract_text()

    speech = gTTS(text, lang='en', tld='com.au')
    speech.save("output.mp3")
    play_button.grid(row=3, column=1, padx=20, pady=20)
    play_label.config(text='You can play your audio now')


def play_audio():
    os.system("start output.mp3")


# -------------UI------------
window = Tk()
window.title('PDF to Audio Converter')
window.minsize(width=500, height=400)
window.config(bg=BG, padx=50, pady=50)

empty_label = Label(text='', bg=BG, width=20)
empty_label.grid(row=0, column=0)

label = Label(text='Select Your PDF File', font=FONT, bg=BG, fg=FG)
label.grid(row=0, column=1, padx=20, pady=20)

empty_label_2 = Label(text='', bg=BG, width=20)
empty_label_2.grid(row=0, column=2)

select_button = Button(window, text="Select", command=select_file, bg=FG, borderwidth=0, highlightthickness=0, font=BTN_FONT)
select_button.grid(row=1, column=1, padx=20, pady=20)

play_label = Label(text='After selection please wait for conversion process...', fg=FG, bg=BG, font=BTN_FONT)
play_label.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

play_button = Button(window, text="Play", command=play_audio, bg=FG, borderwidth=0, highlightthickness=0, font=BTN_FONT)
window.mainloop()

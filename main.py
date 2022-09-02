from tkinter import *
import os.path
from tkinter import filedialog
import pytesseract
from PIL import Image
from tkinter import messagebox


window1 = Tk()
window1.geometry('560x450')
window1.title('Mahmoud [Extract Text from Image and video OCR]')
window1.resizable(False, False)
window1.configure(bg = 'white')
#----------Define--------------
def imo():
    file = filedialog.askopenfile(mode='r', filetypes = [('PNG Files', '*.png')])
    if file:
        filepath = os.path.abspath(file.name)
        En1.insert(0, filepath)
def ORC():
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    file = En1.get()
    savo = En2.get()
    language = En3.get()
    img = Image.open(file)
    txt = pytesseract.image_to_string(img)
    with open(savo, "w") as f:
        f.write(txt)
    messagebox.showinfo('Mahmoud', '\n The file saved')


#--------Tools---------------------

F1 = Frame(window1, width = 600, height = 368, bg = 'white', bd = 1, relief = SOLID)
F1.place(x = 1, y=1)

text = Label(F1, text = 'PROGRAM: [IMG 2 TXT]', font = ('times new roman', 13), fg= 'black', bg = 'white')
text.place(x=1, y=4)

En1_text = Label(F1, text= 'Image Path', fg = 'black', bg = 'white', font = ('times new roman', 11))
En1_text.place(x=10, y=51)
En1 = Entry(F1, font = ('times new roman', 16), width = 30, bd = 1, relief = SOLID)
En1.place(x=100, y=50)


btn1 = Button(F1, text = '+', cursor = 'hand2', command = imo)
btn1.place(x=445, y = 51)

En2_text = Label(F1, text= 'Save path', fg = 'black', bg = 'white', font = ('times new roman', 11))
En2_text.place(x=10, y=84)
En2 = Entry(F1, font = ('times new roman', 16), width = 30, bd = 1, relief = SOLID)
En2.place(x=100, y=84)


En3_text = Label(F1, text= 'Language', fg = 'black', bg = 'white', font = ('times new roman', 11))
En3_text.place(x=10, y=117)
En3 = Entry(F1, font = ('times new roman', 16), width = 30, bd = 1, relief = SOLID)
En3.place(x=100, y=117)



btn2 = Button(F1, text = 'Extract text', width = 10, height = 6, fg= 'white', bg = '#383838', cursor = 'hand2', command = ORC)
btn2.place(x= 470, y=49)


logo = PhotoImage(file = 'ocr.png')
logo_lbl = Label(window1, image = logo)
logo_lbl.place(x = 1, y=160)



#C:\Program Files (x86)\Tesseract-OCR

window1.mainloop()
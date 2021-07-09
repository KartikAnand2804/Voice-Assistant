import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("voice assistant")
buttonText = "Get Started."
HEIGHT = 500
WIDTH = 600
labeltext = "HELEN VOICE ASSISTANT"
creatorLabelText = "<Created by>\n KARTIK, MIHIR, HIMANI"



img = Image.open("mic.png")
img = img.resize((100,100), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)


def runningMsg():
	labelgreet = tk.Label(frame, text='voice assistant is running.', bg='black', fg='white', justify='center')
	labelgreet.pack()
	voiceassistant()

#background window
canvas = tk.Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='black')
frame.place(relwidth=1, relheight=1)

#introductory label
label = tk.Label(frame, text=labeltext, bg='black', fg='white')
label.config(font= ("Courier", 32))
label.pack()

#creator label
creLabel = tk.Label(frame, text= creatorLabelText, bg='black', fg='white', font='Times')
creLabel.config(font= ("Courier", 16))
creLabel.pack()

#action button
button = tk.Button(frame, text=buttonText, bg='white', image= photoImg,  activebackground='pink', highlightcolor='red', command=voiceassistant, compound='top')
button.config(font= ("Courier", 16))
button.pack()

# exit button
exit_button = tk.Button(frame, text="exit frame", bg='white', command=root.quit)
exit_button.pack()

#information from the user

root.mainloop()
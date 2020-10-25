from tkinter import *
import math

def leftClickButton(event):
    # print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    # labelResult.configure(text=float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2))
    Result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    texts = ""
    if Result < 18.5:
        texts = "ผอมเกินไป"
    elif Result > 18.5 and Result < 22.9:
        texts = "น้ำหนักปกติ เหมาะสม"
    elif Result > 23.0 and Result < 24.9:
        texts = "น้ำหนักเกิน"
    elif Result > 25 and Result < 29.9:
        texts = "อ้วน"
    elif Result > 30:
        texts = "อ้วนมาก"
    labelResult.configure(text=texts)

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (.cm)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (.kg)")
labelWeight.grid(row=2,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=2,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=3,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=3,column=1)
MainWindow.mainloop()


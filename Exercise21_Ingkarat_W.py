from tkinter import *
import math

def leftClickButton(event):
    Result = (float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    if Result >= 30:
        labelResult.configure(text="อ้วนมาก")
    elif Result >= 25:
        labelResult.configure(text = "อ้วน")
    elif Result >= 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif Result >= 18.6:
        labelResult.configure(text="น้ำหนักปกติ")
    else:
        labelResult.configure(text= "ผอมเกินไป")


MainWindow = Tk()
labelHight = Label(MainWindow,text = "ส่วนสูง(cm.)")
labelHight.grid(row=0, column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0, column=1)
labelWeight = Label(MainWindow,text = "น้ำหนัก(Kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text = "คำนวณ")
calculateButton.bind("<Button-1>", leftClickButton)
calculateButton.grid(row=2,column = 0)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()
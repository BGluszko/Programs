import tkinter.ttk as ttk
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from numpy import *
import sys
okno = Tk()
okno.geometry('1000x600')
okno.configure(background='light blue')
topFrame = Frame(okno)
topFrame.pack()
bottomFrame = Frame(okno)
bottomFrame.pack(side=BOTTOM)
okno.title("Program rysujący wykresy funkcji")
frame = Frame(okno, width=500, height=440,  bg='white')
frame.pack()
frame.place(x=400,y=100)
def plot():
    funkcje = entry1.get().split(';')
    zakres_X = entry2.get().split(',')
    zakres_Y = entry3.get().split(',')
    tytuł = entry4.get()
    etykieta_x = entry5.get()
    etykieta_y = entry6.get()
    x =  arange(float(zakres_X[0]), float(zakres_X[1]), 0.001)
    f = Figure(figsize=(5,4))
    ax = f.add_subplot(111)
    y = []
    for i in range(len(funkcje)):
        funkcje_s={"x":x,"sin":sin,"cos":cos,"exp":exp,"log":log}
        y.append(eval(funkcje[i], funkcje_s))
        ax.plot(x, y[i], label=funkcje[i])
    ax.set_xlabel(etykieta_x)
    ax.set_ylabel(etykieta_y)
    ax.set_title(tytuł)
    ax.set_xticks(range(round(float(zakres_X[0])),round(float(zakres_X[1])+1)))
    ax.set_yticks(range(round(float(zakres_Y[0])),round(float(zakres_Y[1])+1)))
    if decyzja.get() == True or len(funkcje)>1:
            ax.legend()
    canvas  = FigureCanvasTkAgg(f, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack(expand=True)
    canvas.get_tk_widget().pack()
def clear():
    for widget in frame.winfo_children():
        widget.destroy()
def quit():
    sys.exit()
def przycisk(p):
    entry1.insert(END, p)
przycisk1 = Button(okno, text = "Plot", command = plot)
przycisk1.pack(side=BOTTOM, expand=YES)
przycisk1.place(x=150,y=400)
przycisk2 = Button(bottomFrame, text = "Quit", command = quit)
przycisk2.pack(side=BOTTOM, expand=YES)
przycisk3= Button(okno, text = "Clear", command = clear)
przycisk3.pack()
przycisk3.place(x=160,y=480)
label1 = Label(okno, text='Wpisz wzór funkcji')
label1.pack()
label1.place(x=135, y=120)
entry1 = Entry(okno)
entry1.pack()
entry1.place(x=125, y=140)
label2 = Label(okno, text='ZakresX')
label2.pack()
label2.place(x=140, y=10)
entry2 = Entry(okno)
entry2.pack()
entry2.place(x=100,y=30)
label3 = Label(okno, text='Zakres Y')
label3.pack()
label3.place(x=290, y=10)
entry3 = Entry(okno)
entry3.pack()
entry3.place(x=250,y=30)
label4 = Label(okno, text='Title')
label4.pack()
label4.place(x=450, y=10)
entry4 = Entry(okno)
entry4.pack()
entry4.place(x=405,y=30)
label5 = Label(okno, text='Etykieta X')
label5.pack()
label5.place(x=590, y=10)
entry5 = Entry(okno)
entry5.pack()
entry5.place(x=555,y=30)
label6 = Label(okno, text='Etykieta Y')
label6.pack()
label6.place(x=700, y=10)
entry6 = Entry(okno)
entry6.pack()
entry6.place(x=705,y=30)
decyzja = BooleanVar()
decyzja.set(False)
check = Checkbutton(okno, text='legenda', var=decyzja)
check.pack()
check.place(x=850, y=30)
nawias_lewy = Button(okno, text=' ( ', command = lambda: przycisk('('))
nawias_lewy.pack()
nawias_lewy.place(x=140,y=180)
nawias_prawy = Button(okno, text=' ) ', command = lambda: przycisk(')'))
nawias_prawy.pack()
nawias_prawy.place(x=206,y=180)
plus = Button(okno, text=' + ', command = lambda: przycisk('+'))
plus.pack()
plus.place(x=140,y=206)
minus = Button(okno, text=' - ', command = lambda: przycisk('-'))
minus.pack()
minus.place(x=206,y=206)
mnożenie = Button(okno, text=' * ', command = lambda: przycisk('*'))
mnożenie.pack()
mnożenie.place(x=140,y=232)
dzielenie = Button(okno, text=' / ', command = lambda: przycisk('/'))
dzielenie.pack()
dzielenie.place(x=206,y=232)
pot = Button(okno, text=' ^ ', command = lambda: przycisk('**'))
pot.pack()
pot.place(x=140,y=258)
sinus = Button(okno, text=' sin ', command = lambda: przycisk('sin'))
sinus.pack()
sinus.place(x=140,y=284)
cosinus = Button(okno, text=' cos ', command = lambda: przycisk('cos'))
cosinus.pack()
cosinus.place(x=206,y=284)
logarytm = Button(okno, text='log', command = lambda: przycisk('log'))
logarytm.pack()
logarytm.place(x=206,y=258)
okno.mainloop()

__all__ = ["plot"]

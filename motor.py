from tkinter import Entry, Label, LabelFrame, Radiobutton, StringVar, Tk
from tkinter.constants import W

ventana=Tk()
ventana.geometry('300x300')
ventana.resizable(0,0)
ventana.title('Minicalc')

#Variables 
type_sys=StringVar(ventana,"1")
freq_sys=StringVar(ventana,"50")

#Elementos graficos
type_sys_lblframe=LabelFrame(ventana,text="Sistema")
monofasico=Radiobutton(type_sys_lblframe,text="Monofasico",variable=type_sys,value=1)
trifasico=Radiobutton(type_sys_lblframe,text="Trifasico     ",variable=type_sys,value=3)

freq_sys_lblframe=LabelFrame(ventana,text="Frecuencia")
f50=Radiobutton(freq_sys_lblframe,text="50 Hz",variable=freq_sys,value=50)
f60=Radiobutton(freq_sys_lblframe,text="60 Hz",variable=freq_sys,value=60)

potencia=Entry(ventana,width=6)
lblpot=Label(ventana,text="Potencia")
lblpotunit=Label(ventana,text="HP")

#render
type_sys_lblframe.grid(row=0,column=0)
monofasico.grid()
trifasico.grid()

freq_sys_lblframe.grid(row=1,column=0,sticky=W)
f50.grid()
f60.grid()

lblpot.grid(row=2,column=0,sticky=W)
potencia.grid(row=2,column=1,sticky=W)
lblpotunit.grid(row=2,column=3,sticky=W)

ventana.mainloop()
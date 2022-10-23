# By: Euronymou5
# ErnesSpam v2

from tkinter import *
import tkinter.font as tkFont
import pyautogui
import webbrowser
import time

root = Tk()

logo = PhotoImage(file = "icono.png")
root.iconphoto(False, logo)

def GButton_998_command():
    webbrowser.open_new_tab('http://web.whatsapp.com/')


def GButton_996_command():
    lol = cantidad.get()
    mss = lool.get()
    pyautogui.alert(text='Antes de mandar el spam debes de entrar al chat donde quieres mandar el spam.', title='Advertencia', button='OK')
    pyautogui.alert(text='Se abrira whatsapp web donde tendras que entrar a tu whatsapp escanenado el codigo qr', title='Advertencia', button='OK')
    a = pyautogui.confirm(text='¿Whatsapp esta abierto?', title='', buttons=['OK', 'Cancel'])
    if a == "OK":
        confirmar = pyautogui.confirm(text='Una vez ya estes dentro del chat presiona el boton Aceptar para empezar el spam.', title='ErnesSpam', buttons=['OK', 'Cancel'])
        if confirmar == "OK":
            pyautogui.alert(text='Comenzando el ataque en 5 segundos...', title='ErnesSpam', button='OK')
            time.sleep(5)
            for _ in range(lol):
                pyautogui.typewrite(mss)
                pyautogui.keyDown('enter')
        else:
            pyautogui.alert(text='Spam Cancelado.', title='', button='OK')
            pass
    else:
        pyautogui.alert(text='Debes de presionar el boton llamado "Abrir Whatsapp"', title='Advertencia', button='OK')
        pass

root.title("ErnesSpam v2")
width=416
height=439
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

GLabel_522=Label(root)
GLabel_522["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=12)
GLabel_522["font"] = ft
GLabel_522["fg"] = "#333333"
GLabel_522["justify"] = "center"
GLabel_522["text"] = ""
GLabel_522["relief"] = "flat"
GLabel_522.place(x=0,y=0,width=416,height=439)

GLabel_42=Label(root)
GLabel_42["bg"] = "#140c0c"
ft = tkFont.Font(family='Times',size=18)
GLabel_42["font"] = ft
GLabel_42["fg"] = "#ff0000"
GLabel_42["justify"] = "center"
GLabel_42["text"] = "ErnesSpam v2"
GLabel_42["relief"] = "flat"
GLabel_42.place(x=0,y=0,width=416,height=60)

lool = StringVar()
mensaje_entry=Entry(textvariable=lool)
mensaje_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
mensaje_entry["font"] = ft
mensaje_entry["fg"] = "#333333"
mensaje_entry["justify"] = "center"
mensaje_entry.place(x=100,y=100,width=197,height=42)

GLabel_134=Label(root)
ft = tkFont.Font(family='Times',size=12)
GLabel_134["font"] = ft
GLabel_134["fg"] = "#48ff05"
GLabel_134["bg"] = "#000000"
GLabel_134["justify"] = "center"
GLabel_134["text"] = "Mensaje:"
GLabel_134.place(x=120,y=70,width=152,height=31)

GLabel_471=Label(root)
ft = tkFont.Font(family='Times',size=12)
GLabel_471["font"] = ft
GLabel_471["bg"] = "#000000"
GLabel_471["fg"] = "#48ff05"
GLabel_471["justify"] = "center"
GLabel_471["text"] = "Cantidad:"
GLabel_471.place(x=130,y=150,width=146,height=30)

cantidad = IntVar()
cantidad.set('0')
cantidad_entry=Entry(textvariable=cantidad)
cantidad_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
cantidad_entry["font"] = ft
cantidad_entry["fg"] = "#333333"
cantidad_entry["justify"] = "center"
cantidad_entry.place(x=140,y=180,width=123,height=35)

GButton_998=Button(root)
GButton_998["bg"] = "#fffafa"
ft = tkFont.Font(family='Times',size=12)
GButton_998["font"] = ft
GButton_998["fg"] = "#000000"
GButton_998["justify"] = "center"
GButton_998["text"] = "Abrir Whatsapp"
GButton_998.place(x=20,y=340,width=130,height=35)
GButton_998["command"] = GButton_998_command

GButton_996=Button(root)
GButton_996["bg"] = "#2c2626"
GButton_996["disabledforeground"] = "#f9f9f9"
ft = tkFont.Font(family='Times',size=16)
GButton_996["font"] = ft
GButton_996["fg"] = "#ff0606"
GButton_996["justify"] = "center"
GButton_996["text"] = "Empezar spam"
GButton_996.place(x=90,y=240,width=218,height=46)
GButton_996["command"] = GButton_996_command

root.mainloop()

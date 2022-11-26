#enconding:utf-8
from pickle import NONE
import tkinter as tk
from tkinter import CENTER, END, PhotoImage, ttk
from turtle import bgcolor, width
import ConectionMqtt as t
from faker import Faker
from PIL import Image, ImageTk
import sqlite3 as sql

    
def insertCollection(Steps,Metros,color,Ip):
        conectar_bd =sql.connect("semaforoc.db")
        cursor = conectar_bd.cursor()
        instruction =f"INSERT INTO pasos_color_semaforo VALUES ('{Steps}','{Metros}','{color}','{Ip}')"
        cursor.execute(instruction)
        conectar_bd.commit()
        conectar_bd.close()

def ver_campos_amarillo():
    insertCollection("10","1","Amarillo",ip)
def ver_campos_verde():
     insertCollection("10","1","Verde", ip)     
def ver_campos_rojo():
     insertCollection("10","1","Rojo", ip)


ve = 1
pulsedBotton = 0
appmain = tk.Tk()
appmain.geometry("1005x605")
appmain.resizable(False, False)
appmain.title("IoT_Semaforo")
appmain.iconbitmap("img/semaforo.ico")
appmain.config(
    bg="gray99",
    relief="groove"

)
relojFrame = tk.Frame()
relojFrame.pack(side="bottom", anchor=tk.SE)
relojFrame.config(
    bg="gray89",
    width="500",
    height="200"

)
offFrame = tk.Frame()
offFrame.pack(side="right", anchor="n")
offFrame.config(
    bg="gray99",
    width="200",
    height="200"
)
rojoFrame = tk.Frame()
rojoFrame.pack(side="right", anchor=tk.N)
rojoFrame.config(
    bg="gray99",
    width="200",
    height="200"
)
verdeFrame = tk.Frame()
verdeFrame.pack(side="right", anchor=tk.N)
verdeFrame.config(
    bg="gray99",
    width="200",
    height="200"
)
amarilloFrame = tk.Frame()
amarilloFrame.pack(side="right", anchor=tk.N)
amarilloFrame.config(
    bg="gray99",
    width="200",
    height="200"
)
amarilloFrame.forget()
rojoFrame.forget()
verdeFrame.forget()
# offFrame.forget()
# relojFrame.forget()


img_off = tk.PhotoImage(file="img/off.gif")
img_amarillo = tk.PhotoImage(file="img/amarillo.gif")
img_verde = tk.PhotoImage(file="img/verde.gif")
img_rojo = tk.PhotoImage(file="img/rojo.gif")
img_cell = tk.PhotoImage(file="img/cell.png")

img_semaforo_label_amarilloframe = tk.Label(
    amarilloFrame,
    image=img_amarillo,
    width="100",
    height="150"
).place(x=10, y=10)

img_semaforo_label_rojoframe = tk.Label(
    rojoFrame,
    image=img_rojo,
    width="100",
    height="150"
).place(x=10, y=10)

img_semaforo_label_verdeframe = tk.Label(
    verdeFrame,
    image=img_verde,
    width="100",
    height="150"
).place(x=10, y=10)

img_semaforo_label_offframe = tk.Label(
    offFrame,
    image=img_off,
    width="100",
    height="150"
).place(x=10, y=10)

img_cell_label_appmain = tk.Label(
    appmain,
    image=img_cell,
    width="235",
    height="400"
).place(x=10, y=10)

img_txt_label_offframe = tk.Label(
    offFrame,
    text="*.....*",
    fg="black",
    bg="gray99",
    font=("Arial", 20)
).place(x=130, y=80)

img_txt_label_verdeframe = tk.Label(
    verdeFrame,
    text=" ¡GOO! ",
    fg="springGreen2",
    bg="gray99",
    font=("Arial", 20)
).place(x=100, y=80)

img_txt_label_rojoframe = tk.Label(
    rojoFrame,
    text=" ¡STOP! ",
    fg="red2",
    bg="gray99",
    font=("Arial", 20)
).place(x=100, y=80)

img_txt_label_amarilloframe = tk.Label(
    amarilloFrame,
    text=" ¡slow! ",
    fg="gold",
    bg="gray99",
    font=("Arial", 20)
).place(x=100, y=80)

reloj_label_txt_verde = tk.Label(
    relojFrame,
    text="00")
reloj_label_txt_verde.grid(row=0, column=0, pady=5, padx=5)


def fuctioExecute():
    global d
    d = 0
    global pulsedBotton
    pulsedBotton = 1
    refresh_color()


def cambio():
    global ip
    global ve
    global i
    global pulsedBotton
    ex = Faker()
    ip = ex.ipv4()
    if ve == 1:
        verdeFrame.pack(side="right", anchor=tk.N)
        amarilloFrame.forget()
        rojoFrame.forget()
        offFrame.forget()
        ve = 2
        ver_campos_verde()
        t.run("Verde", ip)
        return("springGreen2")

    elif ve == 2:

        amarilloFrame.pack(side="right", anchor=tk.N)
        verdeFrame.forget()
        rojoFrame.forget()
        offFrame.forget()
        ve = 3
        #sql3.insertCollection("10","1","Amarrillo", ip)
        ver_campos_amarillo()
        t.run("Amarrillo", ip)
        return("orange")
    elif ve == 3:
        rojoFrame.pack(side="right", anchor=tk.N)
        amarilloFrame.forget()
        verdeFrame.forget()
        offFrame.forget()
        ve = 1
        #sql3.insertCollection("10","1","Rojo", ip)
        ver_campos_rojo()
        t.run("Rojo", ip)
        return("red2")


img = Image.open('./img/pushBotton.jpeg')
img = img.resize((110, 90))
img = ImageTk.PhotoImage(img)
btn_cambio_appmain = tk.Button(
    appmain,
    image=img,
    font=("Arial 12 bold"),
    fg="dark violet",
    bg="snow",
    cursor="hand2",
    command=fuctioExecute
).place(x=75, y=170)

# Codigoo
style = ttk.Style(appmain)
style.theme_use("clam")
style.configure("Treeview.Heading", background="black", foreground="white")


def table():
    global tabla
    tabla = ttk.Treeview(appmain, columns=('Metros', 'Color', 'Ip'))
    tabla.column("#0", width=80)
    tabla.column('Metros', width=60)
    tabla.column('Color', width=60)
    tabla.column('Ip', width=120)

    tabla.heading("#0", text="Pasos", anchor=CENTER)
    tabla.heading('Metros', text='Metros', anchor=CENTER)
    tabla.heading('Color', text='Color', anchor=CENTER)
    tabla.heading('Ip', text='Ip', anchor=CENTER)
    
    conectar_bd =sql.connect("semaforoc.db")
    cursor = conectar_bd.cursor()

    registros = tabla.get_children()
    for elementos in registros:
        tabla.delete(elementos)
    instruction =f"SELECT * FROM pasos_color_semaforo"
    cursor.execute(instruction)
    for row in cursor:
        tabla.insert("",0, text=row[0], values=(
            row[1], row[2], row[3]))
    conectar_bd.commit()
    conectar_bd.close()
    tabla.place(x=340, y=100)


after_id = None


def refresh_color():
    global d
    global pulsedBotton
    global after_id
    color = None
    d += 1
    if(pulsedBotton > 0):
        color = cambio()
        if(after_id != None):
            appmain.after_cancel(after_id)
        pulsedBotton = 0
        d = 0
        table()
    if(d == 10):
        color = cambio()
        pulsedBotton = 0
        d = 0
        table()
    reloj_label_txt_verde.config(
        fg=color, font=("Arial", 40), bg="black", width="15",
        height="2", text=f"0{d} s")
    after_id = appmain.after(1000, refresh_color)
    pulsedBotton = 0


table()

appmain.mainloop()

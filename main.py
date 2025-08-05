import sqlite3
from tkinter import *
from tkinter import messagebox


conn = sqlite3.connect("proyecto.inf.soficami")
cursor = conn.cursor()

def guardar_en_bd(valor):
    cursor.execute("INSERT INTO resultado (resultado) VALUES (?)", (valor,))
    conn.commit()

def mostrar_registros():
    cursor.execute("SELECT * FROM resultado")
    registros = cursor.fetchall()
    texto = " ".join([f"ID: {r[0]}, Resultado: {r[1]}" for r in registros])
    messagebox.showinfo("Registros", texto if texto else "No hay registros")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS resultado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resultado REAL
    )
''')
conn.commit()


ventana = Tk()
ventana.title("ejercicio")
ventana.geometry("400x400")
ventana.config(bd=24)

numero1 = StringVar()
numero2 = StringVar()
numero3 = StringVar()
resultado = StringVar()
numero1.set("")
numero2.set("")
numero3.set("")

def sumar():
    try:
        r = float(numero1.get()) + float(numero2.get()) + float(numero3.get())
        resultado.set(str(r))
        guardar_en_bd(r)
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
        numero1.set("")
        numero2.set("")
        numero3.set("")

def restar():
    try:
        r = float(numero1.get()) - float(numero2.get()) - float(numero3.get())
        resultado.set(str(r))
        guardar_en_bd(r)
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
        numero1.set("")
        numero2.set("")
        numero3.set("")

def multiplicar():
    try:
        r = float(numero1.get()) * float(numero2.get()) * float(numero3.get())
        resultado.set(str(r))
        guardar_en_bd(r)
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
        numero1.set("")
        numero2.set("")
        numero3.set("")

def dividir():
    try:
        r = float(numero1.get()) / float(numero2.get()) / float(numero3.get())
        resultado.set(str(r))
        guardar_en_bd(r)
    except:
        messagebox.showerror("Error", "Introduce bien los datos (no dividir por cero)")
        numero1.set("")
        numero2.set("")
        numero3.set("")

marco = Frame(ventana, width=250, height=200)
marco.config(padx=15, pady=15)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número:").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo número:").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="Tercer número:").pack()
Entry(marco, textvariable=numero3, justify="center").pack()

Label(marco, text="Resultado:").pack()
Entry(marco, textvariable=resultado, justify="center", state="readonly").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Ver registros", command=mostrar_registros).pack(side="left", fill=X, expand=YES)


ventana.mainloop()

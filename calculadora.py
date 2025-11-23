import tkinter as tk

# --- Configuración de la ventana principal ---
root = tk.Tk()
root.title("Calculadora")
root.geometry("350x500")
root.config(bg="#2c3e50")

# --- Pantalla de entrada ---
entrada = tk.Entry(root, font=("Arial", 20), border=5, relief="ridge", justify="right", bg="#ecf0f1")
entrada.pack(fill="both", padx=10, pady=20)

# --- Funciones de la calculadora ---
def click_boton(valor):
    entrada.insert(tk.END, valor)

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# --- Estilo de botones ---
boton_estilo = {
    "font": ("Arial", 18),
    "width": 4,
    "height": 2,
    "bg": "#34495e",
    "fg": "white",
    "activebackground": "#1abc9c",
    "activeforeground": "black",
    "relief": "ridge",
    "border": 2
}

# --- Frame para botones ---
frame = tk.Frame(root, bg="#2c3e50")
frame.pack()

# --- Layout de botones ---
botones = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for (texto, fila, columna) in botones:
    if texto == "=":
        b = tk.Button(frame, text=texto, command=calcular, **boton_estilo)
    else:
        b = tk.Button(frame, text=texto, command=lambda t=texto: click_boton(t), **boton_estilo)
    b.grid(row=fila, column=columna, padx=5, pady=5)

# --- Botón de borrar ---
btn_clear = tk.Button(root, text="C", command=borrar, font=("Arial", 18), bg="#e74c3c", fg="white", width=10, height=2)
btn_clear.pack(pady=10)

# --- Ejecutar la app ---
root.mainloop()
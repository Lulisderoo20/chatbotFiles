import tkinter as tk
import subprocess

def ejecutar_script():
    ruta_script = entrada_texto.get()
    subprocess.run(['python', ruta_script])

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ejecutar Script")

# Crear widgets
etiqueta = tk.Label(ventana, text="Ruta del script:")
entrada_texto = tk.Entry(ventana)
boton_ok = tk.Button(ventana, text="OK", command=ejecutar_script)

# Colocar widgets en la ventana
etiqueta.pack()
entrada_texto.pack()
boton_ok.pack()

# Iniciar el bucle de eventos
ventana.mainloop()

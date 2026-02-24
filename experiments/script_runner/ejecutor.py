import subprocess
import sys
from pathlib import Path
import tkinter as tk
from tkinter import messagebox


def ejecutar_script() -> None:
    ruta_script = Path(entrada_texto.get().strip())

    if not ruta_script.exists():
        messagebox.showerror("Error", f"File not found: {ruta_script}")
        return

    if ruta_script.suffix.lower() != ".py":
        messagebox.showerror("Error", "Only .py files are supported")
        return

    try:
        subprocess.run([sys.executable, str(ruta_script)], check=False)
        messagebox.showinfo("Done", "Script executed")
    except OSError as exc:
        messagebox.showerror("Error", f"Could not execute script: {exc}")


ventana = tk.Tk()
ventana.title("Python Script Runner")

etiqueta = tk.Label(ventana, text="Script path:")
entrada_texto = tk.Entry(ventana, width=70)
boton_ok = tk.Button(ventana, text="Run", command=ejecutar_script)

etiqueta.pack(padx=8, pady=(10, 4))
entrada_texto.pack(padx=8, pady=4)
boton_ok.pack(padx=8, pady=(4, 10))

ventana.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog

def procesar_numeros(numeros):
    try:
        lista_numeros = list(map(int, numeros.split(',')))
        lista_numeros.sort()  # Ordenar la lista de números
        cadena_numeros = ",".join(map(str, lista_numeros))
        return cadena_numeros  # Retornar la cadena de números
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese solo números enteros positivos separados por comas.")
        return None

def mostrar_resultados(final_result, results):
    ventana_resultados = tk.Tk()
    ventana_resultados.withdraw()  # Ocultar la ventana principal

    messagebox.showinfo("Resultados", f"Final Result: {final_result}\nResults: {results}")

    ventana_resultados.destroy()

def obtener_entrada_usuario():
    ventana = tk.Tk()
    ventana.withdraw()  # Ocultar la ventana principal

    numeros = simpledialog.askstring("Ingreso de Números", "Ingrese los números separados por comas:")

    ventana.destroy()
    return numeros

if __name__ == "__main__":
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ingreso de Números")

    # Crear el campo de entrada
    entrada = tk.Entry(ventana, width=50)
    entrada.pack(pady=10)

    # Crear el botón "Confirmar"
    boton_confirmar = tk.Button(ventana, text="Confirmar", command=ventana.quit)
    boton_confirmar.pack(pady=5)

    # Crear el botón "Limpiar"
    boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_entrada)
    boton_limpiar.pack(pady=5)

    # Crear la etiqueta para mostrar el resultado
    etiqueta_resultado = tk.Label(ventana, text="")
    etiqueta_resultado.pack(pady=10)

    # Ejecutar el bucle principal de la aplicación
    ventana.mainloop()
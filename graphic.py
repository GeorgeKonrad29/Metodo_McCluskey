import tkinter as tk
from tkinter import Label,Text,messagebox, simpledialog

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
    # Asegúrate de que results sea una lista de cadenas
    if isinstance(results, str):
        results = results.split()  # Divide la cadena en una lista de palabras
    elif not isinstance(results, list):
        results = [str(results)]  # Convierte a lista si no lo es

    # Une los elementos de la lista con '+'
    results_str = ' + '.join(results)

    ventana_resultados = tk.Tk()
    ventana_resultados.title("Resultados")
    ventana_resultados.geometry("600x400")  # Configurar el tamaño de la ventana

    frame = tk.Frame(ventana_resultados)
    frame.pack(expand=True, fill='both', padx=10, pady=10)

    label_title = Label(frame, text="Resultados", font=("Helvetica", 16, "bold"))
    label_title.pack(pady=10)

    label_final_result = Label(frame, text=f"Final Result: {final_result}", font=("Helvetica", 12))
    label_final_result.pack(pady=5)

    text_widget = Text(frame, wrap='word', height=15)
    text_widget.pack(expand=True, fill='both', pady=10)
    text_widget.insert('1.0', results_str)
    text_widget.config(state='disabled')  # Hacer que el Text widget sea de solo lectura

    ventana_resultados.mainloop()
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
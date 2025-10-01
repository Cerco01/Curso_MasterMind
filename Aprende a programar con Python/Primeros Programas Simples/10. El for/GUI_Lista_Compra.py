import customtkinter as ctk
from tkinter import messagebox, END
import json
import os

# --- CONFIGURACIÓN DE DATOS ---
CARPETA_DATOS = "datos_app"
NOMBRE_ARCHIVO = os.path.join(CARPETA_DATOS, "lista_compra.json")

# --- VARIABLES GLOBALES DE LA APP ---
# Usaremos una lista simple de Python para mantener los datos.
lista_productos_modelo = []

# 1. CONFIGURACIÓN INICIAL
# ----------------------------------------------------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Mi Lista de la Compra 🛒")


# 2. FUNCIONES DE PERSISTENCIA Y UTILIDAD
# ----------------------------------------------------------------------

def cargar_lista():
    """Carga los productos del archivo JSON al modelo y dibuja la lista."""
    global lista_productos_modelo
    if not os.path.exists(NOMBRE_ARCHIVO):
        return

    try:
        with open(NOMBRE_ARCHIVO, 'r') as archivo:
            # Carga los productos directamente a nuestra lista de modelo
            lista_productos_modelo = json.load(archivo)

            # Llama a dibujar la lista después de cargar los datos
            dibujar_lista()

    except json.JSONDecodeError:
        messagebox.showwarning("Error de carga", "El archivo de datos está vacío o dañado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al cargar la lista: {e}")


def guardar_lista():
    """Guarda la lista del modelo en el archivo JSON."""
    os.makedirs(CARPETA_DATOS, exist_ok=True)

    try:
        with open(NOMBRE_ARCHIVO, 'w') as archivo:
            # Guarda la lista de modelo, NO la interfaz gráfica
            json.dump(lista_productos_modelo, archivo, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la lista: {e}")


def cerrar_aplicacion():
    """Guarda la lista antes de cerrar la ventana y la destruye."""
    guardar_lista()
    ventana.destroy()


# 3. LÓGICA DE DIBUJO Y MANEJO DE WIDGETS (¡CLAVE!)
# ----------------------------------------------------------------------

def remover_item_por_clic(nombre_producto):
    """Función que se llama al hacer clic en 'Retirar Seleccionado'."""
    global lista_productos_modelo

    if messagebox.askyesno("Confirmar Eliminación", f"¿Seguro que quieres retirar {nombre_producto}?"):
        # 1. Elimina el producto del MODELO de datos
        lista_productos_modelo.remove(nombre_producto)

        # 2. Redibuja toda la interfaz (la forma más simple de actualizar el scrollable frame)
        dibujar_lista()

        messagebox.showinfo("Éxito", f"'{nombre_producto}' retirado de la lista.")


def dibujar_lista():
    """Vací a el frame de la lista y lo redibuja completamente con los datos del modelo."""

    # 1. Elimina los widgets existentes en el frame_lista
    for widget in frame_lista.winfo_children():
        widget.destroy()

    # 2. Si la lista está vacía, muestra un mensaje
    if not lista_productos_modelo:
        ctk.CTkLabel(frame_lista, text="La lista de la compra está vacía.").pack(pady=20)
        return

    # 3. Itera sobre el modelo y crea una etiqueta por cada producto
    for i, producto in enumerate(lista_productos_modelo):
        # Creamos una etiqueta por producto con un color de fondo para distinguirlo
        item_frame = ctk.CTkFrame(frame_lista, fg_color="transparent")
        item_frame.pack(fill="x", pady=2, padx=5)

        # Etiqueta con el nombre del producto
        label_producto = ctk.CTkLabel(item_frame, text=producto, font=ctk.CTkFont(size=14), anchor="w")
        label_producto.pack(side="left", fill="x", expand=True, padx=(0, 10))

        # Botón para retirar que llama a la función de remover con el nombre del producto
        boton_retirar_item = ctk.CTkButton(
            item_frame,
            text="❌",
            width=30,
            height=20,
            fg_color="#A00000",
            hover_color="#C00000",
            command=lambda p=producto: remover_item_por_clic(p)  # Usamos lambda para pasar el argumento
        )
        boton_retirar_item.pack(side="right")


# 4. FUNCIONES DE INTERACCIÓN (Simples y limpias)
# ----------------------------------------------------------------------

def agregar_producto():
    global lista_productos_modelo
    producto = entrada_producto.get().strip()

    if not producto:
        messagebox.showwarning("Aviso", "No has escrito nada.")
        return

    if producto in lista_productos_modelo:  # Comprobación contra el modelo
        messagebox.showinfo("Error", f"'{producto}' ya está en la lista.")

    else:
        if messagebox.askyesno("Confirmar", f"¿Seguro que quieres añadir {producto}?"):
            # 1. Añade al MODELO
            lista_productos_modelo.append(producto)

            # 2. DIBUJA la interfaz
            dibujar_lista()

            entrada_producto.delete(0, END)


# La función retirar_producto original ya no es necesaria; su lógica está en remover_item_por_clic


# 5. INTERFAZ GRÁFICA (Widgets)
# ----------------------------------------------------------------------

# 5.1. CTkScrollableFrame para mostrar los elementos (Reemplazo del Listbox)
frame_lista = ctk.CTkScrollableFrame(ventana, label_text="Productos de la Compra", width=350, height=250)
frame_lista.pack(pady=10, padx=20, fill="x")  # Ya no necesitamos expand=True

# 5.2. FRAME para los controles (Entrada y Botones)
frame_controles = ctk.CTkFrame(ventana)
frame_controles.pack(pady=10, padx=20, fill="x")

# Campo de Entrada (Entry)
entrada_producto = ctk.CTkEntry(frame_controles, width=200, placeholder_text="Escribe aquí tu producto...")
entrada_producto.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Botón de Añadir
boton_agregar = ctk.CTkButton(frame_controles, text="Añadir", command=agregar_producto)
boton_agregar.grid(row=0, column=1, padx=5, pady=5)

# Nota: El botón 'Retirar Seleccionado' ya no es necesario, lo hemos integrado en cada ítem.
# Si quieres mantener el botón de abajo, su lógica debe cambiar.


# 6. INICIALIZACIÓN Y EJECUCIÓN
# ----------------------------------------------------------------------

# Vincula la tecla Enter (Return)
entrada_producto.bind('<Return>', lambda event=None: agregar_producto())

# 1. Cargar la lista al iniciar la aplicación
cargar_lista()

# 2. Configurar el guardado automático al cerrar la ventana
ventana.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

# 3. Iniciar el bucle principal
ventana.mainloop()
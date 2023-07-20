import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import *
import os

def download_and_convert():
    # Obtener la URL del video ingresada por el usuario
    url = url_entry.get()

    try:
        # Crear objeto YouTube
        youtube = YouTube(url)

        # Descargar el video en la mejor resolución disponible
        video = youtube.streams.get_highest_resolution()
        video_filename = video.default_filename
        video_folder = "videos"
        video_path = os.path.join(video_folder, video_filename)
        video.download(output_path=video_folder)

        messagebox.showinfo("Descarga completada", "Video descargado con éxito.")

        # Generar el nombre para el archivo MP3 basado en el nombre del video
        mp3_filename = os.path.splitext(video.default_filename)[0] + ".mp3"
        mp3_folder = "audios"
        mp3_path = os.path.join(mp3_folder, mp3_filename)
        output_path = mp3_path

        # Cargar el video usando MoviePy
        video_clip = VideoFileClip(video_path)

        # Extraer el audio del video
        audio = video_clip.audio

        # Guardar el audio como archivo MP3
        audio.write_audiofile(output_path)

        messagebox.showinfo("Conversión completada", "Archivo MP3 creado con éxito.")

        # Eliminar el archivo de video descargado
        os.remove(video_path)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana de la aplicación
window = tk.Tk()
window.title("Descarga y Conversión de YouTube")
window.geometry("400x200")

# Etiqueta y campo de entrada para la URL del video
url_label = tk.Label(window, text="Ingrese la URL del video de YouTube:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Botón para iniciar la descarga y conversión
download_button = tk.Button(window, text="Descargar y Convertir", command=download_and_convert)
download_button.pack()

# Ejecutar la aplicación
window.mainloop()

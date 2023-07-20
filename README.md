# ConverteYoutubetoMp3
Este código es una pequeña aplicación de descarga y conversión de videos de YouTube a archivos de audio MP3. Explicaré brevemente cómo funciona:

1. Se importan los módulos necesarios:
   - `tkinter`: Proporciona las herramientas para crear la interfaz gráfica de la aplicación.
   - `messagebox`: Permite mostrar mensajes emergentes para notificar sobre eventos o errores.
   - `pytube`: Un módulo para descargar videos de YouTube.
   - `moviepy.editor`: Proporciona funcionalidades para editar y convertir videos.

2. Se define una función llamada `download_and_convert()` que se ejecutará cuando el botón "Descargar y Convertir" sea presionado.
   - Obtiene la URL del video ingresada por el usuario desde el campo de entrada `url_entry`.
   - Utiliza la biblioteca `pytube` para descargar el video de YouTube en la mejor resolución disponible.
   - Muestra un mensaje emergente si la descarga es exitosa.
   - Utiliza la biblioteca `moviepy.editor` para extraer el audio del video descargado y guardarlo como un archivo MP3 en la carpeta "audios".
   - Muestra otro mensaje emergente si la conversión es exitosa.
   - Finalmente, elimina el archivo de video descargado para ahorrar espacio en el sistema.

3. Se crea la ventana de la aplicación usando `tkinter`:
   - Se crea una ventana con un título y un tamaño específico (400x200).
   - Se agrega una etiqueta y un campo de entrada para que el usuario ingrese la URL del video de YouTube.
   - Se agrega un botón con el texto "Descargar y Convertir" que llamará a la función `download_and_convert()` cuando sea presionado.

4. La aplicación se ejecuta mediante el método `window.mainloop()`, lo que inicia el bucle principal de la interfaz gráfica y espera a que el usuario interactúe con la ventana.

Cuando el usuario ingrese la URL del video de YouTube y haga clic en el botón "Descargar y Convertir", la función `download_and_convert()` se ejecutará y realizará la descarga y conversión del video. Si hay algún error en el proceso, se mostrará una ventana emergente con el mensaje de error.

from pytube import YouTube  # Importa la clase YouTube desde el módulo pytube

try:
    # Solicita al usuario que ingrese el enlace del video
    video_link = input('Ingrese el enlace del video: \n')

    # Crea un objeto YouTube con el enlace proporcionado
    yt = YouTube(video_link)

    # Muestra información básica del video
    print("Titulo: ", yt.title)  # Muestra el título del video
    print("Autor: ", yt.author)  # Muestra el autor del video

    # Calcula la duración del video en minutos y segundos
    duration_seconds = int(yt.length)
    minutes, seconds = divmod(duration_seconds, 60)
    print("Duracion: ", "{}:{}".format(minutes, seconds), "\n")  # Muestra la duración del video en formato MM:SS

    # Filtra las opciones de transmisión disponibles para videos progresivos en formato mp4 y las ordena por resolución de forma descendente
    available_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    # Muestra las opciones de calidad disponibles para el usuario
    print("Opciones de calidad disponibles:")
    for i, stream in enumerate(available_streams):
        print(f"{i + 1}. {stream.resolution} - {stream.mime_type} - {stream.filesize / (1024*1024):.2f} MB")

    # Solicita al usuario que seleccione la calidad deseada
    choice = int(input("Seleccione el numero correspondiente a la calidad deseada: "))
    if 1<= choice <= len(available_streams):  # Verifica si la opción seleccionada es válida
        select_stream = available_streams[choice-1]  # Obtiene la transmisión seleccionada
        select_stream.download()  # Descarga el video con la calidad seleccionada
        print("Descarga completa.")  # Indica que la descarga se completó con éxito
    else:
        print("Selección de calidad inválida")  # Indica que la opción seleccionada no es válida
except Exception as e:
    print('Ocurrio un error:', e)  # Muestra un mensaje de error en caso de que ocurra una excepción durante la ejecución del código

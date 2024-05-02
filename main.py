from pytube import YouTube

try:
    yt = input('Ingrese el link del video: ')
    print('\n')
    yt = YouTube(yt)
    print("Titulo: ", yt.title)
    print("Autor: ", yt.author)
    print('\n')
    length_video = int(yt.length)
    min, sec = divmod(length_video, 60)
    print("Duracion: ", "{}:{}".format(min, sec))
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("Descarga finalizada.")
except:
    print('Error')
    exit()
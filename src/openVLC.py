import subprocess
from randomizadorPlaylist import playListRandomizada
from buscarPlaylist import playlist

def openVLC ():
    rutaVLC = input('Coloca la ruta del VLC= ')
    vlc=[rutaVLC] + playListRandomizada(playlist())
    subprocess.Popen(vlc)
    
openVLC ()
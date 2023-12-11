import subprocess
from randomizadorPlaylist import playListRandomizada
from buscarPlaylist import playlist
import os

def openVLC ():
    try:
        assert os.path.exists('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe')
        rutaVLC = os.path.exists('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe')
        if rutaVLC:
            vlc=['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'] + playListRandomizada(playlist())
            subprocess.Popen(vlc)
            ejecucuion = True
        else:
            ejecucuion = False
        assert ejecucuion
    except AssertionError:
        print('No se encuentra el VLC')
    
openVLC ()
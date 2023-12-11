import subprocess
from randomizadorPlaylist import playListRandomizada
from buscarPlaylist import playlist
import os

def openVLC ():
    if os.path.exists('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'):
        vlc=['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'] + playListRandomizada(playlist())
        subprocess.Popen(vlc)
        return True
    else:
        print('No se encuentra la ruta del VLC')
    return False
    
openVLC ()
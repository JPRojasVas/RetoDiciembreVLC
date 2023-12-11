import subprocess
from randomizadorPlaylist import playListRandomizada
from buscarPlaylist import playlist

def openVLC ():
    vlc=["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe"] + playListRandomizada(playlist())
    subprocess.Popen(vlc)
    
openVLC ()
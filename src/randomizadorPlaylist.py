import random
from buscarPlaylist import playlist

def playListRandomizada(urlRandom):
    random.shuffle(urlRandom)
    return urlRandom

print(playListRandomizada(playlist()))
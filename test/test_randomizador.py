from ..src.randomizadorPlaylist import playListRandomizada

def test_longitudPlaylist():
    lista_original = ["cancion1.mp3", "cancion2.mp3", "cancion3.mp3"]
    lista_copia = lista_original.copy()
    lista_randomizada = playListRandomizada(lista_original)
    assert len(lista_randomizada) == len(lista_copia), "Error: Longitud de la lista después de randomizar no es la misma"

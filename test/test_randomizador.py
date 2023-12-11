from src.randomizadorPlaylist import playListRandomizada

def test_longitudPlaylist():
    lista_original = ["cancion1.mp3", "cancion2.mp3", "cancion3.mp3"]
    lista_copia = lista_original.copy()
    lista_randomizada = playListRandomizada(lista_original)
    assert len(lista_randomizada) == len(lista_copia), "Error: Longitud de la lista después de randomizar no es la misma"

def test_playListRandomizada():
    lista_original = ["cancion1.mp3", "cancion2.mp3", "cancion3.mp3"]
    lista_copia = lista_original.copy()
    lista_randomizada = playListRandomizada(lista_original)
    assert set(lista_randomizada) == set(lista_copia), "Error: Elementos en la lista después de randomizar son diferentes"

def test_ListasNoSonIguales():
    lista_original = ["cancion1.mp3", "cancion2.mp3", "cancion3.mp3", "cancion4.mp3", "cancion5.mp3", "cancion6.mp3", "cancion7.mp3"]
    lista_copia = lista_original.copy()
    lista_randomizada = playListRandomizada(lista_original)
    assert lista_randomizada != lista_copia, "Error: La lista no se ha randomizado"

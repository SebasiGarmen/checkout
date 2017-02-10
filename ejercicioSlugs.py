# -*- coding: utf-8 -*-


def palabrasSlugs(palabra):
    palabra = palabra.lower()
    correcciones = {
        " ": "_",
        "á": "a",
        "Á": "a",
        "é": "e",
        "É": "e",
        "í": "i",
        "Í": "i",
        "ó": "o",
        "Ó": "o",
        "ú": "u",
        "Ú": "u",
        "ñ": "n",
        "Ñ": "n",
    }
    for mal, bien in correcciones.iteritems():
        palabra = palabra.replace(mal, bien)
    return palabra

print palabrasSlugs("hOlá niño ¿Cómo estÁs?")

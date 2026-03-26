from txtanim import typewriter
from colorama import Fore, Style, init
import random
from exceptions.paranoiaerror import ParanoiaError
from entidades.paranoia import Paranoia

class Paranoia:
    def __init__(self, prompt: str):
        self.prompt = prompt

    def responder(self) -> str:
        palabras_prohibidas = {"tonta", "matar", "suicidar", "idiota", "golpear"}

        respuestas = [
            "Who knows?",
            "No",
            "yo solo sé que no sé nada",
            "puede que sí, puede que no, pero lo más seguro es que quién sabe xD",
            "simón, al rato..."
        ]

        for palabra in palabras_prohibidas:
            if palabra in self.prompt:
                raise ParanoiaError()

        return random.choice(respuestas)
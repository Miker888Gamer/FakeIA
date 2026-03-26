import colorama
import random 
from entidades.paranoia import Paranoia
from exceptions.paranoiaerror import ParanoiaError
from colorama import Fore, Style, init


init(autoreset=True)

try:
    print("Bienvenido a la aplicación de Paranoia")
    input("Presiona Enter para continuar..." )
    prompt = str(input())
    init(autoreset=True)
    texto = Fore.RED + "Hola, soy una IA medio despistada 😵"
    
    
    if prompt == "tonta":
        print("no sea grosero")
    elif prompt == "no entiendo":
        print("no entiendo lo que quieres decir")
    elif prompt == "tonto":
        print("tontas")
    elif prompt == "tontos":
        print("no se que es eso")
    elif prompt == "tontas":
        print("no se que es eso")
    else:
        raise ParanoiaError("No se reconoce el prompt ingresado")
except ParanoiaError as e:
    print(f"Error: {e}")
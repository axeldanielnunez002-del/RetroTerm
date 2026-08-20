import os
import sys
from datetime import datetime

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    print("========================================")
    print("        PIXELTERM v1.0 (Simple)         ")
    print("========================================")
    print("Escribe 'help' para ver los comandos.\n")

def main():
    limpiar_pantalla()
    mostrar_banner()
    
    while True:
        try:
            # Entrada de comandos sencilla
            comando = input("PIXELTERM> ").strip().lower()
            
            if comando == "":
                continue
            elif comando == "exit":
                print("Cerrando PIXELTERM...")
                break
            elif comando == "help":
                print("\n--- Comandos Disponibles ---")
                print("  help   - Muestra este menú")
                print("  clear  - Limpia la pantalla")
                print("  hora   - Muestra la hora y fecha actual")
                print("  info   - Información del proyecto")
                print("  exit   - Salir de la terminal\n")
            elif comando == "clear":
                limpiar_pantalla()
                mostrar_banner()
            elif comando == "hora":
                ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Fecha y Hora: {ahora}")
            elif comando == "info":
                print("PIXELTERM - Proyecto de terminal personalizada en Python.")
            else:
                print(f"Comando no reconocido: '{comando}'. Usa 'help'.")
                
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo...")
            sys.exit()

if __name__ == "__main__":
    main()
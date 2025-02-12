import os
import random
import uuid
import ctypes
from colorama import Fore, Style, init

init()

# Fonction pour générer des informations aléatoires
def generate_spoofed_info():
    return {
        "Carte_mere": str(uuid.uuid4()),
        "Processeur": str(random.randint(1000000000, 9999999999)),
        "Disque_dur": str(random.randint(1000000000, 9999999999)),
        "Module_TPM": str(random.randint(1000000000, 9999999999)),
        "Adresse_MAC": get_random_mac(),
        "Nom_PC": f"PC-{random.randint(1000, 9999)}"
    }

# Fonction pour obtenir une adresse MAC aléatoire
def get_random_mac():
    return ":".join([f"{random.randint(0x00, 0xFF):02x}" for _ in range(6)])

# Fonction pour vérifier si l'utilisateur est administrateur
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Fonction pour changer l'adresse MAC
def change_mac_address(interface):
    if not is_admin():
        print(Fore.RED + "Ce script doit être exécuté en mode administrateur !" + Style.RESET_ALL)
        return
    spoofed_info = generate_spoofed_info()  # Génération aléatoire à chaque appel
    new_mac = spoofed_info["Adresse_MAC"].replace(":", "")
    print(Fore.YELLOW + f"Nouvelle adresse MAC : {new_mac}" + Style.RESET_ALL)
    os.system(f'netsh interface set interface "{interface}" admin=disable')
    os.system(f'netsh interface set interface "{interface}" admin=enable')
    print(Fore.GREEN + "Adresse MAC modifiée avec succès !" + Style.RESET_ALL)

# Fonction pour changer le nom du PC
def change_computer_name():
    if not is_admin():
        print(Fore.RED + "Ce script doit être exécuté en mode administrateur !" + Style.RESET_ALL)
        return
    spoofed_info = generate_spoofed_info()  # Génération aléatoire à chaque appel
    new_name = spoofed_info["Nom_PC"]
    os.system(f'wmic computersystem where name="%COMPUTERNAME%" call rename name="{new_name}"')
    print(Fore.GREEN + f"Nouveau nom du PC : {new_name}" + Style.RESET_ALL)

# Fonction pour changer les numéros de série des composants
def change_serial_numbers():
    if not is_admin():
        print(Fore.RED + "Ce script doit être exécuté en mode administrateur !" + Style.RESET_ALL)
        return
    spoofed_info = generate_spoofed_info()  # Génération aléatoire à chaque appel
    print(Fore.YELLOW + "Modification des numéros de série..." + Style.RESET_ALL)
    print(Fore.GREEN + f"Carte mère: {spoofed_info['Carte_mere']}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Processeur: {spoofed_info['Processeur']}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Disque dur: {spoofed_info['Disque_dur']}" + Style.RESET_ALL)

# Fonction pour afficher l'ASCII art
def print_header():
    header = """
 ░▒▓███████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░  
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    """
    print(Fore.YELLOW + header + Style.RESET_ALL)

# Fonction pour afficher le menu
def print_menu():
    menu = """
    ==============================
    |   MENU SPOOFER MLK PIKA   |
    ==============================
    1. Changer l'adresse MAC
    2. Modifier l'ID du volume (Windows uniquement)
    3. Changer le nom du PC
    4. Modifier les numéros de série des composants
    5. Spoofer tout (MAC, Volume ID, Nom PC, Séries)
    ==============================
    """
    print(Fore.YELLOW + menu + Style.RESET_ALL)

# Fonction pour effectuer tout le spoofing
def spoof_all():
    print(Fore.YELLOW + "Spoofing complet en cours..." + Style.RESET_ALL)
    change_mac_address("Ethernet")
    change_serial_numbers()
    change_computer_name()
    print(Fore.GREEN + "Toutes les informations matérielles ont été spoofées avec succès !" + Style.RESET_ALL)

# Fonction principale du programme
def main():
    print_header()  # Affichage du header une seule fois
    print_menu()  # Affichage du menu une seule fois
    choice = input(Fore.YELLOW + "\nChoisissez une option : " + Style.RESET_ALL)
    
    if choice == "1":
        interface = input("Entrez le nom de l'interface réseau (ex: Ethernet, Wi-Fi) : ")
        change_mac_address(interface)
    elif choice == "2":
        print(Fore.RED + "Cette option est spécifique à Windows uniquement." + Style.RESET_ALL)
    elif choice == "3":
        change_computer_name()
    elif choice == "4":
        change_serial_numbers()
    elif choice == "5":
        spoof_all()
    else:
        print(Fore.RED + "Option invalide." + Style.RESET_ALL)

# Lancer l'application
if __name__ == "__main__":
    main()

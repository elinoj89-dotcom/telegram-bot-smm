import sys
import time
import json
from datetime import datetime
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- FONCTIONS DE GESTION ---
def charger_cles():
    try:
        with open('bots.json', 'r') as f:
            data = json.load(f)
            return data.get("active_keys", [])
    except FileNotFoundError:
        console.print("[bold red]Erreur: Fichier bots.json introuvable ![/bold red]")
        return []

def enregistrer_utilisation(cle):
    """Enregistre la clé utilisée et l'heure dans un fichier log.txt"""
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{horodatage}] Clé utilisée : {cle}\n"
    
    with open("log.txt", "a") as f:
        f.write(log_entry)

def verifier_cle():
    console.clear()
    console.print(Panel("[bold cyan]🔐 AUTHENTICATION REQUIRED[/bold cyan]", border_style="cyan"))
    
    # Charge les clés autorisées
    cles_valides = charger_cles()
    
    # Demande la clé à l'utilisateur
    cle_utilisateur = console.input("[bold yellow]Enter your License Key : [/bold yellow]")
    
    # Vérification
    if cle_utilisateur in cles_valides:
        console.print("[bold green]✔ License Verified ! Loading Dashboard...[/bold green]\n")
        
        # Enregistre l'utilisation de la clé
        enregistrer_utilisation(cle_utilisateur)
        
        time.sleep(1)
        return True
    else:
        console.print("[bold red]✘ Invalid Key or Key Expired. Access Denied.[/bold red]")
        time.sleep(2)
        return False

def lancer_interface():
    # Ici, ton interface stylée
    console.clear()
    console.print(Panel("[bold green]SMM Dashboard Active[/bold green]", border_style="green"))

if __name__ == "__main__":
    if verifier_cle():
        lancer_interface()
    else:
        sys.exit()
    

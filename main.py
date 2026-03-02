import sys
import time
import json
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- CHARGEMENT DES CLÉS DEPUIS JSON ---
def charger_cles():
    try:
        with open('bots.json', 'r') as f:
            data = json.load(f)
            return data.get("active_keys", [])
    except FileNotFoundError:
        console.print("[bold red]Erreur: Fichier bots.json introuvable ![/bold red]")
        return []

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
    

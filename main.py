import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# --- CONFIGURATION ---
# Dans la réalité, cette clé serait vérifiée en ligne via une API
CLE_VALIDE = "FLEX-SMM-2026" 
# ---------------------

def verifier_cle():
    console.clear()
    console.print(Panel("[bold cyan]🔐 AUTHENTICATION REQUIRED[/bold cyan]", border_style="cyan"))
    
    # Demande la clé à l'utilisateur
    cle_utilisateur = console.input("[bold yellow]Enter your License Key : [/bold yellow]")
    
    # Vérification
    if cle_utilisateur == CLE_VALIDE:
        console.print("[bold green]✔ License Verified ! Loading Dashboard...[/bold green]\n")
        time.sleep(1)
        return True
    else:
        console.print("[bold red]✘ Invalid Key. Access Denied.[/bold red]")
        time.sleep(2)
        return False

def lancer_interface():
    console.clear()
    header = Text("SMM AUTOMATION DASHBOARD", style="bold white on blue", justify="center")
    console.print(Panel(header, border_style="blue"))
    console.print(Panel("[bold green][✔] Status :[/bold green] [white]Connected[/white]\n"
                        "[bold yellow][⚡] Credits :[/bold yellow] [white]1000[/white]", 
                        title="Bot Info", border_style="yellow"))
    # ... tu peux ajouter ici le reste de l'interface graphique ...

if __name__ == "__main__":
    if verifier_cle():
        lancer_interface()
    else:
        sys.exit() # Ferme le programme si la clé est fausse
        ]

    for id, action, cible, statut in actions:
        table.add_row(id, action, cible, statut)
        
    console.print(table)

    # 4. Simulation de tâche en cours
    console.print("\n[bold magenta][⌛] Vérification de sécurité en cours...[/bold magenta]")
    
    # Barre de progression fictive
    for _ in track(range(5), description="[yellow]Analyse...[/yellow]"):
        time.sleep(0.5)
        
    console.print("[bold green][✔] Vérification réussie ![/bold green]")

if __name__ == "__main__":
    afficher_interface_generique()
    

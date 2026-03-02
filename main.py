import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import track

# Initialisation de la console pour l'affichage stylé
console = Console()

def afficher_interface_generique():
    console.clear()
    
    # 1. En-tête du script
    header = Text("BOT D'AUTOMATISATION SMM - MODÈLE", style="bold white on blue", justify="center")
    console.print(Panel(header, border_style="blue"))

    # 2. Section Informations du compte (Fictif)
    console.print(Panel(
        "[bold green][✔] Statut :[/bold green] [white]Connecté[/white]\n"
        "[bold yellow][⚡] Crédits :[/bold yellow] [white]1000[/white]",
        title="Infos Bot", border_style="yellow"
    ))

    # 3. Tableau de bord des actions (Données fictives)
    table = Table(title="[bold]Journal d'activité[/bold]", border_style="cyan")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Action", style="white")
    table.add_column("Cible", style="white")
    table.add_column("Statut", justify="right")

    # Simulation d'actions dans le tableau
    actions = [
        ("01", "Interaction", "Utilisateur_A", "[bold green]Succès[/bold green]"),
        ("02", "Interaction", "Utilisateur_B", "[bold green]Succès[/bold green]"),
        ("03", "Interaction", "Utilisateur_C", "[bold red]Échec[/bold red]"),
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
    

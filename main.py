from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import track
import time

console = Console()

def run_script():
    # En-tête du script
    console.print(Panel("[bold cyan]INSTA-AUTO v2.0[/bold cyan]", expand=False))

    # Simulation d'une boucle sur plusieurs utilisateurs
    users = ["ninablicks", "sayudancestories", "izav_beauty"]
    
    for i, user in enumerate(users, 1):
        # Création du texte pour le bloc utilisateur
        user_info = Text()
        user_info.append(f"[{i:02}] Username: ", style="white")
        user_info.append(f"{user} ", style="bold green")
        user_info.append("[11]:[00]", style="bright_blue")
        
        # Affichage dans un panneau avec bordure fine
        console.print(Panel(user_info, border_style="white"))
        
        if user == "sayudancestories":
            console.print("[magenta][🔗] PostLink:[/magenta] https://www.instagram.com/p/DVX8MaqDrqb/")
            console.print("[yellow][⚡] PostID:[/yellow] 3843805543031290523")
            console.print("[bold green][✔] J'aime Succès[/bold green] [white][3189.2 + 1.1] CashCoins[/white]")
        
        time.sleep(0.5)

    # Simulation du Bypass Captcha avec une barre de progression
    console.print("\n[bold red][🤖] Security check detected![/bold red]")
    for _ in track(range(10), description="[yellow]Bypassing Captcha..."):
        time.sleep(0.2)
        
    console.print("[bold green]✅ Captcha Bypassed Successfully![/bold green]")

if __name__ == "__main__":
    run_script()
        

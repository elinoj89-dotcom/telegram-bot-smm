import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import time

console = Console()

def generer_interface():
    # 1. Le gros logo SMM en ASCII Art
    logo = pyfiglet.figlet_format("SMM", font="block")
    console.print(f"[bold cyan]{logo}[/bold cyan]")

    # 2. Le bloc d'infos (Tool Name, Developer, etc.)
    infos = Text()
    infos.append("[•] TOOL NAME   >> SMM\n", style="green")
    infos.append("[•] DEVELOPPER  >> TON_NOM\n", style="green")
    infos.append("[•] INTERFACE   >> Web Scraping\n", style="green")
    infos.append("[•] VERSION     >> 1.0", style="green")
    
    console.print(Panel(infos, border_style="white"))

    # 3. Le bandeau du compte
    console.print(Panel("[bold yellow][✔] Votre compte:[/bold yellow] [white]Utilisateur Test[/white]", border_style="magenta"))

    # 4. Simulation de la ligne de compteurs (J, H, M, S)
    console.print("[bold magenta]⌛ [7] J [] H [11] M [] S ⌛[/bold magenta]")
    print("-" * 40)

    # 5. Simulation d'une action comme sur l'image
    action = Text()
    action.append("[04] Username: ", style="white")
    action.append("reoudid01 ", style="bold green")
    action.append("[06]:[54]\n", style="blue")
    action.append("[🔗] UserLink: https://instagram.com/...\n", style="magenta")
    action.append("[⚡] UserID: 47382438049\n", style="yellow")
    action.append("[✔] Followers Succès [0 + 1.25] CashCoins", style="bold green")
    
    console.print(action)

    # 6. Section Captcha
    console.print("\n[bold magenta][🤖] Security check[/bold magenta]")
    console.print("[bold white][💀] Emojie indice: √[/bold white]")
    console.print("[bold green][✔] 3 images recuperer[/bold green]")
    console.print("[bold green][✔] Answer: 19[/bold green]")
    console.print("[yellow][...] Bypass Captcha[/yellow]")

if __name__ == "__main__":
    generer_interface()
    

from rich.console import Console
console = Console()

def print_success(message):
    console.print(f"[bold green]✔ {message}[/bold green]")

def print_error(message):
    console.print(f"[bold red]✖ {message}[/bold red]")

def print_info(message):
    console.print(f"[cyan]{message}[/cyan]")

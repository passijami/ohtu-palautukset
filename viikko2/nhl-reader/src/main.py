from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

def main():
    console = Console()

    console.print("[bold cyan]NHL Player Statistics[/bold cyan]")
    console.print("")

    nationality = Prompt.ask(
	"Anna kansalaisuus",
	default="FIN"
    ).upper()

    season = Prompt.ask(
        "Anna kausi",
	default="2024-25"
    )

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_by_nationality(nationality)

    table = Table(
	title=f"Players from {nationality} – Season {season}",
	header_style="bold magenta"
    )

    table.add_column("Player", style="red")
    table.add_column("Team", style="green")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="cyan")


    for player in players:
        points = player.goals + player.assists

        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(points)
        )

    if players:
        console.print(table)
    else:
        console.print(
            f"[yellow]No players found for {nationality}.[/yellow]"
        )

if __name__ == "__main__":
    main()

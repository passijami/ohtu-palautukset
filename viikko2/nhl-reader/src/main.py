"""Command-line interface for NHL player statistics."""

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    """Prompt for filters and display matching player statistics."""
    console = Console()

    console.print("[bold cyan]NHL Player Statistics[/bold cyan]")
    console.print("")

    search_type = Prompt.ask(
        "Hae pelaajia kansalaisuuden vai joukkueen mukaan?",
        choices=["kansalaisuus", "joukkue"],
        default="kansalaisuus"
    )

    if search_type == "joukkue":
        search_value = Prompt.ask("Anna joukkueen tunnus").upper()
    else:
        search_value = Prompt.ask(
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

    if search_type == "joukkue":
        players = stats.top_by_team(search_value)
        title = f"Players from {search_value} – Season {season}"
    else:
        players = stats.top_by_nationality(search_value)
        title = f"Players from {search_value} – Season {season}"

    table = Table(
        title=title,
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
            f"[yellow]No players found for {search_value}.[/yellow]"
        )

if __name__ == "__main__":
    main()

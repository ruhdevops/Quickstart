from prefect import flow, task
import random
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

console = Console()


@task
def get_customer_ids() -> list[str]:
    # Fetch customer IDs from a database or API
    return [f"customer{n}" for n in random.choices(range(100), k=50)]


@task
def process_customer(customer_id: str) -> str:
    # Process a single customer
    return f"Processed {customer_id}"


@flow(log_prints=True)
def main():
    """
    ### 🚀 Getting Started with Prefect
    This flow demonstrates how to map a task over a list of inputs.
    It fetches a list of customer IDs and processes each one individually.
    """
    customer_ids = get_customer_ids()
    # Map the process_customer task across all customer IDs
    console.print(f"[bold blue]📦 Fetched {len(customer_ids)} customer IDs[/bold blue]")

    with console.status("[bold green]Processing customers..."):
        results = process_customer.map(customer_ids)

    console.print(
        Panel.fit(
            f"[bold green]✅ Successfully processed {len(results)} customers![/bold green]",
            title="Success",
            border_style="green",
        )
    )

    console.print(Rule(style="blue"))
    console.print(
        "[bold blue]➡️ Next Step:[/bold blue] Try running [cyan]python 02_logging.py[/cyan] to learn about logging in Prefect!"
    )

    return results


if __name__ == "__main__":
    main()

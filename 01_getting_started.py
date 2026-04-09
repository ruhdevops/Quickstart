from prefect import flow, task
import random
import time
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table

console = Console()


@task
def get_customer_ids() -> list[str]:
    """Fetch customer IDs from a database or API."""
    # Use sorted and zero-padded IDs for better terminal alignment
    # Use random.sample to ensure unique customer IDs in the demo
    ids = [f"customer-{n:02d}" for n in random.sample(range(100), k=5)]
    # Add a brief pause to make the fetching state visible in the UI
    time.sleep(0.1)
    return sorted(ids)


@task
def process_customer(customer_id: str) -> str:
    """Process a single customer."""
    # Add a brief pause to make the processing state visible in the UI
    time.sleep(0.1)
    return f"Processed {customer_id}"


@flow(log_prints=True)
def main():
    """
    ### 🚀 Getting Started with Prefect

    This flow demonstrates how to map a task over a list of inputs.
    It fetches a list of customer IDs and processes each one individually.
    """
    start_time = time.perf_counter()
    # Display the flow's purpose for a guided onboarding experience
    if main.__doc__:
        console.print(
            Panel(
                Markdown(main.__doc__.strip()),
                title="Prefect Workflow Guide",
                border_style="blue",
                padding=(1, 2),
            )
        )

    console.print()

    with console.status("[bold green]🔍 Fetching customer data..."):
        customer_ids = get_customer_ids()

    console.print(
        f"[bold blue]📦 Successfully fetched {len(customer_ids)} customer IDs[/bold blue]"
    )
    console.print()

    with console.status("[bold green]⚙️ Processing customers..."):
        futures = process_customer.map(customer_ids)
        # Explicitly wait for results to avoid AttributeErrors on futures
        results = [f.result() for f in futures]

    duration = time.perf_counter() - start_time

    # Display results in a clean table for better readability
    console.print()
    table = Table(
        title="Processing Summary",
        show_header=True,
        header_style="bold blue",
        show_footer=True,
    )
    table.add_column("Customer ID", style="cyan", footer="Total")
    table.add_column(
        "Status", style="green", footer=f"[bold]{len(results)} Processed[/bold]"
    )

    # Use zip to map results back to their original IDs more reliably
    for customer_id, res in zip(customer_ids, results):
        table.add_row(customer_id, "✅ Success")

    console.print(table)
    console.print()

    console.print(
        Panel.fit(
            f"[bold green]✨ Successfully processed {len(results)} customers in {duration:.2f}s![/bold green]",
            title="Result",
            border_style="green",
        )
    )

    console.print(Rule("Next Step", style="blue"))
    console.print(
        "Try running [cyan]python 02_logging.py[/cyan] to learn about logging in Prefect!"
    )

    return results


if __name__ == "__main__":
    main()

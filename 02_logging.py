from prefect import flow, task
from prefect.logging import get_run_logger
import random
import time
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table

console = Console()


@task
def get_customer_ids() -> list[str]:
    """Fetch customer IDs from a database or API."""
    # Use sorted and zero-padded IDs for better terminal alignment
    ids = [f"customer-{n:02d}" for n in random.choices(range(100), k=5)]
    return sorted(ids)


@task
def process_customer(customer_id: str) -> str:
    """Process a single customer."""
    logger = get_run_logger()
    for _ in range(3):
        # Add a brief pause to make the logging visible and realistic
        time.sleep(0.05)
        logger.info(f"Processing customer {customer_id}")
    return f"Processed {customer_id}"


@flow(log_prints=True)
def main():
    """
    ### 📊 Logging with Prefect

    This flow demonstrates how to use the Prefect logger and capture standard output.
    It processes customer data and logs progress at each step.

    **Key Features:**
    - Capture standard `print` statements as logs with `log_prints=True`.
    - Use the Prefect logger for structured logging in tasks.
    - Map tasks across a list of inputs.
    """
    with console.status("[bold green]Fetching customer data..."):
        customer_ids = get_customer_ids()

    console.print(f"[bold blue]📦 Fetched {len(customer_ids)} customer IDs[/bold blue]")

    with console.status("[bold green]Processing customers with logging..."):
        futures = process_customer.map(customer_ids)
        # Explicitly wait for results to avoid AttributeErrors on futures
        results = [f.result() for f in futures]

    # Display results in a clean table for better readability
    table = Table(
        title="Processing Summary", show_header=True, header_style="bold blue"
    )
    table.add_column("Customer ID", style="cyan")
    table.add_column("Status", style="green")

    for res in results:
        # Extract the customer ID from the result string (e.g., "Processed customer-01")
        customer_id = res.split()[-1]
        table.add_row(customer_id, "✅ Success")

    console.print()
    console.print(table)
    console.print()

    console.print(
        Panel.fit(
            f"[bold green]✅ Successfully processed {len(results)} customers with detailed logging![/bold green]",
            title="Success",
            border_style="green",
        )
    )

    console.print(Rule(style="blue"))
    console.print(
        "[bold blue]🎉 You've completed the Quickstart! Check out the [cyan]README.md[/cyan] for more features.[/bold blue]"
    )

    return results


if __name__ == "__main__":
    main()

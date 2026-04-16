from prefect import flow, task
from prefect.logging import get_run_logger
import random
import time
from rich import box
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table

console = Console()


@task(name="Fetch Customer Data", task_run_name="fetch-customer-data")
def get_customer_ids() -> list[str]:
    """Fetch customer IDs from a database or API."""
    # Use sorted and zero-padded IDs for better terminal alignment
    # Use random.sample to ensure unique IDs in the demo output
    ids = [f"customer-{n:02d}" for n in random.sample(range(100), k=5)]
    return sorted(ids)


@task(name="Process Customer", task_run_name="process-{customer_id}")
def process_customer(customer_id: str) -> str:
    """Process a single customer."""
    logger = get_run_logger()
    for _ in range(3):
        # Add a brief pause to make the logging visible and realistic
        time.sleep(0.05)
        logger.info(f"Processing customer {customer_id}")
    return f"Processed {customer_id}"


@flow(name="Logging Workflow", log_prints=True)
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
    # Start timer to measure total execution duration
    start_time = time.perf_counter()

    # Display the flow's purpose for a guided onboarding experience
    if main.__doc__:
        console.print(
            Panel(
                Markdown(main.__doc__.strip()),
                title="Prefect Workflow Guide",
                border_style="bold blue",
                padding=(1, 2),
            )
        )

    console.print()

    with console.status("[bold green]🔍 Fetching customer data..."):
        customer_ids = get_customer_ids()

    console.print(
        f"[bold blue]📦 Successfully fetched [bold cyan]{len(customer_ids)}[/bold cyan] customer IDs[/bold blue]"
    )
    console.print()

    with console.status("[bold green]⚙️ Processing customers with logging..."):
        futures = process_customer.map(customer_ids)
        # Explicitly wait for results to avoid AttributeErrors on futures
        results = [f.result() for f in futures]

    # Calculate duration
    duration = time.perf_counter() - start_time

    # Add visual breathing room before results
    console.print()

    # Display results in a clean table for better readability
    table = Table(
        title="Processing Summary",
        title_style="bold blue",
        show_header=True,
        header_style="bold blue",
        show_footer=True,
        box=box.ROUNDED,
    )
    table.add_column("Customer ID", style="cyan", footer="Total", footer_style="bold")
    table.add_column(
        "Status",
        style="green",
        footer=f"{len(results)} Processed ✅",
        footer_style="bold blue",
    )

    # Use zip to map results back to their original IDs more reliably
    for customer_id, res in zip(customer_ids, results):
        table.add_row(customer_id, "✅ Success")

    console.print(table)
    console.print()

    console.print(
        Panel.fit(
            f"[bold green]Successfully processed [bold cyan]{len(results)}[/bold cyan] customers with detailed logging in [bold cyan]{duration:.2f}s[/bold cyan]![/bold green]",
            title="📊 Result",
            border_style="bold blue",
        )
    )

    console.print()
    console.print(Rule("🎉 Finishing Up", style="bold blue"))
    console.print(
        "[bold blue]🎉 You've completed the Quickstart! Check out the[/bold blue] [cyan]README.md[/cyan] [bold blue]for more features.[/bold blue]"
    )

    return results


if __name__ == "__main__":
    main()

from prefect import flow, task
from prefect.logging import get_run_logger
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
    # Use random.sample to ensure unique customer IDs
    ids = [f"customer-{n:02d}" for n in random.sample(range(100), k=5)]
    # Using random.sample ensures unique IDs for a more realistic demo
    ids = [f"customer-{n:02d}" for n in random.sample(range(100), k=5)]
    # Use random.sample to ensure unique customer IDs in the demo
    ids = [f"customer-{n:02d}" for n in random.sample(range(100), k=5)]
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

    with console.status("[bold green]⚙️ Processing customers with logging..."):
        futures = process_customer.map(customer_ids)
        # Explicitly wait for results to avoid AttributeErrors on futures
        results = [f.result() for f in futures]

    duration = time.perf_counter() - start_time

    # Display results in a clean table for better readability
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

    duration = time.perf_counter() - start_time

    console.print(
        Panel.fit(
            f"[bold green]✨ Successfully processed {len(results)} customers in {duration:.2f}s![/bold green]",
            title="Result",
            border_style="green",
        )
    )

    console.print(Rule("Next Step", style="blue"))
    console.print(Rule("Conclusion", style="blue"))
    console.print(
        "🎉 You've completed the Quickstart! Check out the [cyan]README.md[/cyan] for more features."
    console.print()
    console.print(Rule("🎉 Finishing Up", style="bold blue"))
    console.print(
        "[bold blue]🎉 You've completed the Quickstart! Check out the [cyan]README.md[/cyan] for more features.[/bold blue]"
    )

    return results


if __name__ == "__main__":
    main()

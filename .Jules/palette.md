## 2025-05-15 - [Naming Conventions vs. Packaging Requirements]
**Learning:** In projects using numbered prefixes for demo scripts (e.g., `01_script.py`), these files cannot be used directly as console script entry points in `pyproject.toml` because they are not valid Python module names. Attempting to "fix" this by renaming the files may break established naming conventions and user expectations.
**Action:** Prefer maintaining existing naming conventions over forcing script entry points. If a demo script needs to be an entry point, create a separate wrapper module with a valid name rather than renaming the numbered file.

## 2026-03-28 - [Guided CLI Onboarding]
**Learning:** For tutorial-style scaffolds, adding "Next Step" guidance directly to the terminal output after a successful run creates a much smoother onboarding experience than relying solely on the README.
**Action:** Always include a clear, visually distinct "Next Step" message at the end of introductory scripts to guide users through the intended learning path.

## 2026-03-30 - [Demo Scale vs. Terminal Readability]
**Learning:** For demo scripts, larger data sets can degrade the UX by flooding the terminal with logs, making it harder for users to see the structure of the output.
**Action:** Limit the default number of items in demo loops (e.g., 5 items) to maintain a high signal-to-noise ratio while still demonstrating the functionality.

## 2026-03-31 - [Visual Polish for CLI Summaries]
**Learning:** In CLI-based workflow scaffolds, replacing raw success messages with structured `rich.table.Table` summaries significantly improves the professional feel and readability of the output. Additionally, zero-padding generated IDs (e.g., 'customer-01') ensures natural sorting and vertical alignment, which reduces cognitive load when scanning lists. Finally, adding minimal artificial delays (e.g., `time.sleep(0.1)`) in demo scripts makes the "work" visible by giving terminal spinners and status indicators enough time to register with the user.
**Action:** Use structured tables for final execution summaries, ensure all generated IDs are zero-padded for alignment, and include brief pacing pauses in demo tasks to make the execution flow more perceptible.

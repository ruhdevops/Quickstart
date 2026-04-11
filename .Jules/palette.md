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

## 2026-04-01 - [CLI Onboarding & Information Density]
**Learning:** For terminal-based workflow scaffolds, rendering the flow's docstring as a 'Prefect Workflow Guide' using `rich.Markdown` inside a `rich.Panel` provides immediate, high-quality context to the user. Additionally, adding footers to summary tables (e.g., total items processed) improves information density and allows users to verify outcomes at a glance.
**Action:** Incorporate a Markdown-rendered welcome panel at the start of main entry points and include summary footers in result tables to enhance clarity and professional feel.

## 2026-04-02 - [Realistic Mock Data for CLI Clarity]
**Learning:** In terminal-based demos, using `random.choices` for small mock data sets can lead to duplicate entries, which can confuse users or make the summary tables look broken.
**Action:** Use `random.sample` instead of `random.choices` when generating mock data for tutorial scripts to ensure uniqueness and maintain a professional appearance in terminal output.
## 2026-04-02 - [Execution Feedback & Visual Hierarchy]
**Learning:** For CLI-based onboarding, providing immediate feedback on execution duration via `time.perf_counter()` and using titled `rich.Rule` components significantly improves the professional feel and clarity of the workflow completion state.
**Action:** Incorporate high-resolution execution timing in final result panels and add descriptive titles to terminal rules to better guide users through multi-step onboarding processes.

## 2026-04-02 - [Micro-UX Polish for Demo CLI Scripts]
**Learning:** For tutorial-style CLI scaffolds, several micro-UX touches significantly improve the professional feel and onboarding experience: (1) using `random.sample` instead of `random.choices` for unique mock data generation; (2) displaying the total execution duration in the final success panel; and (3) adding descriptive titles to `rich.Rule` components for better visual hierarchy between results and "Next Step" guidance.
**Action:** Ensure all demo scripts use unique mock data, provide performance feedback via execution duration, and utilize rule-titles for clear sectional separation.

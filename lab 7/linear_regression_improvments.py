"""
Name: Student
Course: HSC 4933
Assignment: Linear Regression Improvements
Description:
    Load a user-selected CSV file, clean selected numeric columns, and create
    an ordinary least squares regression plot. Improvements include an
    interactive command-line plot-formatting interface and plotting two
    dependent variables against one independent variable.

Privacy note: This program does not contain or hardcode patient-level data.
"""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm


def get_csv_path():
    """Ask the user for a CSV path and verify that it exists."""
    while True:
        file_name = input("Enter the CSV file path (for example, birthwt.csv): ").strip().strip('"')
        csv_path = Path(file_name).expanduser()
        if csv_path.is_file() and csv_path.suffix.lower() == ".csv":
            return csv_path
        print("File not found or not a CSV. Check the filename/path and try again.")


def load_dataset(csv_path):
    """Load a CSV and show available column names."""
    try:
        data = pd.read_csv(csv_path)
    except (OSError, pd.errors.ParserError, UnicodeDecodeError) as error:
        print(f"Could not read the CSV: {error}")
        return None

    if data.empty:
        print("The selected CSV has no data rows.")
        return None

    # Normalize column names for easier selection without changing source data.
    data.columns = [str(column).strip() for column in data.columns]
    print("\nAvailable columns:")
    for column in data.columns:
        print(f"  - {column}")
    return data


def convert_numeric(values):
    """Convert values to numbers, accepting counts formatted with commas."""
    cleaned_values = values.astype("string").str.replace(",", "", regex=False).str.strip()
    return pd.to_numeric(cleaned_values, errors="coerce")


def select_numeric_column(data, prompt, excluded=None):
    """Prompt until the user selects a column with numeric values."""
    excluded = set(excluded or [])
    while True:
        name = input(prompt).strip()
        if name not in data.columns:
            print("That column was not found. Copy a column name from the list above.")
            continue
        if name in excluded:
            print("Choose a different column from the one already selected.")
            continue
        numeric_values = convert_numeric(data[name])
        if numeric_values.notna().sum() < 3:
            print("That column has fewer than three numeric observations. Choose another.")
            continue
        return name


def ask_choice(prompt, allowed, default):
    """Get a case-insensitive choice, using a default when left blank."""
    allowed_lower = {choice.lower(): choice for choice in allowed}
    while True:
        answer = input(f"{prompt} ({'/'.join(allowed)}, default {default}): ").strip()
        if not answer:
            return default
        if answer.lower() in allowed_lower:
            return allowed_lower[answer.lower()]
        print("Please choose one of the listed options.")


def get_plot_settings():
    """Improvement 2: collect plot-formatting preferences through the CLI."""
    print("\n--- Plot formatting options ---")
    title = input("Custom plot title (blank for an automatic title): ").strip()
    x_label = input("X-axis label (blank to use the column name): ").strip()
    first_color = input("Color for first outcome points/line (default tab:blue): ").strip() or "tab:blue"
    second_color = input("Color for second outcome points/line (default tab:orange): ").strip() or "tab:orange"

    while True:
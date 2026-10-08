## Linear Regression Script - IC #5 / Lab 7 / Sofia Spada / Python for health analytics


#  Loads a selected CSV dataset, cleans column names, allows the user
# to select independent (X) and dependent (Y) variables, creates a scatterplot,
#  calculates an OLS regression model, and optionally saves both plots.

Author: Sofia Spada
Course: Python for health analytics


#Notes:
    - No patient data is hardcoded in this script.
    - The dataset path, variables, and output filenames are entered by the user.
'''
import os
import re

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm


def clean_column_name(column_name):
    """Convert a column name to snake_case."""
    clean_name = str(column_name).strip().lower()
    clean_name = re.sub(r"[^a-z0-9]+", "_", clean_name)
    clean_name = re.sub(r"_+", "_", clean_name)
    return clean_name.strip("_")


def clean_column_names(dataframe):
    """Clean all dataframe column names and return the dataframe."""
    dataframe.columns = [
        clean_column_name(column) for column in dataframe.columns
    ]
    return dataframe


def get_dataset_path():
    """Prompt the user for the CSV dataset path."""
    while True:
        dataset_path = input(
            "\nEnter the path to the CSV dataset: "
        ).strip().strip('"').strip("'")

        if os.path.isfile(dataset_path):
            return dataset_path

        print("File not found. Please check the path and try again.")


def get_column_choice(dataframe, variable_type):
    """Prompt the user to select a valid column name."""
    while True:
        column_name = input(
            f"\nEnter the column name for the {variable_type} variable: "
        ).strip().lower()

        if column_name in dataframe.columns:
            return column_name

        print("That column was not found. Please enter one of the listed names.")


def get_save_choice(message):
    """Ask the user whether they want to save a figure."""
    while True:
        choice = input(f"\n{message} (y/n): ").strip().lower()

        if choice in {"y", "yes"}:
            return True

        if choice in {"n", "no"}:
            return False

        print("Please enter y or n.")


def get_output_filename():
    """Prompt the user for a custom output filename."""
    filename = input(
        "Enter a custom filename for the figure "
        "(example: scatterplot.png): "
    ).strip()

    if not filename.lower().endswith(".png"):
        filename += ".png"

    return filename


def main():
    """Run the linear regression workflow."""

    # ------------------------------------------------------------------
    # 1. Load the dataset selected by the user.
    # ------------------------------------------------------------------
    dataset_path = get_dataset_path()
    data = pd.read_csv(dataset_path)

    print("\nDataset loaded successfully.")

    # ------------------------------------------------------------------
    # 2. Clean column names to snake_case.
    # ------------------------------------------------------------------
    data = clean_column_names(data)

    # ------------------------------------------------------------------
    # 3. List available column names.
    # ------------------------------------------------------------------
    print("\nAvailable column names:")
    for column in data.columns:
        print(f"  - {column}")

    # ------------------------------------------------------------------
    # 4. Ask the user to select X and Y variables.
    # ------------------------------------------------------------------
    x_column = get_column_choice(data, "X (independent)")
    y_column = get_column_choice(data, "Y (dependent)")

    if x_column == y_column:
        print("\nX and Y variables must be different.")
        return

    # ------------------------------------------------------------------
    # 5. Remove rows missing either regression value.
    # ------------------------------------------------------------------
    regression_data = data[[x_column, y_column]].copy()

    regression_data[x_column] = pd.to_numeric(
        regression_data[x_column], errors="coerce"
    )
    regression_data[y_column] = pd.to_numeric(
        regression_data[y_column], errors="coerce"
    )

    regression_data = regression_data.dropna()

    if regression_data.empty:
        print("\nNo usable rows remain after removing missing values.")
        return

    print(
        f"\nRows available for regression: {len(regression_data)}"
    )

    # ------------------------------------------------------------------
    # 6. Create a scatterplot without a regression line.
    # ------------------------------------------------------------------
    plt.figure(figsize=(8, 6))

    plt.scatter(
        regression_data[x_column],
        regression_data[y_column]
    )

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} vs. {x_column}")
    plt.tight_layout()

    # ------------------------------------------------------------------
    # 7. Ask whether the scatterplot should be saved.
    # ------------------------------------------------------------------
    if get_save_choice("Would you like to save the scatterplot?"):
        filename = get_output_filename()
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        print(f"Scatterplot saved as: {filename}")

    plt.show()
    plt.close()

    # ------------------------------------------------------------------
    # 8. Calculate the OLS regression line.
    # ------------------------------------------------------------------
    x_values = sm.add_constant(regression_data[x_column])
    y_values = regression_data[y_column]

    model = sm.OLS(y_values, x_values).fit()

    intercept = model.params["const"]
    slope = model.params[x_column]
    r_squared = model.rsquared

    predicted_y = model.predict(x_values)

    # ------------------------------------------------------------------
    # Display regression results.
    # ------------------------------------------------------------------
    print("\nOLS Regression Results")
    print("-" * 40)
    print(f"Independent variable (X): {x_column}")
    print(f"Dependent variable (Y):   {y_column}")
    print(f"Beta 0 (intercept):        {intercept:.4f}")
    print(f"Beta 1 (slope):            {slope:.4f}")
    print(f"R-squared:                 {r_squared:.4f}")

    # ------------------------------------------------------------------
    # 9. Plot the OLS regression line on the scatterplot.
    # ------------------------------------------------------------------
    plt.figure(figsize=(8, 6))

    plt.scatter(
        regression_data[x_column],
        regression_data[y_column],
        label="Observed values"
    )

    # Sort X values so the regression line is drawn cleanly.
    sorted_data = regression_data.copy()
    sorted_data["predicted_y"] = predicted_y
    sorted_data = sorted_data.sort_values(by=x_column)

    plt.plot(
        sorted_data[x_column],
        sorted_data["predicted_y"],
        label="OLS regression line"
    )

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} vs. {x_column} with OLS Regression Line")
    plt.legend()
    plt.tight_layout()

    # ------------------------------------------------------------------
    # 10. Ask whether the regression plot should be saved.
    # ------------------------------------------------------------------
    if get_save_choice(
        "Would you like to save the scatterplot with the OLS regression line?"
    ):
        filename = get_output_filename()
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        print(f"OLS regression plot saved as: {filename}")

    plt.show()
    plt.close()

    print("\nScript completed successfully.")


if __name__ == "__main__":
    main()

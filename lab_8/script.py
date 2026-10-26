"""
Title: Regression Analysis Automation Script
Course: Data Science / Statistics Lab 8
Description:
    - Prompts the user for a specific dataset and loads it using pandas.
    - Cleans column names into 'snake_case' format.
    - Lists available columns.
    - Prompts the user for response and multiple predictor variables.
    - Drops rows containing missing values for selected variables.
    - Fits either a Logistic Regression model (with Confusion Matrix)
      or a Count-Variable Poisson Regression model (with VIF).
    - Asks the user if they wish to save the results to a custom .txt file.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import re


def clean_column_name(col):
    """Converts a column name to snake_case format."""
    col = str(col).strip().lower()
    col = re.sub(r'[^a-z0-9]+', '_', col)
    col = col.strip('_')
    return col


def main():
    print("==================================================")
    print("           REGRESSION ANALYSIS TOOLKIT            ")
    print("==================================================")

    # 3. Prompt user for dataset and load it
    file_path = input("Enter dataset filename (e.g., birthwt (2).csv or places_2025 (2).csv): ").strip()
    try:
        df = pd.read_csv(file_path)
        print(f"\n[INFO] Successfully loaded '{file_path}'. Shape: {df.shape}")
    except Exception as e:
        print(f"[ERROR] Could not load file: {e}")
        return

    # 4. Clean column names to 'snake_case' format
    df.columns = [clean_column_name(col) for col in df.columns]

    # 5. List available column names
    print("\n--------------------------------------------------")
    print("Available Columns (snake_case):")
    print("--------------------------------------------------")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")
    print("--------------------------------------------------")

    # 6. Prompt user for regression type and variables
    reg_type = input("Select regression type ('logistic' or 'poisson'): ").strip().lower()

    response_var = input("Enter response (dependent) variable name: ").strip()
    predictors_input = input("Enter predictor variable names separated by commas: ").strip()
    predictors = [p.strip() for p in predictors_input.split(',')]

    # 7. Remove rows missing any values used for the regression
    cols_to_use = [response_var] + predictors
    initial_rows = len(df)
    df_clean = df.dropna(subset=cols_to_use).copy()
    print(f"\n[INFO] Removed {initial_rows - len(df_clean)} rows with missing values.")
    print(f"[INFO] Clean dataset row count: {len(df_clean)}")

    # Initialize output list for file saving
    output_lines = []
    output_lines.append(f"Dataset Used: {file_path}")
    output_lines.append(f"Regression Type: {reg_type.upper()}")
    output_lines.append(f"Response Variable: {response_var}")
    output_lines.append(f"Predictors: {predictors}\n")

    # 8. Calculate regression model
    if reg_type == 'logistic':
        print("\n--- Running Logistic Regression ---")
        output_lines.append("=== LOGISTIC REGRESSION RESULTS ===")

        X = df_clean[predictors]
        X = sm.add_constant(X)
        y = df_clean[response_var]

        logit_model = sm.Logit(y, X)
        logit_results = logit_model.fit()

        summary_str = str(logit_results.summary())
        print(summary_str)
        output_lines.append(summary_str)

        # Pseudo R-squared
        pseudo_r2 = logit_results.prsquared
        pr2_str = f"\nPseudo R-squared (McFadden): {pseudo_r2:.4f}"
        print(pr2_str)
        output_lines.append(pr2_str)

        # Predictions & Confusion Matrix
        y_pred_prob = logit_results.predict(X)
        y_pred = (y_pred_prob >= 0.5).astype(int)

        cm = confusion_matrix(y, y_pred)
        cm_str = f"\nConfusion Matrix:\n{cm}"
        print(cm_str)
        output_lines.append(cm_str)

        acc = accuracy_score(y, y_pred)
        acc_str = f"Accuracy: {acc:.4f}"
        print(acc_str)
        output_lines.append(acc_str)

        report = classification_report(y, y_pred, digits=4, zero_division=0)
        rep_str = f"\nClassification Report:\n{report}"
        print(rep_str)
        output_lines.append(rep_str)

    elif reg_type == 'poisson':
        print("\n--- Running Count-Variable (Poisson) Regression ---")
        output_lines.append("=== POISSON REGRESSION RESULTS ===")

        X = df_clean[predictors]
        X = sm.add_constant(X)
        y = df_clean[response_var]

        poisson_model = sm.GLM(y, X, family=sm.families.Poisson())
        poisson_results = poisson_model.fit()

        summary_str = str(poisson_results.summary())
        print(summary_str)
        output_lines.append(summary_str)

        # Deviance-based Pseudo R-squared
        pseudo_r2 = 1 - (poisson_results.deviance / poisson_results.null_deviance)
        pr2_str = f"\nPseudo R-squared (Deviance-based): {pseudo_r2:.4f}"
        print(pr2_str)
        output_lines.append(pr2_str)

        # Variance Inflation Factor (VIF)
        print("\n--- Variance Inflation Factor (VIF) ---")
        output_lines.append("\n--- Variance Inflation Factor (VIF) ---")

        X_vif = df_clean[predictors].copy()
        X_vif['const'] = 1
        vif_data = pd.DataFrame()
        vif_data["Feature"] = X_vif.columns
        vif_data["VIF"] = [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[1])]

        vif_str = str(vif_data)
        print(vif_str)
        output_lines.append(vif_str)

    else:
        print("[ERROR] Invalid regression type specified. Choose 'logistic' or 'poisson'.")
        return

    # 9. Ask user if they would like to save the output to a .txt file
    save_choice = input("\nWould you like to save the output to a .txt file? (yes/no): ").strip().lower()
    if save_choice in ['yes', 'y']:
        out_filename = input("Enter custom filename: ").strip()
        with open(out_filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(output_lines))
        print(f"[INFO] Output successfully saved to '{out_filename}'.")


if __name__ == "__main__":
    main()
import os
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


def clean_column_names(df):
  """Cleans dataframe column names to snake_case format."""
  df.columns = (
      df.columns.str.strip()
      .str.lower()
      .str.replace(r'[^0-9a-zA-Z]+', '_', regex=True)
      .str.replace(r'_+', '_', regex=True)
      .str.strip('_')
  )
  return df


def main():
  print('--- Interactive OLS Regression & Plotting Tool ---')

  # 2. Prompt user for dataset and load it
  dataset_filename = input(
      'Enter the dataset filename (e.g., birthwt.csv or places_2025.csv): '
  ).strip()

  if not os.path.exists(dataset_filename):
    print(f"Error: File '{dataset_filename}' not found in the current directory.")
    return

  # Load dataset, handling potential thousands separators if present
  df = pd.read_csv(dataset_filename, thousands=',')

  # 3. Clean column names to 'snake_case'
  df = clean_column_names(df)

  # 4. List available column names
  print('\nAvailable columns in dataset:')
  for col in df.columns:
    print(f' - {col}')

  # 5. Prompt user for X and Y variables
  x_var = input(
      '\nEnter the column name you want as the X (independent) variable: '
  ).strip()
  y_var = input(
      'Enter the column name you want as the Y (dependent) variable: '
  ).strip()

  if x_var not in df.columns or y_var not in df.columns:
    print('Error: One or both specified column names are invalid.')
    return

  # 6. Remove rows missing either value used for regression
  initial_count = len(df)
  subset = df[[x_var, y_var]].dropna()
  # Convert to numeric in case data loaded as object
  subset[x_var] = pd.to_numeric(subset[x_var], errors='coerce')
  subset[y_var] = pd.to_numeric(subset[y_var], errors='coerce')
  subset = subset.dropna()

  print(
      f'Removed {initial_count - len(subset)} rows with missing or non-numeric'
      ' values.'
  )

  x = subset[x_var]
  y = subset[y_var]

  # 7. Create a scatterplot without regression line
  plt.figure(figsize=(8, 6))
  plt.scatter(x, y, alpha=0.6, edgecolors='k')
  plt.xlabel(x_var)
  plt.ylabel(y_var)
  plt.title(f'Scatterplot of {y_var} vs. {x_var}')
  plt.grid(True, linestyle='--', alpha=0.5)

  # 8. Ask user if they would like to save the scatterplot file
  save_first = (
      input('Would you like to save this scatterplot? (y/n): ')
      .strip()
      .lower()
  )
  if save_first == 'y':
    fig_name = input('Enter custom filename (e.g., fig_1.png): ').strip()
    os.makedirs(os.path.dirname(fig_name), exist_ok=True) if '/' in fig_name or '\\' in fig_name else None
    plt.savefig(fig_name, dpi=300, bbox_inches='tight')
    print(f"Saved scatterplot as '{fig_name}'.")

  # 9. Calculate OLS regression line
  slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
  r_squared = r_value**2
  print(f'\nOLS Regression Results:')
  print(f'Intercept (beta_0): {intercept:.4f}')
  print(f'Slope (beta_1): {slope:.4f}')
  print(f'R^2: {r_squared:.4f}')

  # 10. Plot the OLS regression line on the scatterplot
  plt.plot(
      x,
      intercept + slope * x,
      color='red',
      linewidth=2,
      label=(
          f'OLS Line: y = {slope:.2f}x + {intercept:.2f} ($R^2$ ='
          f' {r_squared:.2f})'
      ),
  )
  plt.legend()
  plt.title(f'Scatterplot with OLS Regression: {y_var} vs. {x_var}')

  # 11. Ask user if they would like to save the scatterplot with OLS line
  save_second = (
      input('Would you like to save the scatterplot with OLS line? (y/n): ')
      .strip()
      .lower()
  )
  if save_second == 'y':
    fig_name_reg = input(
        'Enter custom filename for regression plot (e.g., fig_2.png): '
    ).strip()
    plt.savefig(fig_name_reg, dpi=300, bbox_inches='tight')
    print(f"Saved regression plot as '{fig_name_reg}'.")

  plt.show()


if __name__ == '__main__':
  main()vimport os
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


def clean_column_names(df):
  """Cleans dataframe column names to snake_case format."""
  df.columns = (
      df.columns.str.strip()
      .str.lower()
      .str.replace(r'[^0-9a-zA-Z]+', '_', regex=True)
      .str.replace(r'_+', '_', regex=True)
      .str.strip('_')
  )
  return df


def main():
  print('--- Interactive OLS Regression & Plotting Tool ---')

  # 2. Prompt user for dataset and load it
  dataset_filename = input(
      'Enter the dataset filename (e.g., birthwt.csv or places_2025.csv): '
  ).strip()

  if not os.path.exists(dataset_filename):
    print(f"Error: File '{dataset_filename}' not found in the current directory.")
    return

  # Load dataset, handling potential thousands separators if present
  df = pd.read_csv(dataset_filename, thousands=',')

  # 3. Clean column names to 'snake_case'
  df = clean_column_names(df)

  # 4. List available column names
  print('\nAvailable columns in dataset:')
  for col in df.columns:
    print(f' - {col}')

  # 5. Prompt user for X and Y variables
  x_var = input(
      '\nEnter the column name you want as the X (independent) variable: '
  ).strip()
  y_var = input(
      'Enter the column name you want as the Y (dependent) variable: '
  ).strip()

  if x_var not in df.columns or y_var not in df.columns:
    print('Error: One or both specified column names are invalid.')
    return

  # 6. Remove rows missing either value used for regression
  initial_count = len(df)
  subset = df[[x_var, y_var]].dropna()
  # Convert to numeric in case data loaded as object
  subset[x_var] = pd.to_numeric(subset[x_var], errors='coerce')
  subset[y_var] = pd.to_numeric(subset[y_var], errors='coerce')
  subset = subset.dropna()

  print(
      f'Removed {initial_count - len(subset)} rows with missing or non-numeric'
      ' values.'
  )

  x = subset[x_var]
  y = subset[y_var]

  # 7. Create a scatterplot without regression line
  plt.figure(figsize=(8, 6))
  plt.scatter(x, y, alpha=0.6, edgecolors='k')
  plt.xlabel(x_var)
  plt.ylabel(y_var)
  plt.title(f'Scatterplot of {y_var} vs. {x_var}')
  plt.grid(True, linestyle='--', alpha=0.5)

  # 8. Ask user if they would like to save the scatterplot file
  save_first = (
      input('Would you like to save this scatterplot? (y/n): ')
      .strip()
      .lower()
  )
  if save_first == 'y':
    fig_name = input('Enter custom filename (e.g., fig_1.png): ').strip()
    os.makedirs(os.path.dirname(fig_name), exist_ok=True) if '/' in fig_name or '\\' in fig_name else None
    plt.savefig(fig_name, dpi=300, bbox_inches='tight')
    print(f"Saved scatterplot as '{fig_name}'.")

  # 9. Calculate OLS regression line
  slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
  r_squared = r_value**2
  print(f'\nOLS Regression Results:')
  print(f'Intercept (beta_0): {intercept:.4f}')
  print(f'Slope (beta_1): {slope:.4f}')
  print(f'R^2: {r_squared:.4f}')

  # 10. Plot the OLS regression line on the scatterplot
  plt.plot(
      x,
      intercept + slope * x,
      color='red',
      linewidth=2,
      label=(
          f'OLS Line: y = {slope:.2f}x + {intercept:.2f} ($R^2$ ='
          f' {r_squared:.2f})'
      ),
  )
  plt.legend()
  plt.title(f'Scatterplot with OLS Regression: {y_var} vs. {x_var}')

  # 11. Ask user if they would like to save the scatterplot with OLS line
  save_second = (
      input('Would you like to save the scatterplot with OLS line? (y/n): ')
      .strip()
      .lower()
  )
  if save_second == 'y':
    fig_name_reg = input(
        'Enter custom filename for regression plot (e.g., fig_2.png): '
    ).strip()
    plt.savefig(fig_name_reg, dpi=300, bbox_inches='tight')
    print(f"Saved regression plot as '{fig_name_reg}'.")

  plt.show()


if __name__ == '__main__':
  main()

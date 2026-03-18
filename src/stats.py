import pandas as pd

def get_column_statistics(df, col):

    # Select only desired columns
    df_selected = df[col].apply(pd.to_numeric, erros='coerce')

    # Generate statistics 
    stats_df = df_selected.describe().T

    # Add IQR columns
    stats_df['IQR'] = stats_df['75%'] - stats_df['25%']

    return stats_df
# Imports 
from src import histogram,boxplot, remove_outliers, stats, correlation
from src import constants as const

import pandas as pd

if __name__ == "__main__":
    # Read Excel file
    df = pd.read_csv(const.CSV_FILE, decimal=',', parse_dates=['date']) 

    # Columns to plot
    columns = [
        'date',
        '% Iron Feed', 
        '% Silica Feed', 
        'Starch Flow',
        'Amina Flow',
        'Ore Pulp Flow',
        'Ore Pulp pH',
        'Ore Pulp Density',
        '% Iron Concentrate',
        '% Silica Concentrate'
    ]  

    # Filter columns to be analysed
    df = df[columns]

    # Define datietime index 
    df.set_index('date', inplace = True)

    # Resample per hour (mean inside of hour)
    df_hourly = df.groupby(pd.Grouper(freq='h')).mean()

    # Verify result 
    #print(f'Hourly df: {df_hourly.head()}')   
    
    # Define variables to plot 
    cols_to_plot = [col for col in columns if col != 'date']

    # Generate histrogram for raw data 
    histogram.histogram(df, cols_to_plot, 'Histograma para dados brutos de:', 'hist') 

    # # Generate boxplot for raw data 
    boxplot.plot_boxplots(df, cols_to_plot, 'Boxplot para dados brutos de:', 'boxplot')

    # Remove outliers routine
    df_modified = remove_outliers.remove_outliers(df_hourly, cols_to_plot)
    #print(f'Df without outliers {df_modified.head()}')

    # Save in a new excel File
    # df_modified.to_excel(f'{const.OUTPUT_FILE}flotation_wot_outliers.xlsx', index=False)

    # Generate new histograms
    histogram.histogram(df_modified, cols_to_plot, 'Histograma após remoção de outliers:', 'hist_wot_outliers')

    # Generate new boxplots 
    boxplot.plot_boxplots(df_modified, cols_to_plot, 'Boxpolot após remoção de outliers:', 'boxplot_wot_outliers')

    # Get statistical information 
    stats.get_column_statistics(df_modified, cols_to_plot)

    # Get correlations with target values (%Fe Concentrate and %Si Concentrate)
    # Define target variables
    targets = ['% Iron Concentrate', '% Silica Concentrate']
    
    correlation.analyze_correlations(df_modified, targets)
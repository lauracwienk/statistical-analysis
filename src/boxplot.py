import matplotlib.pyplot as plt
import os

from src import constants as const


def plot_boxplots(
        df, 
        columns, 
        title,
        path
):

    for col in columns:
        plt.figure(figsize=(8,5))
        plt.boxplot(df[col].dropna())
        plt.title(f'{title}{col}')
        plt.ylabel(col)
        plt.grid(True, linestyle ='--', alpha=0.5)
        
        # Save figure 
        # Save figure
        filename = os.path.join(const.OUTPUT_FILE, f'{path}_{str(col)}.png')
        plt.savefig(filename)


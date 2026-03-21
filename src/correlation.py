import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

from src import constants as const

def analyze_correlations(
    df,
    targets,
    method_list = ['pearson', 'spearman']
):
    # Convert all data to numeric type 
    df = df.select_dtypes(include='number')

    results = {}

    for method in method_list:
        print(f'\n Correlation: ({method.upper()})')
        
        corr = df.corr(method=method)
        results[method] = corr
        
        # Correlação com targets
        for target in targets:
            print(f'\n Correlation with {target}:')
            print(corr[target].sort_values(ascending=False))
        
        # Heatmap
        plt.figure(figsize=(10,8))
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title(f'Heatmap - {method.capitalize()}')
        plt.savefig(f'{const.OUTPUT_FILE}heatmap.png', dpi=300, bbox_inches='tight')
        plt.close()

    # Scatter plots
    for target in targets:
        for col in df.columns:
            if col != target:
                plt.figure()
                sns.scatterplot(x=df[col], y=df[target])
                plt.xlabel(col)
                plt.ylabel(target)
                plt.title(f'{col} vs {target}')
                plt.savefig(f'{const.OUTPUT_FILE}{col}_scatter_plot.png', dpi=300, bbox_inches='tight')
                plt.close()

    return results
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(r'C:\Users\Compumundo\Desktop\Data Science\FreeCODECAMP\medical visualizer\medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] /(0.01*df['height'])**2
df['overweight'] = df['overweight'].apply(lambda x: 1 if x >= 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x != 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x != 1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
      # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df2 = df.melt(id_vars=['cardio'] , value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = pd.DataFrame(df2.groupby(['variable', 'value', 'cardio'])['value'].count()).rename( columns={'value': 'total'}).reset_index()
  
      # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
      
      # Draw the catplot with 'sns.catplot()'
  
      # Get the figure for the output
    fig = sns.catplot(x='variable', y="total", hue = 'value', col="cardio", data=df_cat, kind="bar" )
  
      # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # Clean the data
    df_heat = df.copy()

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    #fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    fig = sns.heatmap(corr, mask=mask, fmt='.1f', vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)

    # Do not modify the next two lines
    #fig.savefig('heatmap.png')
    return fig
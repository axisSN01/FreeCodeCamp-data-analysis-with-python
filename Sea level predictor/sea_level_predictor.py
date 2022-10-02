import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def draw_plot():
    # Read data from file
    df = pd.read_csv('/gdrive/MyDrive/Data Science/epa-sea-level.csv')#('epa-sea-level.csv')

    # Create scatter plot
    plt.style.use('dark_background')

    plt.figure(figsize=(24,6))

    plt.fill_between(df.iloc[:,0], df.iloc[:,3], df.iloc[:,2], alpha=0.7, linewidth=0)
    plt.scatter(df.iloc[:,0],df.iloc[:,1])

    # Create first line of best fit
    res = stats.linregress(df.iloc[:,0],df.iloc[:,1])
    plt.plot(df.iloc[:,0], res.intercept + res.slope*df.iloc[:,0], 'r', label='fitted line')

    # Create second line of best fit
    sr1 = pd.Series([int(i) for i in range(1880, 2050)])
    slope, intercept, r_value, p_value, std_err  = stats.linregress(df['Year'], df["CSIRO Adjusted Sea Level"])
    plt.plot(sr1, intercept + slope*sr1, 'r', label='best fit line from 1880 to 2050')

    recent = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err  = stats.linregress(recent['Year'], recent["CSIRO Adjusted Sea Level"])

    sr2 = pd.Series([int(i) for i in range(2000, 2050)])
    recent.append(sr2, ignore_index=True)
    plt.plot(sr2, intercept + slope*sr2, 'r', label='new best fit line after year 2000', color="pink")

    # Add labels and title
        
    plt.title("Sea Level")
    plt.xlabel("Year")
    plt.ylabel(df.columns[1])
    plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot(y='CSIRO Adjusted Sea Level',x='Year',kind='scatter')

    # Create first line of best fit
    res=linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    plt.xlim(1850,2075)
    x=pd.Series(range(1880,2051))
    plt.plot(x,res.intercept+res.slope*x,color='r',label='Line of best fit(1880-2050)')

    # Create second line of best fit
    df_2000=df[df['Year']>=2000]
    res=linregress(x=df_2000['Year'],y=df_2000['CSIRO Adjusted Sea Level'])
    x=pd.Series(range(2000,2051))
    plt.plot(x,res.intercept+res.slope*x,color='r',label='Line of best fit(2000-2050)')

    # Add labels and title

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
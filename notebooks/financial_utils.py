import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

def plot_individual_stock(df, name='AMAZON', color='black', year_ticks=True):    
    plt.figure(figsize=(8,5), dpi=200)

    plt.plot(df.index, df[name], label=name, color=color)
    if year_ticks:
        plt.gca().xaxis.set_major_locator(mdates.YearLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


def legend_unique_labels():
    # Get existing handles and labels
    handles, labels = plt.gca().get_legend_handles_labels()

    # Filter out duplicate legend items
    unique_handles = []
    unique_labels = []
    for handle, label in zip(handles, labels):
        if label not in unique_labels:
            unique_handles.append(handle)
            unique_labels.append(label)

    # Create legend with unique items
    plt.legend(unique_handles, unique_labels)

def get_predicted_prices(sims,nb_sim,prev_close):
    # Calculate predicted prices based on predicted returns
    predicted_returns = sims.values[-1, :nb_sim].T
    predicted_prices = [prev_close]

    for ret in predicted_returns:
        predicted_prices.append(predicted_prices[-1] * np.exp(ret))
    
    return predicted_prices

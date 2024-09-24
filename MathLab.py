def graphic_x_2():
    x = np.linspace(-10, 10, 400) 
    y = x**2
    plt.plot(x, y)
    plt.title('The graphic of function y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def graphic_more_functions():
    x1 = np.linspace(-10, 10, 1000) 
    y1 = x1**2
    y2 = x1**3
    y3 = x1**4
    fig, ax = plt.subplots()
    ax.plot(x1, y1, label='y = x^2', color='green', linestyle='--')
    ax.plot(x1, y2, label='y = x^3', color='blue', linestyle='-.')
    ax.plot(x1, y3, label='y = x^4', color='black', linestyle=':')
    ax.legend()
    plt.title('The graphic of function y = x^2, y = x^3 and y = x^4')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def scatter_plot_random_values():
    np.random.seed(42) 
    num_points = 100
    x_data = np.random.rand(num_points) * 10
    y_data = np.random.rand(num_points) * 10
    sizes = np.random.randint(20, 100, num_points)
    colors = np.random.rand(num_points, 3)  
    plt.scatter(x_data, y_data, s=sizes, c=colors, alpha=0.7, edgecolors='k')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter plot with random values')
    plt.show()

def histogram_random_values():
    np.random.seed(42) 
    data = np.random.normal(loc=5, scale=2, size=1000)  
    num_bins = 20  
    hist_type = 'stepfilled'  
    color = 'steelblue'  
    edgecolor = 'none'  
    plt.hist(data, bins=num_bins, alpha=0.5, histtype=hist_type, color=color, edgecolor=edgecolor)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

def layout():
    np.random.seed(42) 
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.exp(-x/2)
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('Layout with different graphs')
    axs[0, 0].plot(x, y1, label='sin(x)', color='yellow')
    axs[0, 0].set_title('Graphic of sin(x)')
    axs[0, 1].scatter(x, y2, label='cos(x)', color='blue', marker='o')
    axs[0, 1].set_title('Scatter plot of cos(x)')
    axs[1, 0].bar(x, y3, label='exp(-x/2)', color='red', alpha=0.7)
    axs[1, 0].set_title('Histogram of exp(-x/2)')
    axs[1, 1].plot(x, y1, label='sin(x)', color='purple')
    axs[1, 1].set_title('Graphic of sin(x)')
    axs[1, 1].set_xticks([])  
    axs[1, 1].legend().set_visible(False)  
    plt.tight_layout()
    plt.show()

def histogram(path):
    data = pd.read_csv(path)  
    data.hist(bins=6)  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Histogram')
    plt.show()

def diagram_with_letters():
    categories = ['I', 'Υ', 'Ρ', 'Χ', 'N', 'O'] 
    values1 = [20, 40, 60, 80, 50, 70]  
    values2 = [30, 20, 40, 20, 50, 30]  
    barWidth = 0.5
    r = np.arange(len(categories))
    plt.bar(r, values1, color='orange', edgecolor='white', width=barWidth)
    plt.bar(r, values2, bottom=values1, color='blue', edgecolor='white', width=barWidth)
    plt.ylim(0,100)
    plt.xticks(r, categories)
    plt.show()


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_customer = os.path.join(current_dir, 'customers-100.csv')


graphic_x_2()
graphic_more_functions()
scatter_plot_random_values()
histogram_random_values()
layout()
histogram(csv_file_path_customer)
diagram_with_letters()
import matplotlib.pyplot as plt

def plot_bar_chart(x, y, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

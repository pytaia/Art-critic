from data.elements import return_statistics
import matplotlib.pyplot as plt
import numpy as np


def graph_art(individual_number):
    # остроение статистики картины
    views, statistic = return_statistics(individual_number)
    vals = np.array(list(statistic.values()), int) / int(views)
    labels = list(statistic.keys())
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels)
    ax.axis("equal")
    fig.savefig('chart.png', dpi=60)
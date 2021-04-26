import matplotlib.pyplot as plt
import seaborn as sns

def cm_to_inch(value):
    """To change from cm to inch"""

    return value/2.54


def histogram_figure(x, y, x_label, y_label, rooth_path, name_fig):
    """Creating an histogram """

    # Creating the figure
    plt.figure(figsize=(cm_to_inch(20),cm_to_inch(10)))
    plt.bar(x=x, height=y, facecolor='#222220')

    # Labels
    plt.xlabel(x_label, weight="bold")
    plt.ylabel(y_label, weight="bold")
    plt.xticks(rotation="90")

    # Saving the figure
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Showing the figure
    plt.show()


def linediagram_figure(x, y, x_label, y_label, rooth_path, name_fig):
    """ Creating a line diagram """

    # Creating the figure
    plt.figure(figsize=(cm_to_inch(20),cm_to_inch(10)))
    plt.plot(x, y, color='#434343', marker=".", markersize=15, linewidth= 3, label="Year")

    # Labels
    plt.xlabel(x_label, weight="bold")
    plt.ylabel(y_label, weight="bold")
    plt.xticks(rotation="90")

    # Saving the figure
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Showing the figure
    plt.show()


def correlation_matrix(df):
    """ Creating a correlation matrix """
    
    # Creating the figure
    plt.figure(figsize=(cm_to_inch(30),cm_to_inch(20)))

    correlation_ = df.corr()
    heatmap_ = sns.heatmap(correlation_, cmap="bone",annot=True)
    fig_cor_ = heatmap_.get_figure()

    # Labels
    plt.yticks(va="center", rotation = 0)


def piechart_figure_6labels(x1, x2, x3, x4, x5, x6, labels, name_fig, rooth_path):
    
    # Creating the figure
    plt.figure(figsize=(cm_to_inch(20),cm_to_inch(20)))
    colors = ["#222220","#2C2C2C", "#434343", "#62635D", "#868781", "#D6D6D4"]
    plt.pie([x1, x2, x3, x4, x5, x6], labels = labels, colors=colors, autopct="%.1f %%")    

    # Saving the figure
    carpeta_reports = "\\reports"
    plt.savefig(rooth_path + carpeta_reports + name_fig, dpi=300, bbox_inches='tight')

    # Showing the figure
    plt.show()
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys, getopt

NB_SIMULATIONS = 10000
NB_INSERTIONS = 15


## FONCTIONS UTILITAIRES SUR LE MELANGE  ##########################################

# Construction d'un paquet de cartes à partir de la taille d'un paquet
def construction_paquet(taille_paquet):
    paquet = []
    for i in range(1, taille_paquet+1):
        paquet.append(i)
    return paquet



## FONCTIONS UTILITAIRES SUR LES TYPES  ###########################################

# Retourne l'indice de l'élément x dans le tableau tab
def get_indice(tab, x):
    i = 0
    while(tab[i] != x):
        i += 1
    return i

# Retourne le tableau des occurences des valeurs du tableau
def get_occurence(tab):
    tab_tmp = []
    nbr_occurence = []
    for val in tab:
        if val not in tab_tmp:
            tab_tmp += [val]
            nbr_occurence += [tab.count(val)]

    for i in range(0, len(nbr_occurence)):
        nbr_occurence[i] = nbr_occurence[i]/NB_SIMULATIONS
    
    return tab_tmp, nbr_occurence



## FONCTIONS ARITHMETIQUES  #######################################################

# Calcul du factoriel de x
def factor(x):
    res = 1
    for i in range(2, x+1):
        res *= i
    return res



## FONCTIONS AUXILIAIRES POUR LES GRAPHES  ########################################

# Affichage d'un graphe bar
def show_graph_bar(tab_x, tab_y, title_x, title_y, title):
    x = np.array(tab_x)
    y = np.array(tab_y)
    plt.xlabel(title_x)
    plt.ylabel(title_y)
    plt.title(title)
    plt.bar(x, y)
    plt.show()

# Sauvegarde un graphe bar
def save_graph_bar(tab_x, tab_y, title_x, title_y, title, name_file):
    x = np.array(tab_x)
    y = np.array(tab_y)
    plt.xlabel(title_x)
    plt.ylabel(title_y)
    plt.title(title)
    plt.bar(x, y)

    plt.savefig(name_file)
    plt.clf()

# Affiche un graphe Hist
def show_graph_hist(tab, title_x, title_y, title):
    plt.hist(tab, bins = 25, color = 'lightblue', edgecolor = 'black')
    plt.ylabel(title_y)
    plt.xlabel(title_x)
    plt.title(title)
    plt.show()

# Sauvegarde un graphe Hist
def save_graph_hist(tab, title_x, title_y, title, name_file):
    plt.hist(tab, bins = 25, color = 'lightblue', edgecolor = 'black')
    plt.ylabel(title_y)
    plt.xlabel(title_x)
    plt.title(title)
    plt.savefig(name_file)
    plt.clf()

# Affiche un graphe avec des points
def show_graph_plot(tab_x, tab_y, title_x, title_y, title):
    x = np.array(tab_x)
    y = np.array(tab_y)
    plt.ylabel(title_y)
    plt.xlabel(title_x)
    plt.title(title)
    plt.plot(x, y)
    plt.show()

# Affiche un graphe avec des points
def save_graph_plot(tab_x, tab_y, title_x, title_y, title, name_file):
    x = np.array(tab_x)
    y = np.array(tab_y)
    plt.ylabel(title_y)
    plt.xlabel(title_x)
    plt.title(title)
    plt.plot(x, y)
    plt.savefig(name_file)
    plt.clf()

# Affiche plusieurs graphes sur le même graphe
def show_multi_graph_plot(tab_x, tab_y, title_x, title_y, title):
    x = np.array(tab_x)
    for i in range(0, len(tab_y)):
        y = np.array(tab_y[i])
        plt.plot(x, y, label=('i=' + str(i)))
    plt.ylabel(title_y)
    plt.xlabel(title_x)
    plt.title(title)
    plt.legend()
    plt.show()
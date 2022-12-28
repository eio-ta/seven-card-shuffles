import sys
sys.path.append('../')

from utils import *

## FONCTIONS AUXILAIRES  ##########################################################



## PARTIE 1  ######################################################################

# Applique une k-insertion sur un paquet
# k est choisi aléatoirement
def k_insertion(paquet, taille_paquet):
    k = random.randint(0, taille_paquet-1)
    dessus = paquet[0]
    paquet.pop(0)
    paquet.insert(k, dessus)
    return paquet

# Applique une k-insertion i fois sur un paquet
def k_insertion_multiple(paquet, taille_paquet, i):
    if(i <= 0):
        return paquet
    while(i > 0):
        paquet = k_insertion(paquet, taille_paquet)
        i -= 1
    return paquet

# Retourne le temps entre deux remontées
def get_time(paquet, taille_paquet, indice):
    tmp = 0
    if(paquet[indice] == taille_paquet):
        paquet = k_insertion(paquet, taille_paquet)
        tmp += 1
        paquet, tmp2 = get_time(paquet, taille_paquet, indice)
        return paquet, tmp + tmp2
    else:
        return paquet, tmp

# Retourne le tableau des temps
def construction_simulation(taille_paquet):
    paquet = construction_paquet(taille_paquet)
    tmp = [0]
    indice = taille_paquet-1
    while(paquet[0] != taille_paquet):
        paquet, time = get_time(paquet, taille_paquet, indice)
        tmp.append(time)
        indice = get_indice(paquet, taille_paquet)
    return paquet, tmp

# Crée NB_SIMULATIONS simulations
def construction_simulation_forte(taille_paquet, temps_i):
    avg = []
    for i in range(NB_SIMULATIONS):
        paquet, simulation = construction_simulation(taille_paquet)
        avg.append(simulation[temps_i])
    return avg

# Construit une simulation pour l'espérance de T
def simulation_esperance_T(taille_paquet):
    T_possible = []
    for i in range(0, NB_SIMULATIONS):
        paquet, val = construction_simulation(taille_paquet)
        paquet = k_insertion(paquet, taille_paquet)
        somme_T = 0
        for i in range(0, len(val)):
            somme_T += val[i]
        T_possible += [somme_T]
    return T_possible



## PARTIE 2  ######################################################################

# Construit une simulation pour la loi Xn
def simulation_loi_Xn(taille_paquet, k_indice):
    etat_possible = []
    nombre_etat_recu = []
    for i in range(0, NB_SIMULATIONS):
        paquet = construction_paquet(taille_paquet)
        paquet = k_insertion_multiple(paquet, taille_paquet, k_indice)
        if paquet not in etat_possible:
            etat_possible += [paquet]
            nombre_etat_recu += [1]
        else:
            i = etat_possible.index(paquet)
            nombre_etat_recu[i] = nombre_etat_recu[i] + 1
    
    for i in range(0, len(nombre_etat_recu)):
        nombre_etat_recu[i] = (1 * nombre_etat_recu[i]) / NB_SIMULATIONS

    return etat_possible, nombre_etat_recu

# Simulation de la mesure invariante X
def simulation_mesure_invarianteX(tab_val, taille_paquet):
    res = 0
    f = factor(taille_paquet)
    for i in range(0, len(tab_val)):
        res += abs(tab_val[i]-(1/f))
    return res/2



## PARTIE 3  ######################################################################

# Construction d'une simulation pour la loi Yn
def simulation_loi_Yn(taille_paquet, n, k_indice):
    indice_possible = []
    nombre_etat_recu = []
    for i in range(0, NB_SIMULATIONS):
        paquet = construction_paquet(taille_paquet)
        paquet = k_insertion_multiple(paquet, taille_paquet, n)
        indice_eu = paquet.index(k_indice)
        
        if indice_eu not in indice_possible:
            indice_possible += [indice_eu]
            nombre_etat_recu += [1]
        else:
            i = indice_possible.index(indice_eu)
            nombre_etat_recu[i] = nombre_etat_recu[i] + 1
    
    for i in range(0, len(nombre_etat_recu)):
        nombre_etat_recu[i] = (1 * nombre_etat_recu[i]) / NB_SIMULATIONS
    
    return indice_possible, nombre_etat_recu

# Simulation de la mesure invariante Y
def simulation_mesure_invarianteY(tab_val, taille_paquet):
    res = 0
    for i in range(0, len(tab_val)):
        res += abs(tab_val[i]-(1/taille_paquet))
    return res/2



##   MAIN   #######################################################################


# Affiche un message d'aide
def print_help():
    print("Pour exécuter le fichier :")
    print("Commande sous la forme: \"-taille [CHIFFRE] -temps [CHIFFRE] [ARGS]\"")

    print("\nInformations sur les arguments :\n")
    print("\"-taille\" : pour spécifier la taille du paquet de cartes")
    print("\"-temps\" : pour spécifier le temps entre deux remontées")
    
    print("\"-esperance\" : pour afficher l'espérance de T")
    print("\"-mesureX\" : pour afficher la mesure invariante de la loi X_n (*)")
    print("\"-mesureY\" : pour afficher la mesure invariante de la loi Y_n (**)")

    print("\"-h\" pour afficher ce message d'aide\n")

    print("(*) et (**) sont deux lois qui sont expliquées dans le README.md.")


# Fonction MAIN
def main(argv):
    if(len(argv) == 0):
        print_help()
    else:
        taille_paquet = 0
        temps_i = -1

        for i in range(0, len(argv)):
            if(argv[i] == "-h"):
                print_help()
                return
            elif(argv[i] == "-taille"):
                taille_paquet = int(argv[i+1])
            elif(argv[i] == "-temps"):
                temps_i = int(argv[i+1])
            elif(argv[i] == "-esperance"):
                etat = simulation_esperance_T(taille_paquet)

                # Calcul de la proba avec la formule :
                # ETAT_1 * PROBA_1 + ETAT_2 * PROBA_2 + ... + ETAT_N * PROBA_N
                etat_tmp, nbr = get_occurence(etat)
                esperance = 0
                for i in range(0, len(etat_tmp)):
                    esperance += etat_tmp[i] * nbr[i]
                print("Espérance : ", esperance)

                show_graph_hist(etat, 'T', 'Nombre de simulations', 'Nombre de simulations en fonction de T')
                return

            elif(argv[i] == "-mesureX"):
                res = []
                # i = nombre d'inversions
                for i in range(0, NB_INSERTIONS):
                    permutations, probabilites = simulation_loi_Xn(taille_paquet, i)
                    nombre_permutations_0 = factor(taille_paquet) - len(permutations)
                    if(nombre_permutations_0 != 0):
                        for j in range(0, nombre_permutations_0):
                            probabilites.append(0)
                    calcul = simulation_mesure_invarianteX(probabilites, taille_paquet)
                    res.append(calcul)
                    print(calcul)

                show_graph_plot(list(range(0, NB_INSERTIONS)), res, 'n insertion(s)', 'Distance', 'Distance entre la loi P_n et la loi uniforme en fonction de n')
                return

            elif(argv[i] == "-mesureY"):
                # i = position de la carte souhaitée
                res_total = []
                for i in range(1, taille_paquet+1):
                    res = []
                    # n = nombre d'inversions
                    for n in range(0, NB_INSERTIONS):
                        etat, nombre_indice = simulation_loi_Yn(taille_paquet, n, i)
                        for j in range(len(nombre_indice), taille_paquet):
                            nombre_indice.append(0)
                        calcul = simulation_mesure_invarianteY(nombre_indice, taille_paquet)
                        res.append(calcul)
                        print(res)
                    res_total.append(res)

                show_multi_graph_plot(list(range(0, NB_INSERTIONS)), res_total, 'n insertions', 'Distance', 'Distance entre la loi Q_n et la loi uniforme en fonction de n')
                return


        if(temps_i != -1):
            avg = construction_simulation_forte(taille_paquet, temps_i)
            show_graph_hist(avg, 'Nombre de remontées nécessaires', 'Nombre de simulation', 'Histogramme T_' + str(temps_i) + ' pour R = ' + str(taille_paquet))
        else:
            for i in range(0, taille_paquet):
                temps_i = i
                avg = construction_simulation_forte(taille_paquet, temps_i)

                save_graph_hist(avg, 'Nombre de remontées nécessaires', 'Nombre de simulation', 'Histogramme T_' + str(temps_i) + ' pour R = ' + str(taille_paquet), './simulations/' + str(taille_paquet) +"/T_" + str(temps_i))


if __name__ == "__main__":
   main(sys.argv[1:])
import sys
sys.path.append('../')

from utils import *

## FONCTIONS AUXILAIRES  ##########################################################


## PARTIE 1  ######################################################################

# Simule le mélange "riffle-shuffle"
def riffle_shuffle(paquet, taille_paquet):
    m = random.randint(0, taille_paquet-1)
    paquet_1, paquet_2 = paquet[:m], paquet[m:]
    res = []
    while(len(paquet_1)>0 and len(paquet_2)):
        r = random.randint(0,1)
        if(r == 0):
            res.insert(0, paquet_1.pop())
        else:
            res.insert(0, paquet_2.pop())
    if(len(paquet_1)>0):
        for i in range(len(paquet_1)):
            res.insert(0, paquet_1.pop())
    else:
        for i in range(len(paquet_2)):
            res.insert(0, paquet_2.pop())
    return res

# Simule le mélange de la partie 2 (celui avec la loi de Bernouilli)
def melange_inverse(paquet, n):
    bernouilli = []
    for i in range(n):
        bernouilli.append(random.randint(0, 1))
    
    res0 = []
    res1 = []
    for i in range(n):
        if(bernouilli[i] == 0):
            res0.append(paquet[i])
        else:
            res1.append(paquet[i])
    
    return res0 + res1



## PARTIE 3 A  ######################################################################

# Applique un riffle-shuffle i fois sur un paquet
def riffle_shuffle_multiple(paquet, taille_paquet, i):
    if(i <= 0):
        return paquet
    while(i > 0):
        paquet = riffle_shuffle(paquet, taille_paquet)
        i -= 1
    return paquet

# Construit une simulation pour la loi Xn
def simulation_loi_Xn(taille_paquet, n):
    etat_possible = []
    nombre_etat_recu = []
    for i in range(NB_SIMULATIONS):
        paquet = construction_paquet(taille_paquet)
        paquet = riffle_shuffle_multiple(paquet, taille_paquet, n)
        if paquet not in etat_possible:
            etat_possible += [paquet]
            nombre_etat_recu += [1]
        else:
            tmp = etat_possible.index(paquet)
            nombre_etat_recu[tmp] += 1

    for i in range(0, len(nombre_etat_recu)):
        nombre_etat_recu[i] = (1 * nombre_etat_recu[i]) / NB_SIMULATIONS

    return etat_possible, nombre_etat_recu

# Simulation de la mesure invariante X
def simulation_mesure_invarianteX(tab_val, taille_paquet):
    res = 0
    for i in range(0, len(tab_val)):
        res += abs(tab_val[i]-(1/factor(taille_paquet)))
    return res/2



## PARTIE 3 B  ######################################################################

# Applique un mélange de Bernouilli k fois sur un paquet
def melange_inverse_multiple(paquet, n, k):
    if(k <= 0):
        return paquet
    while(k > 0):
        paquet = melange_inverse(paquet, n)
        k -= 1
    return paquet

# Construit une simulation pour la loi Xn
def melange_inverse_proba(n, k):
    etat = []
    proba = []
    for j in range(10000):
        # Construction d'un jeu de taille n
        paquet = construction_paquet(n)
        # Applique k fois la distribution inverse 
        paquet = melange_inverse_multiple(paquet, n, k)
        if paquet not in etat:
            etat += [paquet]
            proba += [1]
        else:
            # Indice du paquet dans le tableau etat
            tmp = etat.index(paquet)
            proba[tmp] += 1

    for i in range(0, len(proba)):
        proba[i] = proba[i] / 10000

    return etat, proba



## PARTIE 4  ######################################################################

def eulerian(n, r):
    if(r == 1): return 1
    cal1 = pow(r, n)
    sum = 0
    for j in range(1, r):
        sum += math.comb(n+r-j, n) * eulerian(n, j)
    return cal1 - sum

# Calcule la distance entre la loi X_n et la loi uniforme avec la formule
def simulation_P_n_bis(n, k, euler):
    res = 0
    for r in range(1, n+1):
        calcul1 = math.comb(pow(2, k)+n-r, n)
        calcul2 = calcul1/pow(2, n*k)
        calcul3 = euler[r-1] * abs(calcul2 - 1/factor(52))
        res += calcul3
    return res / 2


##   MAIN   #######################################################################

# Affiche un message d'aide
def print_help():
    print("Pour exécuter le fichier :")
    print("Commande sous la forme: \"-taille [CHIFFRE] [ARGS]\"")

    print("\nInformations sur les arguments :\n")
    print("\"-taille\" : pour spécifier la taille du paquet de cartes")
    
    print("\"-mesureX\" : pour afficher la mesure invariante de la loi X_n (*)")
    print("\"-mesureXFormula\" : pour afficher la mesure invariante de la loi X_n avec la formule (*)")
    print("\"-mesureY\" : pour afficher la mesure invariante de la loi Y_n (**)")

    print("\"-h\" pour afficher ce message d'aide\n")

    print("(*) et (**) sont deux lois qui sont expliquées dans le README.md.")

# Fonction MAIN
def main(argv):
    if(len(argv) == 0):
        print_help()
    else:
        taille_paquet = 0

        for i in range(0, len(argv)):
            if(argv[i] == "-h"):
                print_help()
                return
            elif(argv[i] == "-taille"):
                taille_paquet = int(argv[i+1])
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
                    print(calcul)
                    res.append(calcul)

                show_graph_plot(list(range(0, NB_INSERTIONS)), res, 'n mélange(s)', 'Distance', 'Distance entre la loi X_n et la loi uniforme en fonction de n')
                return
            elif(argv[i] == "-mesureY"):
                res = []
                for k in range(0, NB_INSERTIONS):
                    permu, proba = melange_inverse_proba(taille_paquet, k)
                    nombre_permu_0 = factor(taille_paquet) - len(permu)
                    if(nombre_permu_0 != 0):
                        for j in range(0, nombre_permu_0):
                            proba.append(0)
                    calcul = simulation_mesure_invarianteX(proba, taille_paquet)
                    print(k, calcul)
                    res.append(calcul)

                show_graph_plot(list(range(0, NB_INSERTIONS)), res, 'k mélange(s)', 'Distance', 'Distance entre la loi Y_n et la loi uniforme en fonction de k')
                return
            elif(argv[i] == "-mesureXFormula"):

                euler52 = [1, 4503599627370443, 6461081650535893048297331, 20282067166317747370548924397305, 2219371090444690280167825067011163404,  28980470297130316118851707371113927682308, 86585645711842456879259291396042785694734772, 86713283824808603371563209439361605206738793756, 37025109959688438829553523840364680262742546084490, 7911300235037463075597685089436522698036110779652974, 945840628557918451844218451393465611283022070265930318, 68592119011285455655624013113555233530495826611028105002, 3204605114791094679078453140281792404372059654677564605036, 101000927132657645557134474918099624296907772735089756696100, 2226078789301170911355122880657959428046783979202356910922164, 35302220045338224161235549913989821979876198108712965566590748, 412144632644776097452355282034303085724026998555266406163630407, 3608546499010535175417741799325030679058798554326570866008941901, 24054768032110205230512644571794784352350441257804171198293416085, 123593420813766502721516289401928881854407236400906448620933407519, 494370080113784916965652571921550916631682778978495688799726045528, 1551899076473182499091355855486075911167554010721759160922095067592, 3847618416911169544019658581651153304367757477493818759690300816296, 7571078104391482024576639988655575870087426063556289226755049718520, 11865899443920844006901893126784362875996540301956583552457431915244, 14846515951110031480154418176050166110124588078969987359444606014756, 14846515951110031480154418176050166110124588078969987359444606014756, 11865899443920844006901893126784362875996540301956583552457431915244, 7571078104391482024576639988655575870087426063556289226755049718520, 3847618416911169544019658581651153304367757477493818759690300816296, 1551899076473182499091355855486075911167554010721759160922095067592, 494370080113784916965652571921550916631682778978495688799726045528, 123593420813766502721516289401928881854407236400906448620933407519, 24054768032110205230512644571794784352350441257804171198293416085, 3608546499010535175417741799325030679058798554326570866008941901, 412144632644776097452355282034303085724026998555266406163630407, 35302220045338224161235549913989821979876198108712965566590748, 2226078789301170911355122880657959428046783979202356910922164, 101000927132657645557134474918099624296907772735089756696100, 3204605114791094679078453140281792404372059654677564605036, 68592119011285455655624013113555233530495826611028105002, 945840628557918451844218451393465611283022070265930318, 7911300235037463075597685089436522698036110779652974, 37025109959688438829553523840364680262742546084490, 86713283824808603371563209439361605206738793756, 86585645711842456879259291396042785694734772, 28980470297130316118851707371113927682308, 2219371090444690280167825067011163404, 20282067166317747370548924397305, 6461081650535893048297331, 4503599627370443, 1]

                res = []
                for k in (range(1, NB_INSERTIONS)):
                    calcul = simulation_P_n_bis(52, k, euler52)
                    print(k, calcul)
                    res.append(calcul)

                show_graph_plot(list(range(1, NB_INSERTIONS)), res, 'n mélange(s)', 'Distance', '')
                return



if __name__ == "__main__":
   main(sys.argv[1:])
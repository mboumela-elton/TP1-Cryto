import matplotlib.pyplot as plt
import numpy as np
import string

def charger_frequences_ressource(fichier):
    frequences = {}
    with open(fichier, 'r') as f:
        for ligne in f:
            parts = ligne.strip().split()
            if len(parts) == 2:
                lettre = parts[0].upper()  # mise en majuscule pour uniformité
                freq_str = parts[1].replace(',', '.').replace('%','')
                try:
                    freq = float(freq_str)
                    frequences[lettre] = freq
                except ValueError:
                    pass
    return frequences

# Chargement des fréquences de la ressource
frequences_ressource = charger_frequences_ressource("Ressource_Exo3.txt")

# Lecture du texte
with open("Exo3.txt", "r") as f:
    texte = f.read().replace('\n', '').upper()  # mise en majuscule pour uniformité

taille_bloc = 7
blocs = [texte[i:i+taille_bloc] for i in range(0, len(texte), taille_bloc)]

alphabet = list(string.ascii_uppercase)

for i in range(taille_bloc):
    # Initialiser les fréquences avec 0 pour toutes les lettres
    frequences = {lettre: 0 for lettre in alphabet}

    for bloc in blocs:
        if i < len(bloc):
            lettre = bloc[i]
            if lettre in frequences:
                frequences[lettre] += 1

    lettres_bloc = alphabet
    counts_bloc = [frequences[lettre] for lettre in lettres_bloc]
    counts_ressource = [frequences_ressource.get(lettre, 0) for lettre in lettres_bloc]

    x = np.arange(len(lettres_bloc))
    width = 0.4  # largeur des barres

    plt.figure(figsize=(12, 6))
    plt.bar(x - width/2, counts_bloc, width, label="Occurrences dans blocs")
    plt.bar(x + width/2, counts_ressource, width, label="Fréquences Ressource_Exo3")

    plt.ylabel('Nombre / Fréquence (%)')
    plt.xlabel('Lettre')
    plt.title(f'Fréquence des lettres à la position {i+1} dans les blocs de taille {taille_bloc}')
    plt.xticks(ticks=x, labels=lettres_bloc)
    plt.legend()
    plt.show()

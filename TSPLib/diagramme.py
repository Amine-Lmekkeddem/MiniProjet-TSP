import matplotlib.pyplot as plt
import numpy as np

# Données expérimentales
n = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45])
distance = np.array([741, 775, 821, 956, 883, 967, 1101, 1118, 1124])
cpu_time = np.array([0.05, 0.25, 0.08, 63.19, 3944.45, 29.81, 13759.23, 19.39, 8.94])

# plt.figure()
# plt.plot(n, distance, marker='o')
# plt.xlabel("Nombre de villes (n)")
# plt.ylabel("Distance totale")
# plt.title("Distance totale du TSP en fonction de la taille de l’instance")
# plt.grid(True)
# plt.show()

# Graphique 1 : Distance totale en fonction du nombre de villes
plt.figure()
plt.bar(n, distance)
plt.xlabel("Nombre de villes (n)")
plt.ylabel("Distance totale")
plt.title("Distance totale du TSP par taille d’instance")
plt.grid(axis="y")
plt.show()

# Graphique 2 : Temps CPU en fonction du nombre de villes
plt.figure()
plt.plot(n, cpu_time, marker='o')
plt.yscale("log")
plt.xlabel("Nombre de villes (n)")
plt.ylabel("Temps CPU (secondes, échelle logarithmique)")
plt.title("Temps CPU du modèle MTZ en fonction de la taille")
plt.grid(True, which="both")
plt.show()


# Tp 1 : Ex4 et Exo5

# Graphique : Temps CPU de résolution du TSP (MTZ vs SSB)
methods = ["MTZ (29)","SSB (29)","MTZ (51)","SSB (51)"]
times = [0.86, 3.22, 2.83, 3880.66]

plt.barh(methods, times, color=["blue","orange","blue","orange"])
plt.xlabel("Temps CPU (s)")
plt.title("Comparaison MTZ vs SSB")
plt.xscale("log")  
plt.show()

import random
import os
import math
import numpy as np

def generate_tsp(n, filename):
    coords = {}

    with open(filename, "w") as f:
        f.write(f"NAME: tsp_{n}\n")
        f.write("TYPE: TSP\n")
        f.write(f"DIMENSION: {n}\n")
        f.write("EDGE_WEIGHT_TYPE: EUC_2D\n")
        f.write("NODE_COORD_SECTION\n")

        for i in range(1, n + 1):
            x = random.randint(0, 100)
            y = random.randint(0, 400)
            coords[i] = (x, y)
            f.write(f"{i} {x} {y}\n")

        f.write("EOF\n")

    return coords


def distance_matrix(coords):
    n = len(coords)
    D = np.zeros((n, n), dtype=int)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            xi, yi = coords[i]
            xj, yj = coords[j]
            D[i-1, j-1] = round(math.sqrt((xi - xj)**2 + (yi - yj)**2))

    return D


# tailles demandées
instances = [5, 10, 15, 20, 25, 30, 35, 40, 45]

os.makedirs("instances", exist_ok=True)

for n in instances:
    coords = generate_tsp(n, f"instances/tsp_{n}.tsp")
    D = distance_matrix(coords)

    # sauvegarde optionnelle de la matrice
    np.savetxt(f"instances/dist_matrix_{n}.csv", D, delimiter=",", fmt="%d")

print("✅ Instances .tsp et matrices de distances générées")


def save_dat(D, filename):
    n = D.shape[0]
    with open(filename, "w") as f:
        f.write(f"n = {n};\n")
        f.write("D = [\n")
        for row in D:
            f.write("  [" + ", ".join(map(str, row)) + "],\n")
        f.write("];\n")

for n in instances:
    D = np.loadtxt(f"instances/dist_matrix_{n}.csv", delimiter=",", dtype=float)
    save_dat(D, f"instances/tsp_{n}.dat")

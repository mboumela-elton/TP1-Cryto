import sys
import re
from collections import defaultdict, Counter
from math import gcd
from functools import reduce

DEFAULT_PATH = "/home/tom/Crypto/Exo3.txt"

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def find_repeated_sequences(text, min_len=3, max_len=6):
    positions = defaultdict(list)
    n = len(text)
    for L in range(min_len, max_len + 1):
        for i in range(n - L + 1):
            seq = text[i:i+L]
            positions[seq].append(i)
    return {s: pos for s, pos in positions.items() if len(pos) > 1}

def distances_from_positions(positions):
    dists = []
    for pos in positions:
        for i in range(1, len(pos)):
            dists.append(pos[i] - pos[i-1])
    return dists

def all_pair_distances(positions):
    dists = []
    for pos in positions:
        m = len(pos)
        for i in range(m):
            for j in range(i+1, m):
                dists.append(pos[j] - pos[i])
    return dists

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1 if i == 2 else 2 
    if n > 1:
        factors.append(n)
    return factors

def factor_counts_for_distances(distances, max_factor=40):
    cnt = Counter()
    for d in distances:
        for f in range(2, min(max_factor, d) + 1):
            if d % f == 0:
                cnt[f] += 1
    return cnt

def gcd_of_list(lst):
    if not lst:
        return 0
    return reduce(gcd, lst)

def kasiski(filepath):
    text = load_text(filepath)
    print(f"Texte normalisé: {len(text)} lettres")
    reps = find_repeated_sequences(text, min_len=3, max_len=6)
    print(f"Séquences répétées trouvées: {len(reps)} (longueurs 3..6)")

    all_dists = []
    seq_gcds = {}
    for seq, pos in reps.items():
        pos_sorted = sorted(pos)
        dists = all_pair_distances([pos_sorted])
        if not dists:
            continue
        g = gcd_of_list(dists)
        seq_gcds[seq] = (g, dists)
        all_dists.extend(dists)

    if not all_dists:
        print("Aucune distance calculée — texte peut être trop court ou pas de répétitions utiles.")
        return

    factor_counts = factor_counts_for_distances(all_dists, max_factor=40)
    most_common = factor_counts.most_common()

    print("\nFacteurs candidats (diviseurs des distances) triés par fréquence:")
    for f, c in most_common[:20]:
        print(f"  longueur possible = {f:2d} : {c} occurrences")

    print("\nQuelques gcds par séquence répétée (séquences avec gcd>1):")
    shown = 0
    for seq, (g, dists) in sorted(seq_gcds.items(), key=lambda x: (-x[1][0], -len(x[1][1]))) :
        if g > 1:
            print(f"  '{seq}' -> gcd={g}, distances={dists[:10]}{'...' if len(dists)>10 else ''}")
            shown += 1
            if shown >= 10:
                break

    suggestions = [f for f, _ in most_common if f > 1][:5]
    print("\nSuggestions de longueurs de clé (top 5):", suggestions)

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PATH
    kasiski(path)
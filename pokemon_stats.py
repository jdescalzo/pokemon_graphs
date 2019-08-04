# -*- coding: utf-8 -*-
"""
Pokemon Stats

"""
import matplotlib.pyplot as plt
import csv

filename = 'pokemon.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, header_column in enumerate(header_row):
        print(index, header_column)

    # Stats Lists
    attacks, sp_attacks = [], []
    for row in reader:
        try:
            pokemon_attack = int(row[9])
            pokemon_sp_attack = int(row[12])
        except ValueError:
            print(row[1], 'Missing Stat')
        else:
            attacks.append(pokemon_attack)
            sp_attacks.append(pokemon_sp_attack)
            
    # Avarages
    avarage_attack = sum(attacks)/len(attacks)
    avarage_sp_attack =sum(sp_attacks)/len(sp_attacks)

# Plot Stats
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.scatter(attacks, sp_attacks, s=10, edgecolor='none')
plt.axvline(avarage_attack, c='red', alpha=0.5)
plt.axhline(avarage_sp_attack, c='orange', alpha=0.5)
plt.plot([0, 200], [0, 200], label='Attacks are the same')
plt.legend()

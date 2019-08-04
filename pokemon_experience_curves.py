# -*- coding: utf-8 -*-
"""

Pokemon Experience Curves

"""

import matplotlib.pyplot as plt

# Fast Curve
fast_exp = []
for level in range(101):
    level_exp = ((4*level**3)/5)
    fast_exp.append(level_exp)

# Medium Fast Curve
medium_fast_exp = []
for level in range(101):
    level_exp = level**3
    medium_fast_exp.append(level_exp)

# Medium Slow Curve
medium_slow_exp = []
for level in range(101):
    level_exp = (6/5*level**3)-(15*level**2)+(100*level)-140
    medium_slow_exp.append(level_exp)

# Slow Curve
slow_exp = []
for level in range(101):
    level_exp = (5*level**3)/4
    slow_exp.append(level_exp)

# Fluctuating Curve
fluctuating_exp = []
for level in range(101):
    if level <= 15:
        level_exp = level**3*((((level+1)/3)+24)/50)
        fluctuating_exp.append(level_exp)
    elif level >= 15 and level <= 36:
        level_exp = level**3*((level+14)/50)
        fluctuating_exp.append(level_exp)
    else:
        level_exp = level**3*(((level/2)+32)/50)
        fluctuating_exp.append(level_exp)

# Erratic Curve
# --TO DO--

# Plot Experience Curves
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(fast_exp, c='red', label='Fast')
plt.plot(medium_fast_exp, c='orange', label='Medium Fast')
plt.plot(medium_slow_exp, c='green', label='Medium Slow')
plt.plot(slow_exp, c='blue', label='Slow')
plt.plot(fluctuating_exp, c='black', label='Fluctuating')

# Plot Reference Lines
plt.axhline(fast_exp[-1], c='red', alpha=0.25, xmax=0.95)
plt.axhline(medium_fast_exp[-1], c='orange', alpha=0.25, xmax=0.95)
plt.axhline(medium_slow_exp[-1], c='green', alpha=0.25, xmax=0.95)
plt.axhline(slow_exp[-1], c='blue', alpha=0.25, xmax=0.95)
plt.axhline(fluctuating_exp[-1], c='black', alpha=0.25, xmax=0.95)
plt.axvline(100, c='grey', alpha=0.25, ymax=0.95)

# Plot Parameters
plt.title('Pokémon Experience Curves', fontsize=24)
plt.xlabel('Level', fontsize=18)
plt.ylabel('Experience needed', fontsize=18)
plt.tick_params(axis='x', labelsize=16)
plt.xticks(list(range(0, 101, 10)))
plt.legend()

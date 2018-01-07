# Dota2 Recommendation Engine
I've been playing DOTA for past 6 years, as a not-so regular player i've spent more than 2k hours in playing the game. What attracted me to DOTA was not it's UI or the after effects,but the gameplay and challenging rivals. Dota 2 is one of the games that falls in the categories of strategic,complex and RPG with difficulty in the both vs. world and vs. AI

Dota 2 Recommendation engine based on heroes chosen , recommend what heroes to ban based on a user played with hero 'X' had lost the matches against hero 'Y'

DOTA Engine allows an ally in the team suggest what hero to choose/ban in the nomination phase manually. Our recommendation engine tries to answer if the algorithm for 5th position can suggest the hero if all other position are chosen/banned.

We take into consideration the team composition of the Opponent and your team, and the algorithm using K-means suggests one from the 2 categories (CARRY/SUPPORT) and one from the 7 subcategories considering the best chances to win. Only the category is suggested not the HERO.

Build in Python3 using Scikit-learn, Valve API, Flask
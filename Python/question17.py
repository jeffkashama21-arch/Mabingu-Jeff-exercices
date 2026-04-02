
phrase = input("Entrez une phrase : ")

phrase = phrase.lower()

mots = phrase.split()

nb_mots = len(mots)
print("Nombre total de mots :", nb_mots)

mot_plus_long = max(mots, key=len)
print("Mot le plus long :", mot_plus_long)

frequence = {}

for mot in mots:
    if mot in frequence:
        frequence[mot] += 1
    else:
        frequence[mot] = 1

print("Occurrences des mots :")
for mot, count in frequence.items():
    print(f"{mot} : {count}")

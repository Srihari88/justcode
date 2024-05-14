import random

greetings=['Hello','Hi','Hey','Hello','Hello Hi']

value=random.choice(greetings)

print(value + ' Srihari')


colours=['Red','Green','Blue']

results=random.choices(colours,weights=[18,12,1],k=10)
print(results)
from collections import defaultdict
from matplotlib import pyplot as plt


salaries_and_tenures = [ (3300, 1.0), (3500,2.0), (5000, 3.0), (12500, 10.0), (1500, 0), (10000, 9.5) 
						]

# o indice são os anos, os valores são as lsitas dos salários para cada ano

salary_por_tempo = defaultdict(list)

for salario, tempo in salaries_and_tenures:
	salary_por_tempo[tempo].append(salario)
	
	
# o indice são os anos, cada valor é a média salarial para aquele ano
average_salario_por_tempo = {
							ternure: sum(salaries) / len(salaries)
							for ternure, salaries in salary_por_tempo.items()
							}
							

list_order = sorted(average_salario_por_tempo.items(), key=lambda a:a[1])

list_2_dict = {item: valor for item, valor in list_order}

print(average_salario_por_tempo)

media = sum(average_salario_por_tempo.values())
media = media / len(average_salario_por_tempo)

media_2 = sum(average_salario_por_tempo.keys())
media_2 = media_2 / len(average_salario_por_tempo)

pl_media = []
pl_media.append(media)

pl_media2 = []
pl_media2.append(media_2)


plt.plot(list_2_dict.keys(), list_2_dict.values(), color='green', marker='o', linestyle='solid')
plt.plot(pl_media2, pl_media, color='blue', marker='o', linestyle='solid')

#plt.plot(list_order[0], list_order[1], color='green', marker='o', linestyle='solid')

plt.title("Analista de sistemas - salario")

plt.ylabel("Salários")
plt.xlabel("Anos de experiencia")
plt.show()

# mediana 

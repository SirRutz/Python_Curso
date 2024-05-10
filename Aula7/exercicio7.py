# Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes

filmes = {}
filmes2 = {'Vingadores: Guerra Infinita':{'Thanos',2018}, 'Star Wars: O Império Contra-Ataca':{'Darth Vader',1980}, 'Star Wars: A Vingança dos Sith':{'Darth Sidious',2005}, 'Homem-Aranha: Através do Aranhaverso':{'Homem-Aranha 2099',2023}, 'Avatar: O Caminho da Água':{'Coronel Miles Quaritch',2022}}

filmes.update(filmes2)

for items, keys in filmes.items():
    print(f'{items} - {keys}')
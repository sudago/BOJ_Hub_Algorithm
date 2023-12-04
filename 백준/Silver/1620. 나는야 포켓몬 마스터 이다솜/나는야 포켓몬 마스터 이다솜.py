from sys import stdin as s

n, m = list(map(int, s.readline().split()))
pokemons_dict = { "0":0 }
pokemons_list = []

for i in range(1, n+1):
    pokemon = s.readline().rstrip()
    pokemons_dict[pokemon] = i

pokemons_list = list(pokemons_dict.keys())
for _ in range(m):
    quest = s.readline().rstrip()
    if quest.isdecimal(): # 번호면
        quest = int(quest)
        print(pokemons_list[quest])
    else: # 포켓몬 이름이면
        print(pokemons_dict[quest])
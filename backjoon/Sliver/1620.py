# 실버4
# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
DP = dict()

for i in range(1, N+1):
    name = input().strip()
    DP[str(i)] = name
    DP[name] = str(i)

for _ in range(M):
    print(DP[input().strip()])


'''
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
'''



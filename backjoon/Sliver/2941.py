# 실버5
# 크로아티아 알파벳
import sys
import re

input_str = sys.stdin.readline().strip()
croatia_alphabets = {
    "c=" : 0, "c-" : 0, 
    "dz=" : 0, "d-": 0, 
    "lj": 0, "nj": 0, 
    "s=": 0, "z=": 0
}
input_str_len = len(input_str)

for croatia_alphabet in croatia_alphabets:
    st = [i for i in re.finditer(croatia_alphabet, input_str)]
    croatia_alphabets[croatia_alphabet] = len(st)

if croatia_alphabets["dz="] == 0: pass
else: croatia_alphabets["z="] -= croatia_alphabets["dz="]

for croatia_alphabet in croatia_alphabets:
    # 전체 글자수 + (1 - croa알파벳 수)*croa알파벳 포함 수
    input_str_len = input_str_len + (1-len(croatia_alphabet))*croatia_alphabets[croatia_alphabet]

print(input_str_len)

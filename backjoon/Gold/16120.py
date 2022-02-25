# 골드4
# PPAP
S = list(input())
np_check = False
cnt = 0
i = 0
while i<len(S):
    
    if S[i] == 'P': 
        cnt += 1
        i += 1
        continue
    elif cnt >= 2 and i+1 < len(S) and S[i+1] == 'P':
        cnt -= 1
        i += 2
    elif S[i] == 'A': 
        np_check = True
        break

if cnt == 1 and np_check == False: print("PPAP")
else: print("NP")


"""
PPPAPPAPPPAPPAPPPPAPPAPPPAPPAPPAPAPPPAPAPAPAPAPPPAPAPAP
PPPAPPPPPAPPAPPPAPPAPPAPAPPPAPAPAPPPPAPPAPPAPAPPPAPAPAP
PPPAPAP
PPAPAPP
PPAP
PPPA
"""

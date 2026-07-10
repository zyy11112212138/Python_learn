pass_str = ''

def Index_BF(S,T,pos):
    global pass_str
    i = pos
    j = 0
    while i < len(S) and j < len(T):
        pass_str += S[i]
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j >= len(T):
        return i - len(T)
    else:
        return -1;
for i in range(3):
    pass_str = ''
    S,T = input().split()
    res = Index_BF(S, T, 0)
    print(pass_str)
    print(res + 1) if res != -1 else print(0)

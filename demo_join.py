def join(s, d):
    res = ""
    for i in range(len(s)):
        if i == len(s) - 1:
            res = res + str(s[i])
            break
        res = res + str(s[i]) + d
    return res

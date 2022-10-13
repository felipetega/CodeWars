def solution(s):
    str = ""
    for i in range(0, len(s)):
        if s[i].isupper():
            str += " "
            str += s[i]
        else:
            str += s[i]
    return str

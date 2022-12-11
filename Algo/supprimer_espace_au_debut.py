def supp_espace(ch):
    if ch[0] == " ":
        return supp_espace(ch[1:])
    else:
        return ch


print(supp_espace("                 aaa"))

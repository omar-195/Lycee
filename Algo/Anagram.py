def Anagram(ch1, ch2):
    if len(ch1) == 0:
        return True
    elif ch2.find(ch1[0]) == -1:
        return False
    else:
        return Anagram(ch1[1:], ch2[:ch2.find(ch1[0])]+ch2[ch2.find(ch1[0])+1:])


print(Anagram("http", "tthp"))

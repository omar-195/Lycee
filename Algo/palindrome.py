def palindrome(ch, ch2):
    if len(ch2) == len(ch):
        return ch2 == ch
    else:
        return palindrome(ch[:len(ch)-1], ch2 + ch[len(ch)-1])


print(palindrome("SOS", ""))

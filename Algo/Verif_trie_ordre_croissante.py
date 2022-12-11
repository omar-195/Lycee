# Method 1
def verife(ch):
    if len(ch) > 2 and ord(ch[0]) < ord(ch[1]):
        return verife(ch[1:])
    elif len(ch) == 1:
        return True
    else:
        return ord(ch[0]) < ord(ch[1])
# Method 2


def veriff(ch):
    if len(ch) <= 1:
        return True
    elif ord(ch[0]) > ord(ch[1]):
        return False
    else:
        return verife(ch[1:])

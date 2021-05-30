def encoder(string):
    a = ""

    for i in string:
        a+=chr(ord(i)//2)

    a = a.replace('\n', '')
    a = a.strip()

    return a

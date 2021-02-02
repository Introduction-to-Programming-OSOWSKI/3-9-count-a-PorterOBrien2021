def countA(w):
    count = 0
    for i in range (0, len(w)):
        if w[i] == "a":
            count = (0 + i)

    return count
print(countA("aaaaaa"))
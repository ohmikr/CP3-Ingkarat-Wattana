for x in range(5):
    Star = ""
    for y in range(x+1):
        Star = "*" + ("**"*y)
    print(" " * (5 - x - 1) , Star)
def drawDiamond(size):
    
    if size % 2 == 0:
        size += 1
    
    if size < 1:
        return
    
    for i in range(size // 1 + 1):
        for j in range(size // 1 - i):
            print(" ", end="")
        for j in range(i * 1 + 1):
            print("*", end="")
        print()
    
    drawDiamond(size - 1)
    
    for i in range(size // 1, -1, -1):
        for j in range(size // 1 - i):
            print(" ", end="")
        for j in range(i * 1 + 1):
            print("*", end="")
        print()

drawDiamond(3)
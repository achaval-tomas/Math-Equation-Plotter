def power(n, exp):
    res = 1
    for i in range(exp):
        res *= n
    return res

def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def classicLinear():
    return [0, 1]

def classicCuadratic():
    return [0, 0, 1]

def classicCubic():
    return [0, 0, 0, 1]

'''             WELL-KNOWN TAYLOR SERIES             '''

def taylorForSin():
    eq = []
    for i in range(0, 20, 2):
        eq.append(0)
        eq.append(power(-1, int(i/2))/fact(i+1))
    return eq

def taylorForCos():
    eq = []
    for i in range(0, 20, 2):
        eq.append(power(-1, int(i/2))/fact(i))
        eq.append(0)
    return eq

def exponential():
    eq = []
    for i in range(0, 50):
        eq.append(1/fact(i))
    return eq

def naturalLog():
    eq = [1]
    for i in range(1, 20):
        eq.append(power(-1,i+1)/i)
    return eq

def funQuintic():
    return [0, -2/5, 1/8, -2/3, 1/8, 1/5]

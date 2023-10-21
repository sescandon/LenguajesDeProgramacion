memory = [0] * 1024

IC = 0
CP = 0

registerA = 0
registerB = 0
registerC = 0
registerD = 0

C = 0
P = 0
N = 0
D = 0

def AlterC():
    global C
    C = 1
    return

def AlterP():
    global P
    P = 1
    return

def AlterN():
    global N
    N = 1
    return

def AlterD():
    global D
    D = 1
    return

def ResetC():
    global C
    C = 0
    return

def ResetP():
    global P
    P = 0
    return

def ResetN():
    global N
    N = 0
    return

def ResetD():
    global D
    D = 0
    return

def SetCP(M):
    global CP
    CP = M
    return

def AddCP():
    global CP
    CP = CP + 1
    return

def Sumar(reg1, reg2):
    global C
    global P
    global N
    global D

    result = reg1 + reg2
    AlterC() if result == 0 else 0
    AlterP() if result > 0 else 0
    AlterN() if result < 0 else 0
    AlterD() if result > 32767 or result < -32768 else 0
    return result
    
def Restar(reg1, reg2):
    global C
    global P
    global N
    global D
    
    result = reg1 - reg2
    AlterC() if result == 0 else 0
    AlterP() if result > 0 else 0
    AlterN() if result < 0 else 0
    AlterD() if result > 32767 or result < -32768 else 0
    D = 1 if result > 32767 or result < -32768 else 0
    return result
    
def Mult(reg1, reg2):
    global C
    global P
    global N
    global D
    
    result = reg1 * reg2
    AlterC() if result == 0 else 0
    AlterP() if result > 0 else 0
    AlterN() if result < 0 else 0
    AlterD() if result > 32767 or result < -32768 else 0
    return result
    
def Div(reg1, reg2):
    global C
    global P
    global N
    global D
    
    if reg2 == 0:
        raise ValueError("Division by zero")
    result = reg1 // reg2
    rest = reg1 % reg2
    AlterC() if result == 0 else 0
    AlterP() if result > 0 else 0
    AlterN() if result < 0 else 0
    AlterD() if result > 32767 or result < -32768 else 0
    return result, rest 

def Cargar(R,M):
    R = memory[M]
    return R
    
def CargarValor(R,V):
    R = V
    return R

def Almacenar(R,M):
    memory[M] = R
    return 

def SaltarSiCero(M):
    global C
    global CP

    if C == 1:
        CP = M
        C = 0
    else:
        CP = CP + 1
    return CP , C

def SaltarSiNeg(M):
    global N
    global CP

    if N == 1:
        CP = M
        N = 0
    else:
        CP = CP + 1
    return CP , N

def SaltarSiPos(M):
    global P
    global CP

    if P == 1:
        CP = M
        P = 0
    else:
        CP = CP + 1
    return CP , P

def SaltarSiDes(M):
    global D
    global CP

    if D == 1:
        CP = M
        D = 0
    else:
        CP = CP + 1
    return CP , D

def Saltar(M):
    global CP

    CP = M
    return CP

def Copiar(R1,R2):
    R2 = R1
    return R2


registerA = 1
registerB = 2
Sumar(registerA, registerB)
print(C)
print(P)
print(N)
print(D)
Almacenar(registerA, 0)
print(memory[0])
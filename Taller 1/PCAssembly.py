class Memory:
    def __init__(self, size):
        self.size = size - 1
        self.memory = ["CargarValor A,119", "CargarValor B,240", "Copiar A,C", "Restar C,B", "SaltarSiCero 10", "SaltarSiNeg 8", "Restar A,B", "Saltar 2", "Restar B,A", "Saltar 2", "Almacenar A,35", "Parar", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def read(self, address):
        if address < 0 or address >= self.size:
            raise ValueError("Invalid memory address")
        return self.memory[address]
    
    def write(self, address, value):
        if address < 0 or address >= self.size:
            raise ValueError("Invalid memory address")
        if value < -32768 or value > 32767:
            raise ValueError("Invalid value")
        self.memory[address] = value

class Register:
    def __init__(self):
        self.value = 0
    
    def read(self):
        return self.value
    
    def write(self, value):
        if value < -32768 or value > 32767:
            raise ValueError("Invalid value")
        self.value = value

class ICRegister:
    def __init__(self):
        self.value = 0
    
    def read(self):
        return self.value
    
    def write(self, value):
        self.value = value

class ArithmeticUnit:
    def __init__(self):
        self.C = 0
        self.P = 0
        self.N = 0
        self.D = 0
    
    def add(self, reg1, reg2):
        result = reg1.read() + reg2.read()
        self.C = 1 if result == 0 else 0
        self.P = 1 if result > 0 else 0
        self.N = 1 if result < 0 else 0
        self.D = 1 if result > 32767 or result < -32768 else 0
        reg1.write(result)
    
    def sub(self, reg1, reg2):
        result = reg1.read() - reg2.read()
        self.C = 1 if result == 0 else 0
        self.P = 1 if result > 0 else 0
        self.N = 1 if result < 0 else 0
        self.D = 1 if result > 32767 or result < -32768 else 0
        reg1.write(result)
    
    def mul(self, reg1, reg2):
        result = reg1.read() * reg2.read()
        self.C = 1 if result == 0 else 0
        self.P = 1 if result > 0 else 0
        self.N = 1 if result < 0 else 0
        self.D = 1 if result > 32767 or result < -32768 else 0
        reg1.write(result)
    
    def div(self, reg1, reg2):
        if reg2.read() == 0:
            raise ValueError("Division by zero")
        result = reg1.read() // reg2.read()
        rest = reg1.read() % reg2.read()
        self.C = 1 if result == 0 else 0
        self.P = 1 if result > 0 else 0
        self.N = 1 if result < 0 else 0
        self.D = 1 if result > 32767 or result < -32768 else 0
        reg1.write(result)
        reg2.write(rest)

class ControlUnit:
    def __init__(self, Memory,A, B,C,D, ArithmeticUnit):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.IC = ICRegister()
        self.CP = Register()
        self.Memory = Memory
        self.ArithmeticUnit = ArithmeticUnit
        self.running = False
    def run(self):
        while self.running:
            print("CP: " + str(self.CP.read()))
            self.IC.write(self.Memory.read(int(self.CP.read())))
            if self.IC.read() == 0:
                self.running = False
                break
            
            instructionAddress = self.IC.read()
            if instructionAddress == "Parar":
                self.running = False
                break
            readFunction, parameters = self.ParseCommand(instructionAddress)
            if len(parameters) == 2:
                readFunction(parameters[0], parameters[1])
                self.CP.write(self.CP.read() + 1)
            else:
                readFunction(parameters[0])

            print("Ejecutando: " + instructionAddress)

        print("Program has endend")
        print("A: " + str(self.A.read()))
        print("B: " + str(self.B.read()))
        print("C: " + str(self.C.read()))
        print("D: " + str(self.D.read()))
            

    def ParseCommand(self,command):
        # Split the string into its component parts
        parts = command.split()
        
        # Get the method name and parameters from the parts
        method_name = parts[0]
        register_names = parts[1].split(",")
        
        # Get the method from the method name
        readFunction = getattr(self, method_name)
        parameters = []

        if len(register_names) == 1:
            try:
                R = getattr(self, register_names[0])
            except:
                R = int(register_names[0])
            parameters = [R] 
        else:
            R = getattr(self, register_names[0])
            try:
                pR = getattr(self, register_names[1])
            except:
                pR = int(register_names[1])
            parameters = [R,pR]

        # Call the method with the parameters
        return readFunction, parameters
        
    def Cargar(self,R,M):
        R.write(self.memory.read(M))
        return
    
    def CargarValor(self,R,V):
        R.write(V)
        return
    
    def Almacenar(self,R,M):
        self.Memory.write(M,R.read())
        return
    
    def SaltarSiCero(self,M):
        if self.ArithmeticUnit.C == 1:
            self.CP.write(M)
            self.ArithmeticUnit.C = 0
        else:
            self.CP.write(self.CP.read() + 1)
        return
    
    def SaltarSiNeg(self,M):
        if self.ArithmeticUnit.N == 1:
            self.CP.write(M)
            self.ArithmeticUnit.N = 0
        else:
            self.CP.write(self.CP.read() + 1)
        return
    
    def SaltarSiPos(self,M):
        if self.ArithmeticUnit.P == 1:
            self.CP.write(M)
            self.ArithmeticUnit.P = 0
        else:
            self.CP.write(self.CP.read() + 1)
        return
    
    def SaltarSiDes(self,M):
        if self.ArithmeticUnit.D == 1:
            self.CP.write(M)
            self.ArithmeticUnit.D = 0
        else:
            self.CP.write(self.CP.read() + 1)
        return
    
    def Saltar(self,M):
        self.CP.write(M)
        return
    
    def Copiar(self,R1,R2):
        R2.write(R1.read())
        return
    
    def Sumar(self,R1,R2):
        self.ArithmeticUnit.add(R1,R2)
        return
    
    def Restar(self,R1,R2):
        self.ArithmeticUnit.sub(R1,R2)
        return
    
    def Mult(self,R1,R2):
        self.ArithmeticUnit.mul(R1,R2)
        return
    
    def Div(self,R1,R2):
        self.ArithmeticUnit.div(R1,R2)
        return

class AssemblerPC:
    def __init__(self,Memoria, ArithmeticUnit, ControlUnit):
        self.Memoria = Memoria
        self.ArithmeticUnit = ArithmeticUnit
        self.ControlUnit = ControlUnit



Memoria = Memory(1024)
A = Register()
B = Register()
C = Register()
D = Register()
ArithmeticUnit = ArithmeticUnit()
ControlUnit = ControlUnit(Memoria,A,B,C,D,ArithmeticUnit)

AssemblerPC = AssemblerPC(Memoria,ArithmeticUnit,ControlUnit)

AssemblerPC.ControlUnit.running = True
AssemblerPC.ControlUnit.run()
print(AssemblerPC.ControlUnit.Memory.read(35))




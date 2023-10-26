class PCModel:
    def __init__(self):
        self.A = [0]
        self.B = [0]
        self.C = [0]
        self.D = [0]
        self.Cero = 0
        self.Positivo = 0
        self.Negativo = 0
        self.Desborde = 0
        self.prevCP = 0
        self.CP = 0
        self.ALU = self.ALU()

    class ALU:
        def sumar(self, reg1, reg2):
            result = reg1 + reg2
            C = 1 if result == 0 else 0
            P = 1 if result > 0 else 0
            N = 1 if result < 0 else 0
            D = 1 if result > 32767 or result < -32768 else 0
            return result, reg2, C, P, N, D

        def restar(self, reg1, reg2):
            result = reg1 - reg2
            C = 1 if result == 0 else 0
            P = 1 if result > 0 else 0
            N = 1 if result < 0 else 0
            D = 1 if result > 32767 or result < -32768 else 0
            return result, reg2, C, P, N, D

        def mult(self, reg1, reg2):
            result = reg1 * reg2
            C = 1 if result == 0 else 0
            P = 1 if result > 0 else 0
            N = 1 if result < 0 else 0
            D = 1 if result > 32767 or result < -32768 else 0
            return result, reg2, C, P, N, D

        def div(self, reg1, reg2):
            if reg2 == 0:
                raise ValueError("División por cero")
            result = reg1 // reg2
            result2 = reg1 % reg2
            C = 1 if result == 0 else 0
            P = 1 if result > 0 else 0
            N = 1 if result < 0 else 0
            D = 1 if result > 32767 or result < -32768 else 0
            return result, result2 , C, P, N, D

        def ProccessArithmeticUnit(self, action, reg1, reg2):
            try:
                return getattr(self, action.lower())(reg1, reg2)
            except Exception as e:
                raise e
    
    def load(self, program):
        if not program: raise Exception("Programa vacío")
        if not hasattr(program, '__iter__'):
            raise TypeError("El programa no es un iterable (lista o tupla)")
        self.memory = program
        return self

    def run(self):
        self.ProccessControlUnit()


    def SetReg(self, Reg, value):
        Reg[0] = value
        return

    def ProccessControlUnit(self):
        atr = {
            "A": self.A,
            "B": self.B,
            "C": self.C,
            "D": self.D
            }

        while True:
            IC = self.memory[self.CP: self.CP+16]
            command = IC[0]
            if command == "Parar":
                break
            command = command.split()
            instruction = command[0]
            parameters = command[1].split(",")

            if instruction == "Copiar":
                reg1 = getattr(self, parameters[0])[0]
                reg2 = getattr(self, parameters[1])
                self.SetReg(reg2, reg1)

            elif instruction == "CargarValor":
                reg1 = getattr(self, parameters[0])
                reg2 = int(parameters[1])
                self.SetReg(reg1, reg2)

            elif instruction == "Cargar":
                reg1 = getattr(self, parameters[0])
                self.SetReg(reg1, self.memory[int(parameters[1])])

            elif instruction == "Almacenar":
                self.memory[int(parameters[1])] = getattr(self, parameters[0])[0]

            elif instruction == "SaltarSiCero":
                if self.Cero == 1:
                    self.CP = int(parameters[0])
                    self.Cero = 0
                    continue

            elif instruction == "SaltarSiPos":
                if self.Positivo == 1:
                    self.CP = int(parameters[0])
                    self.Positivo = 0
                    continue

            elif instruction == "SaltarSiNeg":
                if self.Negativo == 1:
                    self.CP = int(parameters[0])
                    self.Negativo = 0
                    continue

            elif instruction == "SaltarSiDes":
                if self.Desborde == 1:
                    self.CP = int(parameters[0])
                    self.Desborde = 0
                    continue

            elif instruction == "Saltar":
                self.CP = int(parameters[0])
                continue

            elif instruction in ["Sumar", "Restar", "Mult", "Div"]:
                print(type(parameters), len(parameters), parameters)
                result, reg2, self.Cero, self.Positivo, self.Negativo, self.Desborde = self.ALU.ProccessArithmeticUnit(action=instruction, reg1=atr[parameters[0]][0], reg2=atr[parameters[1][0]][0])
                self.SetReg(getattr(self, parameters[0]), result)
                self.SetReg(getattr(self, parameters[1]), reg2)
            else:
                raise ValueError("Instruction not found", instruction)

            self.CP += 1

        print('A: ', self.A)
        print('B: ', self.B)
        print('C: ', self.C)
        print('D: ', self.D)


memory = ["CargarValor A,119", "CargarValor B,240", "Copiar A,C", "Restar C,B", "SaltarSiCero 10", "SaltarSiNeg 8", "Restar A,B", "Saltar 2", "Restar B,A", "Saltar 2", "Almacenar A,35", "Parar", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

pc = PCModel().load(memory).run()

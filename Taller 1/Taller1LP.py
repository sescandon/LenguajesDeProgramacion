import re

class Token:
    def __init__(self, tipoLexema, linea, columna,lexema=None):
        self.lexema = lexema
        self.tipo = tipoLexema
        self.linea = linea
        self.columna = columna

    def setTipo(self, tipo):
        self.tipo = tipo

    def getLexema(self):
        return self.lexema if self.lexema is not None else self.tipo
    
    def getTipo(self):
        return self.tipo
    
    def setLexema(self, lexema):
        self.lexema = lexema

    def getLinea(self):
        return self.linea
    
    def getColumna(self):
        return self.columna
    
    def __str__(self):
        if self.lexema is not None:
            return "<" + self.tipo + "," + self.lexema + "," + str(self.linea) + "," + str(self.columna) + ">"
        else:
            return "<" + self.tipo + "," + "NaN" + ","+ str(self.linea) + "," + str(self.columna) + ">"
        



palabrasReservadas = [
    "global", "def", "return", "if", "else"
]
simbols = {
    "TokenPunto": "[.]",
    "TokenComa": ",",
    "TokenDosPuntos": ":",
    "TokenRectangularesCierre": "\]", 
    "TokenRectangularesApertura": "\[",
    "TokenParentesisCierre": "[)]",  
    "TokenParentesisAbre": "[(]",
    "TokenMas": "[+]",
    "TokenMenos": r"-",
    "TokenMultiplica": r"[*]",
    "TokenPotencia": r"\^",
    "TokenIgual": "[=]",
    "TokenNoIgual": "<>",
    "TokenMenorIgual": r"<[=]",
    "TokenMenor": "<",
    "TokenMayorIgual": "[>][=]",
    "TokenMayor": ">",
}

division = {
    "TokenDivision": r"/",
    "TokenComentarioSencillo": r"//.*",
    "TokenComentarioMultilinea": "/[*](.|{0})*[*]/".format(r"\n"),
    "TokenIniciaComentarioMultilinea": "/[*]",
    "TokenFinalizaComentarioMultilinea": "[*]/",
}

tokensNoSimbolos = {
    "TokenIdentificador": "[a-zA-Z][a-zA-Z0-9_]*",
    "TokenNumero": r"[0-9]+",
    "TokenCadena": r"\"([^\"\n])*\"",
    "TokenCaracter": r"'([^'\n])*'",
    "TokenEspacios": r"[( \t\r)^\n]+",
    "TokenSaltoLinea": r"\n",
}

def leerArhivo(archivo):
    with open(archivo, 'r') as file:
        return file.read()
    
def guardarToken(arrayTokens, nombre, linea, columna, lexema=None):
    token = Token(nombre, linea, columna)
    if lexema is not None:
        token.setLexema(lexema)
    arrayTokens.append(token)

tokenList = []
comentPosition = []

def getTokens(archivo):
    pointer = 0
    linea = 1
    columna = 1
    enComentario = False
    while(pointer < len(archivo)):
        token = None
        caracter = archivo[pointer]
        if caracter == "\n":
            linea += 1
            pointer += 1
            columna = 1
        elif enComentario:
            if caracter == "*":
                token = re.match(division["TokenFinalizaComentarioMultilinea"], archivo[pointer:], re.IGNORECASE)
                if token:
                    pointer += token.end()
                    columna += token.end()
                    enComentario = False
                    comentPosition = None
                else:
                    pointer += 1
                    linea += 1
            else:
                pointer += 1
        elif caracter == " ":
            pointer += 1
            columna += 1
        elif caracter.isdigit():
            token = re.match(tokensNoSimbolos["TokenNumero"], archivo[pointer:], re.IGNORECASE)
            if token:
                guardarToken(tokenList, "TokenNumero", linea, columna, token.group())
                pointer += token.end()
                columna += token.end()
            else:
                print("Error en la linea {0}, columna {1}".format(linea, columna))
                break
        elif caracter.isalpha() or caracter == "_":
            for palabraReservada in palabrasReservadas:
                token = re.match(palabraReservada, archivo[pointer:], re.IGNORECASE)
                if token:
                    break
            if token:
                guardarToken(tokenList, palabraReservada, linea, columna)
                pointer += token.end()
                columna += token.end()
            else:
                token = re.match(tokensNoSimbolos["TokenIdentificador"], archivo[pointer:], re.IGNORECASE)
                if token:
                    guardarToken(tokenList, "TokenIdentificador", linea, columna, token.group())
                    pointer += token.end()
                    columna += token.end()
                else:
                    print("Error en la linea {0}, columna {1}".format(linea, columna))
                    break
        elif caracter == "/":
            token = re.match(division["TokenDivision"], archivo[pointer:], re.IGNORECASE)
            if token:
                guardarToken(tokenList, "TokenDivision", linea, columna)
                pointer += token.end()
                columna += token.end()
            else:
                token = re.match(division["TokenComentarioSencillo"], archivo[pointer:], re.IGNORECASE)
                if token:
                    pointer += token.end()
                    columna += token.end()
                else:
                    token = re.match(division["TokenIniciaComentarioMultilinea"], archivo[pointer:], re.IGNORECASE)
                    if token:
                        enComentario = True
                        pointer += token.end()
                        columna += token.end()
                        comentPosition = [linea, columna]
                    else:
                        print("Error en la linea {0}, columna {1}".format(linea, columna))
                        break
        elif caracter == '"':
            token = re.match(tokensNoSimbolos["TokenCadena"], archivo[pointer:], re.IGNORECASE)
            if token:
                guardarToken(tokenList, "TokenCadena", linea, columna, token.group())
                pointer += token.end()
                columna += token.end()
            else:
                print("Error en la linea {0}, columna {1}".format(linea, columna))
                break
        elif caracter == "'":
            token = re.match(tokensNoSimbolos["TokenCaracter"], archivo[pointer:], re.IGNORECASE)
            if token:
                guardarToken(tokenList, "TokenCaracter", linea, columna, token.group())
                pointer += token.end()
                columna += token.end()
            else:
                print("Error en la linea {0}, columna {1}".format(linea, columna))
                break
        else:
            for simbolo in simbols:
                token = re.match(simbols[simbolo], archivo[pointer:], re.IGNORECASE)
                if token:
                    guardarToken(tokenList, simbolo, linea, columna)
                    pointer += token.end()
                    columna += token.end()
                    break
            if not token:
                print("Error en la linea {0}, columna {1}".format(linea, columna))
                break
    guardarToken(tokenList, "$", linea+1, 1)
    if(enComentario and comentPosition):
        print("Error en la linea {0}, columna {1}".format(comentPosition[0], comentPosition[1]))
            

getTokens(leerArhivo("casos.txt"))
for i in tokenList:
  print(i)

        


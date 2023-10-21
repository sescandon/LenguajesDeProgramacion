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





        


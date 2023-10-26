import ply.lex as lex
from prettytable import PrettyTable
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'global': 'GLOBAL',
    'def': 'DEF',
    'return': 'RETURN',
    'elif': 'ELIF',
    'print': 'PRINT',
    'raise': 'RAISE',
    'split': 'SPLIT',
    'locals': 'LOCALS',
    'int': 'INT',
    'continue': 'CONTINUE',
    'or': 'OR',
}

# Lista de tokens
tokens = list(reserved.values()) + [
    'TokenPunto',
    'TokenComa',
    'TokenDosPuntos',
    'TokenRectangularesCierre',
    'TokenRectangularesApertura',
    'TokenParentesisCierre',
    'TokenParentesisAbre',
    'TokenMas',
    'TokenMenos',
    'TokenMultiplica',
    'TokenPotencia',
    'TokenIgual',
    'TokenNoIgual',
    'TokenMenorIgual',
    'TokenMenor',
    'TokenMayorIgual',
    'TokenMayor',
    'TokenDivision',
    'TokenComentarioSencillo',
    'TokenComentarioMultilinea',
    'TokenPorcentaje',
    'TokenIdentificador',
    'TokenNumero',
    'TokenCadena',
    'TokenCaracter',
]
print(tokens)

# Definición de las reglas de expresiones regulares
t_TokenPunto = r'\.'
t_TokenComa = r','
t_TokenDosPuntos = r':'
t_TokenRectangularesCierre = r'\]'
t_TokenRectangularesApertura = r'\['
t_TokenParentesisCierre = r'\)'
t_TokenParentesisAbre = r'\('
t_TokenMas = r'\+'
t_TokenMenos = r'-'
t_TokenMultiplica = r'\*'
t_TokenPotencia = r'\^'
t_TokenIgual = r'='
t_TokenNoIgual = r'<>'
t_TokenMenorIgual = r'<='
t_TokenMenor = r'<'
t_TokenMayorIgual = r'>='
t_TokenMayor = r'>'
t_TokenDivision = r'/'
t_TokenComentarioSencillo = r'\#.*'
t_TokenComentarioMultilinea = r'"""(.|\n)*?"""'
t_TokenPorcentaje = r'%'
t_ignore = ' \t'

# Regla para identificadores
def t_TokenIdentificador(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Regla para números
def t_TokenNumero(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para cadenas
def t_TokenCadena(t):
    r'"([^"\n])*"'
    return t

# Regla para caracteres
def t_TokenCaracter(t):
    r"'([^'\n])*'"
    return t

# Regla para manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regla para manejar errores léxicos
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer


lexer = lex.lex()

# Test del lexer
def leerArchivo(archivo):
    with open(archivo, 'r') as file:
        return file.read()

text = leerArchivo("Pena.txt")

lexer.input(text)



# Crear una tabla para los tokens
table = PrettyTable()
table.field_names = ["Valor", "Tipo"]

# Iterar a través de los tokens y agregarlos a la tabla
while True:
    tok = lexer.token()
    if not tok:
        break
    table.add_row([tok.value, tok.type])

# Imprimir la tabla
print(table)


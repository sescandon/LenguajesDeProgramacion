import ply.lex as lex


reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    "global": "GLOBAL", 
    "def": "DEF", 
    "return": "RETURN", 
    "if": "IF", 
    "else": "ELSE",
    "elif": "ELIF",
    "print": "PRINT",
}

# Define the lexer tokens
tokens = [
    "TokenPunto",
    "TokenComa",
    "TokenDosPuntos",
    "TokenRectangularesCierre",
    "TokenRectangularesApertura",
    "TokenParentesisCierre",
    "TokenParentesisAbre",
    "TokenMas",
    "TokenMenos",
    "TokenMultiplica",
    "TokenPotencia",
    "TokenIgual",
    "TokenNoIgual",
    "TokenMenorIgual",
    "TokenMenor",
    "TokenMayorIgual",
    "TokenMayor",
    
    "TokenDivision",
    "TokenComentarioSencillo",
    "TokenComentarioMultilinea",
    
    "TokenIdentificador",
    "TokenNumero",
    "TokenCadena",
    "TokenCaracter",
] + list(reserved.values())

# Define the regular expressions for each token
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



t_TokenNumero = r'[0-9]+'
t_TokenCadena = r'"([^"\n])*"'
t_TokenCaracter = r"'([^'\n])*'"

t_ignore = ' \n'
# Define the lexer functions for reserved words

def t_TokenIdentificador(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t



# Define the lexer error handling function
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
def leerArhivo(archivo):
    with open(archivo, 'r') as file:
        return file.read()
text = leerArhivo("Pena.txt")

lexer.input(text)
for token in lexer:
    print(token)
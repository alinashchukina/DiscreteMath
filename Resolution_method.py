import ply.lex as lex
import ply.yacc as yacc

# build lexer, which splits equation on separate tokens
tokens = (
    'VARIABLE',
    'NEGATION',
    'CONJUNCTION',
    'DISJUNCTION',
    'IMPLICATION',
    'LPAREN',
    'RPAREN',
)

t_VARIABLE = r'[a-z]'
t_NEGATION = r'~'
t_CONJUNCTION = r'/\\'
t_DISJUNCTION = r'\\/'
t_IMPLICATION = r'->'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# build parser, which recognizes grammar of the equation
def p_conjunction(p):
    'expression : expression CONJUNCTION expression'
    p[0] = (p[1], p[3])


def p_single_expression(p):
    'expression : clause'
    p[0] = p[1]


def p_paren(p):
    'expression : LPAREN clause RPAREN'
    p[0] = p[2]


def p_implication(p):
    'clause : literal IMPLICATION literal'
    lst.append(((p[1][0], 1 - p[1][1]), p[3]))
    p[0] = (p[1], p[3])


def p_disjunction(p):
    'clause : literal DISJUNCTION literal'
    lst.append((p[1], p[3]))
    p[0] = (p[1], p[3])


def p_single_clause(p):
    'clause : literal'
    lst.append((p[1], (None, None)))
    p[0] = p[1]


def p_negation(p):
    'literal : NEGATION VARIABLE'
    p[0] = (p[2], 0)


def p_variable(p):
    'literal : VARIABLE'
    p[0] = (p[1], 1)


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()


# define tautology function for two symbols
def tautology(clause):
    return clause[0][0] == clause[1][0] and clause[0][1] != clause[1][1]


# store 2-CNF formula in the list of tuples with 2 literals/None's
# each literal is represented in a tuple with variable on the 0 place
# and the fact of negation on the second case
# resolution function applies mechanism of resolution
# by adding new clauses until all clauses are generated (satisfiable)
# or until empty clause is generated (2-CNF is not satisfiable)
def resolution():
    i = 0
    while True:
        if i >= len(lst):
            break
        j = i + 1
        while True:
            if j >= len(lst):
                break
            for a in range(2):
                for b in range(2):
                    if tautology((lst[i][a], lst[j][b])):
                        new = (lst[i][1 - a], lst[j][1 - b])
                        if new == ((None, None), (None, None)):
                            lst.append(new)
                            print('Not satisfiable')
                            return
                        if new[0] == new[1]:
                            new = (new[0], (None, None))
                        if new not in set(lst) and not tautology(new):
                            lst.append(new)
            j += 1
        i += 1
    print('Satisfiable')
    return


data = input()
lexer.input(data)
lst = []
result = parser.parse(data)

for i in range(len(lst)):
    if lst[i][0] == lst[i][1]:
        lst[i] = (lst[i][0], (None, None))
resolution()

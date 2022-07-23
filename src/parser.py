from sly import Parser
from calclex import CalcLexer

class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens

    precedence = (
       ('left', PLUS, MINUS),
       ('left', TIMES, DIVIDE),
    )

    # Grammar rules and actions
    @_('def ident(PARAMLIST){STATELIST}')
    def FUNCDEF(self, p):
        return p.expr + p.term

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()

    while True:
        try:
            text = input('calc > ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break
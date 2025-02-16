grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type

    if not hasattr(self, "prev_token"):
        self.prev_token = None  

    if tk == self.UNCLOSE_STRING:       
        result = super().emit()
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text)
    elif tk == self.NL:
        if self.prev_token in {
            self.RETURN, self.CONTINUE, self.BREAK,
            self.FLOATLIT, self.STRINGLIT, self.BOOLLIT, self.INTLIT,
            self.FLOAT, self.STRING,self.BOOLEAN, self.INT,
            self.RP, self.RB, self.RSB,self.ID
        }:
            self.type = self.SEMI
            self.text = ';'
            result = super().emit()
        else:
            return self.nextToken()
    else:
        result = super().emit()

    self.prev_token = result.type 
    return result
}

options {
    language=Python3;
}

/*----------2. Program structure----------*/
program  : decls EOF;
decls: decl decls |;
decl: (const_decl|var_decl|type_decl|func_decl) (SEMI|NL);

/*---------------------------declaration---------------------------------*/
const_decl: CONST ID ASSIGN expr;
var_decl: scalar_decl| array_decl|struct_var_decl;
type_decl: struct_decl|interface_decl;
func_decl: func|method;


/*---------------------------var declaration---------------------------------*/
array_decl: VAR ID arraytype;
scalar_decl: VAR ID primitivetype (ASSIGN expr)?
            |VAR ID ASSIGN expr;
struct_var_decl: VAR ID structtype (ASSIGNMENT structliteral)?
                |VAR ID ASSIGNMENT structliteral;

/*---------------------------type declaration---------------------------------*/
struct_decl: TYPE ID STRUCT LB fieldnamelist RB;
fieldnamelist: ID datatype (SEMI|NL) fieldnamelist | ID datatype (SEMI|NL);
datatype: primitivetype|compositetype|arraytype;
primitivetype: INT|FLOAT|STRING|BOOLEAN;
compositetype: structtype|interfacetype;
structtype: ID;
interfacetype: ID;
arraytype: dimensions (primitivetype|compositetype);
dimensions: LSB (INTLIT|ID) RSB dimensions | LSB (INTLIT|ID) RSB;
interface_decl: TYPE ID INTERFACE LB methodlist RB;
methodlist: ID LP paramlist RP primitivetype? (SEMI|NL)? methodlist | ID LP paramlist RP primitivetype? (SEMI|NL)?;

/*---------------------------func declaration---------------------------------*/
func: FUNC ID LP paramlist RP datatype? body;
paramlist: paramprime | ;
paramprime: ID primitivetype COMMA paramprime| ID COMMA paramprime| ID primitivetype;
body: LB stmtlist RB;
stmtlist: stmt stmtlist|stmt;
stmt: (returnstmt|const_decl|var_decl|assignstmt|ifstmt|forstmt|callstmt|breakstmt|continuestmt) (SEMI|NL);
assignstmt: (scalaassign|fieldassign|arrayassign|struct_instance);
scalaassign: ID (ASSIGNMENT|ADDASS|SUBASS|MULASS|DIVASS|MODASS) expr;
fieldassign: fieldaccess (ASSIGNMENT|ADDASS|SUBASS|MULASS|DIVASS|MODASS) expr;
arrayassign: arrayaccess (ASSIGNMENT|ADDASS|SUBASS|MULASS|DIVASS|MODASS) expr;
struct_instance: ID ASSIGNMENT structliteral;
fieldaccess: ID DOT ID;
arrayaccess: ID dimensions_stmt;
dimensions_stmt: LSB expr RSB dimensions_stmt | LSB expr RSB; //decl array: số nguyên hoặc const, stmt array: expr
returnstmt: RETURN expr?;
method: FUNC receiver ID LP paramlist RP datatype body;
receiver: LP ID compositetype RP;

ifstmt: if_clause elseif_clauselist else_clause? ;
if_clause: IF subexpr body;
else_clause: ELSE body;
elseif_clauselist: elseif_clause elseif_clauselist |;
elseif_clause: ELSE IF subexpr body;

forstmt: (forbasic|foricu|forrange);
forbasic: FOR subexpr body;
foricu: FOR initialization_clause condition_clause update_clause body;
initialization_clause: scalaassign SEMI|scalar_decl;
condition_clause: expr SEMI;
update_clause: scalaassign;
forrange: FOR (ID|'_') COMMA ID ASSIGNMENT RANGE expr body;

breakstmt: BREAK;
continuestmt: CONTINUE;
callstmt: struct_call|func_call;

/*----------4.1 Boolean Type----------*/
expr: expr OR expr1 | expr1 ;
expr1: expr1 AND expr2 | expr2;
expr2: expr2 (EQUAL|N_EQUAL|LESS|L_EQUAL|GREATER|G_EQUAL) expr3 | expr3;
expr3: expr3 (ADD|SUB) expr4 | expr4;
expr4: expr4 (MUL|DIV|MOD) expr5 | expr5 ;
expr5: (NOT|SUB) expr5 | expr6;
expr6: primitive_literals|arrayliteral|structliteral|subexpr|ID|fieldaccess|arrayaccess|call;
subexpr: LP expr RP;

call: struct_call|func_call;
struct_call: fieldaccess LP argumentlist RP; //a.b()
func_call: ID LP argumentlist RP; //b()
argumentlist: argumentprime | ;
argumentprime: expr COMMA argumentprime | expr;
literals: primitive_literals|arrayliteral|structliteral;
structliteral: structtype LB fieldvaluelist RB; //Person{a:"a", b:"b"}
fieldvaluelist: fieldvalueprime|;
fieldvalueprime: ID COLON expr COMMA fieldvalueprime | ID COLON expr;
arrayliteral: arraytype elementlist;
elementlist: LB (element COMMA elementlist | element) RB;
element: elementlist | expr;

/*----------6.6.2 Struct Literals----------*/

primitive_literals: INTLIT|FLOATLIT|STRINGLIT|BOOLLIT;
/*----------Boolean Literals----------*/
BOOLLIT: TRUE|FALSE;

/*---------Type----------*/

/*----------3.3.2 Keywords----------*/
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
INT: 'int';
FLOAT: 'float';
STRING: 'string';
BOOLEAN: 'boolean';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

/*----------3.2 Program comment----------*/
COMMENT: '/*' (COMMENT|.)*? '*/'  -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

/*----------3.3.3 Operators----------*/
ADD: '+'; SUB: '-'; MUL: '*'; DIV: '/'; MOD: '%';
EQUAL: '=='; N_EQUAL: '!='; LESS: '<'; L_EQUAL: '<='; GREATER: '>'; G_EQUAL: '>=';
AND: '&&'; OR: '||'; NOT: '!';
ASSIGNMENT: ':='; ADDASS: '+='; SUBASS: '-='; MULASS: '*='; DIVASS: '/='; MODASS: '%=';
ASSIGN: '=';DOT: '.';

/*----------3.3.4 Separators----------*/
LP: '('; RP: ')'; LSB: '['; RSB: ']'; LB: '{'; RB: '}';
COMMA: ','; SEMI: ';'; COLON: ':';

/*----------3.3.5 Literals----------*/
/*----------Integer Literals----------*/
INTLIT: DEC|BIN|OCT|HEX;
fragment DEC: '0'|[1-9][0-9]*;
fragment BIN: '0' [Bb] [0-1]+;
fragment OCT: '0' [Oo] [0-7]+;
fragment HEX: '0' [Xx] [0-9A-Fa-f]+;

/*----------Floating-point Literals----------*/
FLOATLIT: INTPART DOT INTPART? | INTPART DOT INTPART EXPPART?;
fragment INTPART: [0-9]+;
fragment EXPPART: [Ee] [+-]? [0-9]+;

/*----------String Literals----------*/
STRINGLIT: '"' STR_CHAR* '"';
fragment STR_CHAR: (~["\\]|ESC);
fragment ESC: '\\' [ntr"\\];

/*----------3.3.1 Identifiers----------*/
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

/*----------3.1 Characters set----------*/
WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs 
NL: '\n';

UNCLOSE_STRING: '"' STR_CHAR* {raise UncloseString(self.text[:])};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {raise IllegalEscape(self.text[:])};
/*các ký tự bắt đầu bằng \ mà không phải là (\n \t \r " \\) ví dụ \a hoặc ký tự \ */
fragment ESC_ILLEGAL: '\\' ~[ntr"\\] | '\\'; 

ERROR_CHAR: . {raise ErrorToken(self.text)};
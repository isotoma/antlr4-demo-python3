grammar Demo;

program: subroutine+;

subroutine: 'sub' ID '{' body '}';

body: statement+;

statement: print | read | gosub | assign | halt | if;

print: 'print' expr ';';
read: 'read' ID ';';
gosub: 'gosub' ID ';';
assign: ID '=' expr ';';
halt: 'halt' ';';
if: 'if' compare '{' body '}' ('else' '{' body '}')?;

compare: expr op = ('==' | '!=' | '<' | '<=' | '>' | '>=') expr;

expr:
	expr op = ('+' | '-') expr		# AddSub
	| expr op = ('*' | '/') expr	# MulDiv
	| ID							# Id
	| NUMBER						# Number
	| STRING						# String;

NUMBER: [0-9]+;
ID: [a-zA-Z][a-zA-Z0-9]*;
STRING: '"' .*? '"';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
WS: [ \t\r\n]+ -> skip;
EQ: '==';
NE: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
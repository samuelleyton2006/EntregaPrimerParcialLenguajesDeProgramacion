%{
#include "y.tab.h"
%}

%%

[0-9]+"."[0-9]+    { yylval.fval = atof(yytext); return REAL; }
[0-9]+             { yylval.fval = atof(yytext); return REAL; }
sqrt               { return SQRT; }
[ \t\n]            ; // Ignorar espacios y saltos de línea
.                  { return yytext[0]; }
%%

int yywrap() { return 1; }

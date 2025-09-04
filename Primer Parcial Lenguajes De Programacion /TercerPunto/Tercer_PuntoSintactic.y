%{
#include <stdio.h>
#include <math.h>
void yyerror(char *s);
int yylex();
%}

%union {
    double fval;
}

%token <fval> REAL
%token SQRT

%type <fval> expr

%%

input: /* vacío */
     | input line
     ;

line: expr '\n' { printf("Resultado: %.8g\n", $1); }
    ;

expr: REAL           { $$ = $1; }
    | SQRT expr      { 
                        if ($2 < 0) {
                            printf("Error: raíz de número negativo.\n");
                            $$ = 0;
                        } else {
                            $$ = sqrt($2);
                        }
                      }
    ;

%%

void yyerror(char *s) { fprintf(stderr, "Error: %s\n", s); }
int main(int argc, char **argv) {
    if (argc > 1) {
        FILE* file = fopen(argv[1], "r");
        if (!file) {
            perror("No se pudo abrir el archivo de entrada");
            return 1;
        }
        yyin = file;
    }
    yyparse();
    return 0;
}

%union { float fval; }
%token <fval> NUM
%token SQRT
%%
calculo: SQRT NUM    { printf("Raiz: %.2f\\n", sqrt($2)); }
      | NUM          { printf("Numero: %.2f\\n", $1); }
      ;
%%

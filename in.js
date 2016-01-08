/* Programa de ejemplo  */
/*******  6, diciembre, 2016 *********/
/* El ejemplo incorpora elementos del lenguaje opcionales y elementos que no hay que implementar */
/* Declaración de variables */

// var chars one // Declaración de una variable
// var chars s	= "string" // Declaracion con constante
// var chars z, b, p // Múltiples variables

// var int two // Declaración de una variable
// var int v = 5 // Declaracion con constante
// var int g, e, f // Múltiples variables
// var bool boo // Declaración de una variable
// var bool bo, co // Múltiples variables

/* Tipo de datos */



/*------------------------------------*/
/*---INSTRUCCIONES DE ENTRADA/SALIDA--*/
/*------------------------------------*/

var int a

//La sentencia write (expresión) evalúa la expresión e imprime el resultado por pantalla. Por ejemplo:
a = 50; write(a * 2 + 16) /* imprime: 116 */

//La expresión puede ser también una cadena o un lógico. Por ejemplo:
a = "Adiós"
write("Hola"); write(a) /* imprime HolaAdiós */

// La sentencia prompt (var) lee un número o una cadena del teclado y lo almacena en la variable var, 
// que tiene que ser, respectivamente, de tipo entero o cadena. Por ejemplo:
var chars c
prompt (a) // lee un número
write(a * a) /* imprime el cuadrado del número leído */
write("Pon tu nombre")
prompt (c) // lee una cadena

/*------------------------------------*/
/*---OPERACIONES DE ASIGNACIÓN--*/
/*------------------------------------*/

d |= a /* es equivalente a b1 = b1 |= d */

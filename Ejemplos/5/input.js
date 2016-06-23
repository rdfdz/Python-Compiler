/* Programa de ejemplo 5  */
/******* José Luis Fuertes, 5, septiembre, 2015 *********/
/* El ejemplo incorpora elementos del lenguaje opcionales y elementos que no hay que implementar */

var chars s	/* variable global cadena */
var int num
var int a

function int FactorialRecursivo (int n)	/* n: parámetro formal de la función entera */
{
	if (n == 0)	write("Error")
//	return n * FactorialRecursivo (n - 1)	/* llamada recursiva */ ERROR
	return 2 // entero
}

function int FactorialDo (int n)
{
	var int factorial 	// variable local inicializada a uno
	//	 	NO IMPLEMENTACION       //
	//do
	//{
	//	factorial *= n--	// equivale a: factorial = factorial * n; n = n - 1;
	//} while (n)		// mientras n no sea 0
	return factorial	// devuelve el valor entero de la variable factorial
}

function int FactorialWhile ()
{
	var int factorial 
	var int i 
	//	 	NO IMPLEMENTACION       //
	//while (i < num)			// num es variable global entera sin declarar
	//{
	//	factorial *= ++i	// equivale a: i = i + 1; factorial = factorial * i;
	//}
	return factorial
}

function int FactorialFor (int n)
{
	var int i
	var int factorial 	/* variables locales */
	for (i = 1; i <= n; i = i + 1)
	{
		factorial |= i // Caso grupo 51
	}
	return factorial
}

var int For, Do, While	// tres variables globales

function imprime (chars msg, int f)	/* función que recibe dos argumentos */
{
	write (s)
	write (msg)
	write (f)
	write ("\n")	// imprime un salto de línea */
	return	/* finaliza la ejecución de la función (en este caso, se podría omitir) */
}

function chars cadena (bool log)
{
	if (!log)
		write("error")
	//	 	NO IMPLEMENTACION       //
	//else
	//{
	//	return "Fin"
	//}
	//return "FIN" // NO DEJA STRINGS
	return log
}	// fin cadena: función que devuelve una cadena

// Parte del programa principal:
s = "El factorial "	// Primera sentencia que se ejecutaría  

write (s)
write ("\nIntroduce un 'número'.")
prompt (num)	/* se lee un número del teclado y se guarda en la variable global num */


function bool esFechaCorrecta (int d, int m, int a)	
{
	return m>=1 && m<=12 && d>=1 //&& d <= //NO IMPLEMENTACION// ---->dias (m, a)
} //fin de esFechaCorrecta

function imprime2 (int v, int w)	
{
	write (v + w)
} //fin de imprime2

function potencia (int z, int dim)	
{
	var int s	// Oculta a la global
	for (s=0; s < dim; s = s + 1)
	{
		//NO IMPLEMENTACION//z *= z
		z |= z
		//write("Potencia") 
		
	}
} // fin de potencia: función que no devuelve nada

function demo ()	/* definición de la función demo, sin argumentos y que no devuelve nada */
{
	var int i	// Variables locales
	var int v0
	var chars s	// Oculta a la global
	var int v
	var int v1
	var int v2
	var int v3
	var int zv 

	write ("Escriba tres números: ")
	prompt (v1)
	prompt (v2)
	prompt (v3)

	//if (!((v1 == v2) && (v1 != v3)))	/* NOT ((v1 igual a v2) AND (v1 distinto de v3))  */
//	{
		write ("Escriba su nombre: ")
		prompt (s)
		//v0 = (v2 < v3) ? (v2): (v3)	/* si v2<v3, v0=v2; en otro caso v0=v3 */
		write (s)
//	}
	
	s = "El primer valor era "  
	
	if (v1 != 0)
		write (v1)
	
	//	 	NO IMPLEMENTACION       //
	//else
	//{
	//	write (s, 0, ".\n")	// imprime la cadena `El primer valor era 0.\n´
	//}


	for (i=1; i <= 10; i = i + 1)
	{
		//NO IMPLEMENTACION//zv+=i
		zv|=i
	}
	
	write (num)
	write(s)
}

/* esto constituye la llamada a una función sin argumentos. 
Es en este instante cuando se llama a esta función y, por tanto, 
cuando se ejecuta todo el código de dicha función */
demo() // NO DEJA SIN ARGUMENTOS

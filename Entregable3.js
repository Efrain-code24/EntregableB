let n1=24;
let n2=12;
let operacion = "suma"; //puede ser "suma", "resta", "multiplicacion" o "division" 
function realizarOperacion(n1, n2, operacion) {
    if (operacion === "suma") {
        return n1 + n2;
    }
    else if (operacion === "resta") {
        return n1 - n2;
    }
    else if (operacion === "multiplicacion") {
        return n1 * n2;
    }
    else if (operacion === "division") {
        if (n2 !== 0) {
            return n1 / n2;
        } else {
            return "Error: División por cero";
        }
    } else {
        return "Operación no válida";
    }
  }   
  let continuar=true

while (continuar) {
       let num1 = parseFloat(prompt("Ingrese el primer número:"));
    let num2 = parseFloat(prompt("Ingrese el segundo número:"));
    let operacion = prompt("Ingrese la operación (suma, resta, multiplicacion, division) o 'salir' para terminar:");

    if (operacion.toLowerCase() === "salir") {
        alert("Gracias por usar la calculadora. ¡Hasta luego!");
        continuar = false;
    } else {
        let resultado = realizarOperacion(num1, num2, operacion.toLowerCase());
        alert("Resultado: " + resultado);
    }
}
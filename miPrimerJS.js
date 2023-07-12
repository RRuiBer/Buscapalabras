//suma, resta, multiplicación y división.

function suma (a,b){
    result = a + b
    console.log(result)
}

suma(20,7)

let lista = [5, 8, 7, 27, 915, 16, 15, 886, 153, 1565, 1575, 156, 1535];
let max = lista[Math.floor(Math.random() * lista.length)];
console.log(max);

for (let i = 0; i < lista.length; i++) {
    if (max < lista[i]) {
        max = lista[i];
    }
}
console.log(max);

/*
4. *Нарисовать пирамиду с помощью console.log, как показано на рисунке, только у вашей пирамиды должно быть 20 рядов, а не 5:x
*/

console.log('Task - 4');
console.log('---------------------------------------------');

for(let i=1; i<21; i++){
    let str = ''
    for(j=1; j <= i; j++){
        str += '*'
    }
    console.log(str)
}


console.log('---------------------------------------------');
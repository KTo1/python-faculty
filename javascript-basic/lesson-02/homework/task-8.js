/* 
С помощью рекурсии организовать функцию возведения числа в степень. Формат: function power(val, pow), где val – заданное число, pow – степень.
*/

console.log('Task - 8');
console.log('---------------------------------------------');

function power(val, pow){
    if (pow == 0) {
        return 1
    }
    
    return val * power(val, pow - 1)
};

console.log(`3 ^ 5 = ${power(3, 5)}`);

console.log('---------------------------------------------');
/*
Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation), 
где arg1, arg2 – значения аргументов, operation – строка с названием операции. 
В зависимости от переданного значения операции выполнить одну из арифметических операций (использовать функции из пункта 5) 
и вернуть полученное значение (использовать switch).
*/

console.log('Task - 6');
console.log('---------------------------------------------');

function mathOperation(arg1, arg2, operation){
    switch (operation){
        case '+': return add(arg1, arg2);
        case '-': return sub(arg1, arg2);
        case '*': return mul(arg1, arg2);
        case '/': return div(arg1, arg2);
        default: return 'Неизвестная операция';    
    }
};

console.log(mathOperation(2, 2, '+'));
console.log(mathOperation(2, 2, '-'));
console.log(mathOperation(2, 2, '*'));
console.log(mathOperation(2, 2, '/'));
console.log(mathOperation(2, 2, 'q'));

console.log('---------------------------------------------');
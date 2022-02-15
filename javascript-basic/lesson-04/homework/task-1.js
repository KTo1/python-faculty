/*
Написать функцию, преобразующую число в объект. Передавая на вход число от 0 до 999, мы должны получить на выходе объект, 
в котором в соответствующих свойствах описаны единицы, десятки и сотни. 
Например, для числа 245 мы должны получить следующий объект: 
{‘единицы’: 5, ‘десятки’: 4, ‘сотни’: 2}. 
Если число превышает 999, необходимо выдать соответствующее сообщение с помощью console.log и вернуть пустой объект.
Что есть пустой объект? Пусть будет {}
*/

console.log('Task - 2');
console.log('---------------------------------------------');


function num_to_object(num){    
    if  (0 <= num && num <= 999) {
        return {
                'единицы': num % 10, 
                'десятки': Math.floor(num / 10) % 10,
                'сотни': Math.floor(num / 100) % 10
                }

    } else {
        console.log('Недопустимое значение параметра (от 0 до 999 включительно)')
        return {}
    };
}


console.log(num_to_object(156))
console.log(num_to_object(651))
console.log(num_to_object(1))
console.log(num_to_object(-10))
console.log(num_to_object(1000))


console.log('---------------------------------------------');

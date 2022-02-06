/* 
1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.
*/
console.log('Task - 1');
console.log('---------------------------------------------');

let i = 2;                                                   
let is_simple;
while(i<=100){

    is_simple = true
    for(j=2; j<=100; j++){
        if (i % j === 0 && i !== j){
            is_simple=false;
            break;
        };
    };

    if(is_simple){console.log(i)};

    i++;
};


console.log('---------------------------------------------');

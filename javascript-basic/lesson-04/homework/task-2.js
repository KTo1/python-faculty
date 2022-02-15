/*
2.Продолжить работу с интернет-магазином:
2.1. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими объектами можно заменить их элементы?
2.2. Реализуйте такие объекты.
2.3. Перенести функционал подсчета корзины на объектно-ориентированную базу.
*/

console.log('Task - 2');
console.log('---------------------------------------------');


const Basket = 
    {
        goods: [],
        add(id, name, count, price){
            this.goods.push([id, name, count, price]);      
        },
        countBasketPrice(){
            return this.goods.reduce((total, item) => total + item[2] * item[3], 0);
        },
    };


Basket.add(1, 'good 1', 1, 30)
Basket.add(2, 'good 2', 2, 12)
Basket.add(3, 'good 3', 7, 16)

console.log(`Сумма товаров в корзине: ${Basket.countBasketPrice()}`)


console.log('---------------------------------------------');
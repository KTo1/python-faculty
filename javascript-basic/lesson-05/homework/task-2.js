/*
2. Сделать генерацию корзины динамической: верстка корзины не должна находиться в HTML-структуре. Там должен быть только div, в который будет вставляться корзина, сгенерированная на базе JS:
2.1. Пустая корзина должна выводить строку «Корзина пуста»;
2.2. Наполненная должна выводить «В корзине: n товаров на сумму m рублей».
*/

console.log('Task - 2');
console.log('---------------------------------------------');


const Basket = 
    {
        goods: [],
        add(id, name, count, price){
            this.goods.push([id, name, count, price]);      
        },
        clear(){
            this.goods = []
        },
        countBasketPrice(){
            return this.goods.reduce((total, item) => total + item[2] * item[3], 0);
        },
        countBasket(){
            return this.goods.reduce((total, item) => total + item[2], 0);
        },
    };

const parentElementBasket = document.getElementById("basket");

const divFullBasket = document.createElement('div');
const divEmptyBasket = document.createElement('div');

Basket.add(1, 'good 1', 1, 30)
Basket.add(2, 'good 2', 2, 12)
Basket.add(3, 'good 3', 7, 16)

countBasketPrice = Basket.countBasketPrice();
divFullBasket.textContent = countBasketPrice ? `В корзине: ${Basket.countBasket()} товаров на сумму: ${Basket.countBasketPrice()} рублей` : 'Корзина пуста';

Basket.clear();

countBasketPrice = Basket.countBasketPrice();
divEmptyBasket.textContent = countBasketPrice ? `В корзине: ${Basket.countBasket()} товаров на сумму: ${Basket.countBasketPrice()} рублей` : 'Корзина пуста';
 
parentElementBasket.appendChild(divFullBasket);
parentElementBasket.appendChild(divEmptyBasket);

console.log('---------------------------------------------');
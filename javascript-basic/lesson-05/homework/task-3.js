/*
3*. Сделать так, чтобы товары в каталоге выводились при помощи JS:
3.1. Создать массив товаров (сущность Product);
3.2. При загрузке страницы на базе данного массива генерировать вывод из него. 
HTML-код должен содержать только div id=”catalog” без вложенного кода. Весь вид каталога генерируется JS.

На моем текущем уровне понимания проекта я вижу что-то вот такое) не совсем по заданию, но это ведь задание со звездой)
*/

const Catalog = 
    {
        goods: [],
        add(id, name, count, price){
            this.goods.push([id, name, count, price]);      
        },
        clear(){
            this.goods = []
        },
        Draw(Container){

            Container.innerHTML = '';

            this.goods.forEach(function(item, i, goods) {
                const divProduct = document.createElement('div');
                divProduct.textContent = item[1];
                Container.appendChild(divProduct);                
            });            
        },
    };

const parentElementCatalog = document.getElementById("catalog");

Catalog.add(1, 'good 1', 1, 30);
Catalog.add(2, 'good 2', 2, 12);
Catalog.add(3, 'good 3', 7, 16);

Catalog.Draw(parentElementCatalog);

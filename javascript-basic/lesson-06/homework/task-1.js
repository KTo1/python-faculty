/*
1. Доработать модуль корзины.
a. Добавлять в объект корзины выбранные товары по клику на кнопке «Купить» без перезагрузки страницы
b. Привязать к событию покупки товара пересчет корзины и обновление ее внешнего вида

Сущности Товар уже явно не хватает )

*/


console.log('Task - 1');
console.log('---------------------------------------------');

const Basket = 
    {
        goods: [],
        settings: {
            container: null,
            basketName: 'Корзина',
        },

        init(userSettings={}){
            Object.assign(this.settings, userSettings);
        },

        getSetting(settingName){
            return this.settings[settingName];
        },

        add(id, name, images, count, price){
            element = this.goods.find(el => (el.id === id));
            if (element) {
                element[3]++;
            } else {
                this.goods.push({id:id, name:name, images:images, count:count, price:price});
            };
        },

        clear(){
            this.goods = []
        },

        countBasketPrice(){
            return this.goods.reduce((total, item) => total + item.count * item.price, 0);
        },

        countBasket(){
            return this.goods.reduce((total, item) => total + item.count, 0);
        },

        draw(){

            container = this.getSetting('container');

            container.innerHTML = '';

            tableBoard = document.createElement('table');
            tableBoard.id = "tableBoard";
            tableBoard.textContent = this.settings.basketName;
            container.appendChild(tableBoard);

            tr = null;
            this.goods.forEach(function(item, i, goods) {
                const divProductContianer = document.createElement('div');
                const tr = document.createElement('tr');

                const tdProduct = document.createElement('td');
                const tdCount = document.createElement('td');
                const tdPrice = document.createElement('td');
                const tdTotal = document.createElement('td');

                tdProduct.textContent = item.name + ': ';
                tdCount.textContent = item.count + ': ';
                tdPrice.textContent = item.price + ' (руб.) : ';
                tdTotal.textContent = item.count * item.price + ' (руб.) ';

                tr.appendChild(tdProduct);
                tr.appendChild(tdCount);
                tr.appendChild(tdPrice);
                tr.appendChild(tdTotal);
                
                tableBoard.appendChild(tr);

            }, this);               

            if (tr) {
                divProductContianer.appendChild(tr);
                container.appendChild(divProductContianer);             
            };
        },    
    };

const Catalog = 
    {
        basket: null,
        goods: [],

        settings:{
            imagePath: 'images',
            imagePathSmall: 'small',
            imagePathBig: 'big',
            buyButttonName: 'Купить',    
            buyButttonColor: '#248a1e',
            container: null,
        },

        init(userSettings={}, basket){
            Object.assign(this.settings, userSettings);
            this.basket = basket;
            this.basket.draw();
        },

        getSetting(SettingName){
            return this.settings[SettingName];
        },

        getImagesPath(){
            return this.settings.imagePath;
        },

        getImagesPathSmall(){
            return this.getImagesPath() + '\\' + this.settings.imagePathSmall;
        },

        getImagesPathBig(){
            return this.getImagesPath() + '\\' + this.settings.imagePathBig;
        },

        add(id, name, images, count, price){
            this.goods.push({id:id, name:name, images:images, count:count, price:price});
        },

        addToBasket(item){
            this.basket.add(item.id, item.name, item.images, 1, item.price);
            this.basket.draw()
        }, 
        
        clear(){
            this.goods = []
        },

        draw(){

            container = this.getSetting('container');

            container.innerHTML = '';

            this.goods.forEach(function(item, i, goods) {

                const divImage = document.createElement('div');
                const divProductContianer = document.createElement('div');
                const divProduct = document.createElement('div');
                const divButtonBy = document.createElement('div');

                const tagBr = document.createElement('br');

                divButtonBy.textContent = this.getSetting('buyButttonName');
                divButtonBy.style.backgroundColor = this.getSetting('buyButttonColor');
                divButtonBy.style.width = '100px';
                divButtonBy.addEventListener('click', () => this.addToBasket(item));
    
                divProduct.textContent = item[1];
                
                /* пикчи*/
                tableBoard = document.createElement('table');
                tableBoard.id = "tableBoard";
                tableBoard.classList.add("tableGallery");
                divImage.appendChild(tableBoard);      

                const tr = document.createElement('tr');
                tableBoard.appendChild(tr);
                images = item.images;
                images.forEach(function(image, i, images) {

                    const tagImg = document.createElement('img');
                    tagImg.src = this.getImagesPathSmall() + '\\' + image;
                    tagImg.dataset.full_image_url=this.getImagesPathBig() + '\\' + image;
                    tagImg.dataset.img_num = i;
                    tagImg.dataset.img_count = images.length - 1;
                    tagImg.dataset.prod_id = item.id;

                    const td = document.createElement('td');
                    td.classList.add("imageProduct");
                    td.appendChild(tagImg);    
                    tr.appendChild(td);

                }, this);
                
                divProductContianer.appendChild(divImage);
                divProductContianer.appendChild(divProduct);
                divProductContianer.appendChild(divButtonBy);
                divProductContianer.appendChild(tagBr);

                container.appendChild(divProductContianer);        

            }, this);            
        },
    };


const parentElementCatalog = document.getElementById("catalog");
const parentElementBasket = document.getElementById("basket");

const settingsBasket = {
    container: parentElementBasket,
    };

const settingsCatalog = {
    container: parentElementCatalog,
    };

Basket.init(settingsBasket);
Catalog.init(settingsCatalog, Basket);

Catalog.add(1, 'good 1', ['img1_1.jpg', 'img1_2.jpg', 'img1_3.jpg'], 1, 30);
Catalog.add(2, 'good 2', ['img2_1.jpg', 'img2_2.jpg', 'img2_3.jpg'], 2, 12);
Catalog.add(3, 'good 3', ['img3_1.jpg', 'img3_2.jpg', 'img3_3.jpg'], 7, 16);

Catalog.draw();

console.log('---------------------------------------------');

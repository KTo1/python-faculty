/*
2 *У товара может быть несколько изображений. Нужно:
a. Реализовать функционал показа полноразмерных картинок товара в модальном окне
b. Реализовать функционал перехода между картинками внутри модального окна ("листалка")
*/

'use strict';
const gallery = {
    settings: {
        previewSelector: '.mySuperGallery',
        openedImageWrapperClass: 'galleryWrapper',
        openedImageClass: 'galleryWrapper__image',
        openedImageScreenClass: 'galleryWrapper__screen',
        openedImageCloseBtnClass: 'galleryWrapper__close',
        openedImageCloseBtnSrc: 'images/gallery/close.png',
        openedImageRightBtnClass: 'galleryWrapper__right',
        openedImageRightBtnSrc: 'images/gallery/right.png',
        openedImageLeftBtnClass: 'galleryWrapper__left',
        openedImageLeftBtnSrc: 'images/gallery/left.png',
    },

    init(userSettings = {}) {
        Object.assign(this.settings, userSettings);

        let gallery_element = document.querySelectorAll(this.settings.previewSelector);
        gallery_element.forEach(function(Item) {  
            Item.addEventListener(
                'click',
                (event) => this.containerClickHandler(event)
            );
        }, this);            
    },

    containerClickHandler(event) {
        if (event.target.tagName !== 'IMG') return;

        this.openImage(event.target.dataset);
    },

    openImage(dataset) {
        const element = this.getScreenContainer()
            .querySelector(`.${this.settings.openedImageClass}`)
        element.src = dataset.full_image_url;
        element.dataset.img_num = dataset.img_num;
        element.dataset.img_count = dataset.img_count;
        element.dataset.prod_id = dataset.prod_id;
    },

    getScreenContainer() {
        const galleryWrapperElement = document
            .querySelector(`.${this.settings.openedImageWrapperClass}`);

        if (galleryWrapperElement) return galleryWrapperElement;

        return this.createScreenContainer();
    },

    addBtnGallery(Container, Class, Img, Func){
        const closeImageElement = new Image();
        closeImageElement.classList.add(Class);
        closeImageElement.src = Img;
        closeImageElement.addEventListener('click', Func.bind(this));
        Container.appendChild(closeImageElement);
    },

    createScreenContainer() {
        const galleryWrapperElement = document.createElement('div');
        galleryWrapperElement.classList.add(this.settings.openedImageWrapperClass);

        const galleryScreenElement = document.createElement('div');
        galleryScreenElement.classList.add(this.settings.openedImageScreenClass);
        galleryWrapperElement.appendChild(galleryScreenElement);

        /* btn */
        this.addBtnGallery(galleryWrapperElement, this.settings.openedImageRightBtnClass, this.settings.openedImageRightBtnSrc, this.right);
        this.addBtnGallery(galleryWrapperElement, this.settings.openedImageLeftBtnClass, this.settings.openedImageLeftBtnSrc, this.left);
        this.addBtnGallery(galleryWrapperElement, this.settings.openedImageCloseBtnClass, this.settings.openedImageCloseBtnSrc, this.close);
        /* btn */

        const image = new Image();
        image.classList.add(this.settings.openedImageClass);
        
        galleryWrapperElement.appendChild(image);        

        document.body.appendChild(galleryWrapperElement);

        return galleryWrapperElement;
    },

    close() {
        document.querySelector(`.${this.settings.openedImageWrapperClass}`)
            .remove();
    },

    move(offset){
        const elementGallery = document.querySelector(`.${this.settings.openedImageClass}`)
        
        let img_count = elementGallery.dataset.img_count;
        let img_num = Number(elementGallery.dataset.img_num) + offset;
        let prod_id = elementGallery.dataset.prod_id;

        if (img_num > img_count) { img_num = 0};
        if (img_num < 0) { img_num = img_count};
        
        const elementProd = document.querySelector(`[data-prod_id="${prod_id}"][data-img_num="${img_num}"]`);
        
        elementGallery.src = elementProd.dataset.full_image_url;
        Object.assign(elementGallery.dataset, elementProd.dataset);
        
    },

    right() {
        this.move(1);
    },
    
    left() {
        this.move(-1);
    },    
};

gallery.init({ previewSelector: '.tableGallery' });

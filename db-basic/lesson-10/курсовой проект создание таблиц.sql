-- Система управления складом
-- 1. Снижение рисков пересорта при сборе заказов
-- 2. Обеспечение незалеживаемости товаров
-- 3. Оперативная информация об остатках товара на складах
	
-- Основые операции:
-- Размещение товаров на складах
-- Заказ товара клиентом
-- Сбор заказа нашей фирмой
-- Инвентаризация

 	
DROP DATABASE IF EXISTS store;
CREATE DATABASE store;
USE store;

DROP TABLE IF EXISTS options;
CREATE TABLE options(
	id SERIAL PRIMARY KEY, 
    name VARCHAR(150),
	description VARCHAR(150),
	ITN  VARCHAR(15),
	IEC  VARCHAR(15),
	scanprefix_cells VARCHAR(4),
	scanprefix_weight VARCHAR(4) 
) COMMENT 'Наша организация, общие настройки';

DROP TABLE IF EXISTS users;
CREATE TABLE users(
	id SERIAL PRIMARY KEY, 
	name VARCHAR(150),
	description VARCHAR(150)
) COMMENT 'Пользователи';	  

DROP TABLE IF EXISTS storehouses;
CREATE TABLE storehouses(
	id SERIAL PRIMARY KEY, 
    name VARCHAR(150),
	description VARCHAR(150),
	address VARCHAR(200),
	phone VARCHAR(150),
	storekeeper_id BIGINT UNSIGNED, 
	
	FOREIGN KEY (storekeeper_id) REFERENCES users(id) ON DELETE SET NULL ON UPDATE CASCADE,    
	INDEX storehouses_name_idx(name)
) COMMENT 'Склады';

DROP TABLE IF EXISTS goods;
CREATE TABLE goods(
	id SERIAL PRIMARY KEY, 
	name VARCHAR(150),
	description VARCHAR(150),
	
	INDEX goods_name_idx(name)
) COMMENT 'Товары';

DROP TABLE IF EXISTS partners;
CREATE TABLE partners(
	id SERIAL PRIMARY KEY, 
	name VARCHAR(150),
	description VARCHAR(150),
	address VARCHAR(200),
	phone VARCHAR(150),
	
	INDEX partners_name_idx(name)
) COMMENT 'Партнеры';	  

DROP TABLE IF EXISTS cells;
CREATE TABLE cells(
	id SERIAL PRIMARY KEY, 
	name VARCHAR(10),
	description VARCHAR(50),
	
	INDEX cells_name_idx(name)
) COMMENT 'Ячейки';	  

DROP TABLE IF EXISTS cells_storehouses;
CREATE TABLE cells_storehouses(
	id SERIAL PRIMARY KEY, 
	cells_id BIGINT UNSIGNED NOT NULL,
	storehouses_id BIGINT UNSIGNED NOT NULL,
	
	FOREIGN KEY (cells_id) REFERENCES cells(id) ON DELETE CASCADE ON UPDATE CASCADE,  
	FOREIGN KEY (storehouses_id) REFERENCES storehouses(id) ON DELETE CASCADE ON UPDATE CASCADE	
) COMMENT 'Ячейки на складах';	  

DROP TABLE IF EXISTS orders_statuses;
CREATE TABLE orders_statuses(
	id SERIAL PRIMARY KEY, 
	name VARCHAR(50)
) COMMENT 'Статусы';	  

DROP TABLE IF EXISTS orders;
CREATE TABLE orders(
	id SERIAL PRIMARY KEY, 
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	status_id BIGINT UNSIGNED,
	partners_id BIGINT UNSIGNED,
	description VARCHAR(150),
	
	FOREIGN KEY (partners_id) REFERENCES partners(id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (status_id) REFERENCES orders_statuses(id) ON DELETE SET NULL ON UPDATE CASCADE
) COMMENT 'Заказы';	  

DROP TABLE IF EXISTS orders_goods;
CREATE TABLE orders_goods(
	id SERIAL PRIMARY KEY, 
	order_id BIGINT UNSIGNED NOT NULL,
	storehouse_id BIGINT UNSIGNED,
	user_id BIGINT UNSIGNED,
	goods_id BIGINT UNSIGNED,
	quantity SMALLINT,
	quantity_collected SMALLINT DEFAULT 0,
	
	FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE ON UPDATE CASCADE,	
	FOREIGN KEY (storehouse_id) REFERENCES storehouses(id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL ON UPDATE CASCADE,	
	FOREIGN KEY (goods_id) REFERENCES goods(id) ON DELETE SET NULL ON UPDATE CASCADE
) COMMENT 'Заказы строки';	 

DROP TABLE IF EXISTS remains;
CREATE TABLE remains(
	id SERIAL PRIMARY KEY, 
	storehouse_id BIGINT UNSIGNED,
	exp_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	cells_id BIGINT UNSIGNED,	
	goods_id BIGINT UNSIGNED,
	quantity SMALLINT,
	
	FOREIGN KEY (cells_id) REFERENCES cells(id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (storehouse_id) REFERENCES storehouses(id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (goods_id) REFERENCES goods(id) ON DELETE SET NULL ON UPDATE CASCADE
) COMMENT 'Остатки товаров на складах';	 

DROP TABLE IF EXISTS barcodes;
CREATE TABLE barcodes(
	id SERIAL PRIMARY KEY, 
	code VARCHAR(128),
	
	INDEX barcodes_code_idx(code)
) COMMENT 'Штрих коды';	 

DROP TABLE IF EXISTS barcodes_goods;
CREATE TABLE barcodes_goods(
	id SERIAL PRIMARY KEY, 
	barcodes_id BIGINT UNSIGNED NOT NULL,
	goods_id BIGINT UNSIGNED NOT NULL,

	FOREIGN KEY (barcodes_id) REFERENCES barcodes(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (goods_id) REFERENCES goods(id) ON DELETE CASCADE ON UPDATE CASCADE
) COMMENT 'Штрих коды товаров';	

DROP TABLE IF EXISTS barcodes_cells;
CREATE TABLE barcodes_cells(
	id SERIAL PRIMARY KEY, 
	barcodes_id BIGINT UNSIGNED NOT NULL,
	cells_id BIGINT UNSIGNED NOT NULL,

	FOREIGN KEY (barcodes_id) REFERENCES barcodes(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (cells_id) REFERENCES cells(id) ON DELETE CASCADE ON UPDATE CASCADE
) COMMENT 'Штрих коды ячеек';	

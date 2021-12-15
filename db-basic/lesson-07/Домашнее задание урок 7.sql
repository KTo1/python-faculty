-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
use shop;

select * from users as u where exists (select id from orders as o where u.id = o.user_id)


-- Выведите список товаров products и разделов catalogs, который соответствует товару.
use shop;

select p.name as product_name, c.name as catalog_name from products as p 
left join catalogs as c
on
	p.catalog_id = c.id

    
-- (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
-- Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов flights с русскими названиями городов.
use shop;

select c_from.name as `from`, c_to.name as `to` from flights as f 
left join cities as c_from 
on
	f.from = c_from.label 
left join cities as c_to 
on
	f.to = c_to.label 
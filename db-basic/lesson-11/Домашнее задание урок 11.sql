-- Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, catalogs и products в таблицу logs помещается
-- время и дата создания записи, название таблицы, идентификатор первичного ключа и содержимое поля name.
use shop;

drop table if exists logs;

create table logs (
	id SERIAL,
	name_table varchar(50),
	id_table BIGINT UNSIGNED NOT NULL, 
	name varchar(255), 
	created_at DATETIME DEFAULT NOW()
) engine ARCHIVE;

drop trigger if exists after_insert_catalogs; 
drop trigger if exists after_insert_products; 
drop trigger if exists after_insert_users; 

delimiter \\
create trigger after_insert_catalogs after insert on catalogs
for each row begin 
    set @tbl_name = 'catalogs';
	insert into logs (name_table, id_table, name) values (@tbl_name, new.id, new.name);
end\\

create trigger after_insert_products after insert on products
for each row begin 
    set @tbl_name = 'products';
	insert into logs (name_table, id_table, name) values (@tbl_name, new.id, new.name);
end\\

create trigger after_insert_users after insert on users
for each row begin 
    set @tbl_name = 'users';
	insert into logs (name_table, id_table, name) values (@tbl_name, new.id, new.name);
end\\

delimiter ;


-- (по желанию) создайте sql-запрос, который помещает в таблицу users миллион записей.
-- после некоторых экспериментов вот такое решение родилось

use vk;

drop procedure if exists they_are_billions; 

delimiter //  
    
create procedure they_are_billions()  
begin  
    declare count_users, cur_count int;  
    
    set count_users = 1000000;  
	set cur_count = 0;
    
    start transaction;
    
    while cur_count < count_users do  
		set @username = concat('user', cur_count) ;
        insert into users(firstname) values 
                (@username), (@username), (@username), (@username), (@username), (@username), (@username), (@username), (@username), (@username) ;
        set cur_count = cur_count + 10;  
    end while;  
    
    commit;
    
end //  

delimiter ;

call they_are_billions() ;


-- В базе данных Redis подберите коллекцию для подсчета посещений с определенных IP-адресов.
-- Мое предложение в качестве ключей использовать адреса в качестве значений количество посещений
select 0
set 192.168.0.1 1

-- При повторном посещении:
incr 192.168.0.1

-- При помощи базы данных Redis решите задачу поиска имени пользователя по электронному адресу и наоборот, поиск электронного адреса пользователя по его имени.
-- Если я все верно понял то в рэдис в рамках одной БД это решается плохо. У меня два варианта родилось:
-- 1. Я бы создал две базы: в одной было бы в качестве ключа адрес в другой имя пользователя.
-- 2. Хранить в ключе сразу имя и почту) Выбирать по регулярному выражению, пример:
select 0
set admin:admin@ya.ru 1
-- поиск почты:
keys admin:*
-- поиск имени пользователя:
keys *:admin@ya.ru

-- Организуйте хранение категорий и товарных позиций учебной базы данных shop в СУБД MongoDB.use shop
-- думаю как то-так, на мой взгляд реляционная БД для этой задачи походит лучше
db.shop.insert({name: 'Intel Core i3-8100	Процессор для настольных персональных компьютеров, основанных на платформе Intel.', price:7890.00, catalog: 'Процессоры', created_at: '2021-11-2200:44:09', updated_at: '2021-11-22 00:44:09'})
db.shop.insert({name: 'Intel Core i5-7400	Процессор для настольных персональных компьютеров, основанных на платформе Intel.', price:12700.00, catalog: 'Процессоры', created_at: '2021-11-22 00:44:09', updated_at: '2021-11-22 00:44:09'})
db.shop.insert({name: 'AMD FX-8320E	Процессор для настольных персональных компьютеров, основанных на платформе AMD.', price:4780.00, catalog: 'Процессоры', created_at: '2021-11-22 00:44:09', updated_at: '2021-11-22 00:44:09'})
db.shop.insert({name: 'AMD FX-8320	Процессор для настольных персональных компьютеров, основанных на платформе AMD.', price:7120.00, catalog: 'Процессоры', created_at: '2021-11-22 00:44:09', updated_at: '2021-11-22 00:44:09'})
db.shop.insert({name: 'ASUS ROG MAXIMUS X HERO	Материнская плата ASUS ROG MAXIMUS X HERO, Z370, Socket 1151-V2, DDR4, ATX', price:19310.00, catalog: 'Материнские платы', created_at: '2021-11-22 00:44:09', updated_at: '2021-11-22 00:44:09'})
db.shop.insert({name: 'Gigabyte H310M S2H	Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX', price:4790.00,	catalog: 'Материнские платы', created_at: '2021-11-22 00:44:09', updated_at: '2021-11-22 00:44:09'})
db.shop.insert({name: 'MSI B250M GAMING PRO	Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX', price:5060.00, catalog: 'Материнские платы', created_at: '2021-11-22 00:44:09', updated_at: '2021-11-22 00:44:09'})

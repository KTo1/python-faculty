-- ************************* Практическое задание по теме “Транзакции, переменные, представления”
 
-- В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.
start transaction;

insert into sample.users(id, name, birthday_at, created_at, updated_at) 
select id, name, birthday_at, created_at, updated_at 
  from shop.users 
 where id = 1;
 
delete 
  from shop.users 
 where id = 1;
 
commit;


-- Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.
use shop;

create view names as 
select p.name as product_name, c.name as catalog_name 
  from products as p
  left join catalogs as c 
    on p.catalog_id = c.id;


-- Пусть имеется таблица с календарным полем created_at. В ней размещены разряженые календарные записи за август 2018 года '2018-08-01', '2016-08-04', '2018-08-16' и 2018-08-17. 
-- Составьте запрос, который выводит полный список дат за август, выставляя в соседнем поле значение 1, если дата присутствует в исходном таблице и 0, если она отсутствует.
-- Полагаю, что есть решение изящнее )
use shop;

create temporary table tmp_numbers (id int);
insert tmp_numbers 
values (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21), (22), (23), (24), (25), (26), (27), (28), (29), (30), (31);

select concat_ws('-', '2021', '08', right(concat('0', n.id), 2)) as date, if(o.id is null, 0, 1) as exist 
  from tmp_numbers as n 
  left join orders as o 
    on dayofmonth(o.created_at) = n.id;
	
drop table tmp_numbers;


-- Пусть имеется любая таблица с календарным полем created_at. Создайте запрос, который удаляет устаревшие записи из таблицы, оставляя только 5 самых свежих записей.
-- предлагаю решение через временную таблицу
use shop;

create temporary table tmp_table (id bigint unsigned);

insert into tmp_table 
select id 
  from orders 
 order by created_at desc 
 limit 5;

delete 
  from orders 
 where id not in (select id from tmp_table); 
 
drop table tmp_table;



-- ************************* Практическое задание по теме “Администрирование MySQL” (эта тема изучается по вашему желанию)

-- Создайте двух пользователей которые имеют доступ к базе данных shop. Первому пользователю shop_read должны быть доступны только запросы на чтение данных,
-- второму пользователю shop — любые операции в пределах базы данных shop.
create user shop_read@localhost identified with sha256_password by '123';
create user shop@localhost identified with sha256_password by '123';

grant all on shop.* to shop@localhost;
grant select on shop.* to shop_read@localhost;


-- Пусть имеется таблица accounts содержащая три столбца id, name, password, содержащие первичный ключ, имя пользователя и его пароль. 
-- Создайте представление username таблицы accounts, предоставляющий доступ к столбца id и name. Создайте пользователя user_read, который бы не имел доступа к таблице accounts,
-- однако, мог бы извлекать записи из представления username.

use shop;

create view security_accounts as 
select id, name 
  from accounts;
  
create user user_read@localhost identified with sha256_password by '123';
grant select on shop.security_accounts to user_read@localhost;



-- ************************* Практическое задание по теме “Хранимые процедуры и функции, триггеры"

-- Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
-- С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
use shop;

drop function if exists hello;

create function hello()
returns varchar(11) deterministic	
return (select 
			case 
				when HOUR(now()) >= 6 and HOUR(now()) < 12 
					then 'Доброе утро'
				when HOUR(now()) >= 12 and HOUR(now()) < 18 
					then 'Добрый день'
				when HOUR(now()) >= 18 and HOUR(now()) < 0 
					then 'Добрый вечер"'
				when HOUR(now()) >= 0 and HOUR(now()) < 6 
					then 'Доброй ночи'        
				end as greetings);
                
select hello();

drop function hello;


-- В таблице products есть два текстовых поля: name с названием товара и description с его описанием. Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
-- Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. При попытке присвоить полям NULL-значение необходимо отменить операцию.
use shop;

delimiter = \\
create trigger product_insert_trigger before insert on products
for each row begin
	if (new.name is null) and (new.desription is null) then
		signal sqlstate '45000' set message_text = 'Fields ''name'' or ''decriprion'' must be fill!';
    end if;
end;


-- (по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел. 
-- Вызов функции FIBONACCI(10) должен возвращать число 55.
use shop;

drop function if exists fibonacci;

delimiter = \\
create function fibonacci(num int)
returns bigint deterministic	
begin
	set @SQRT5 = sqrt(5);
    set @PHI = (@SQRT5 + 1) / 2;
    return FLOOR(pow(@PHI, num) / @SQRT5 + 0.5);
end;
                
select fibonacci(10);
select fibonacci(50);

drop function fibonacci;
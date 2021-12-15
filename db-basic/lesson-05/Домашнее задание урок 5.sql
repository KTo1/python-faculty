-- Практическое задание по теме “Операторы, фильтрация, сортировка и ограничение”

-- Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
-- Поскольку поле updated_at зависит от created_at, то достаточно установить его

update users set created_at = now()

-- Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 08:10". 
-- Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.
use vk;

alter table users
rename column created_at TO created_at_str,
rename column updated_at TO updated_at_str,
add column created_at DATETIME DEFAULT NOW(),
add column updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP;

update users set created_at = str_to_date(created_at_str, '%d.%m.%Y %h:%i'), updated_at = str_to_date(updated_at_str, '%d.%m.%Y %h:%i');
 
alter table users
drop column created_at_str,
drop column updated_at_str

-- В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы. 
-- Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. Однако, нулевые запасы должны выводиться в конце, после всех записей.
-- Поскольку в нашей БД нет таблицы storehouses_products, я добавил поле value в таблицу users 
SELECT firstname, value, if (value = 0, 2, 1) FROM users where value is not null group by 1, 3 order by 3, 2;

-- (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. Месяцы заданы в виде списка английских названий ('may', 'august')
SELECT * FROM profiles where monthname(birthday) in ('may', 'august')

-- (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN.
use vk;
SELECT * FROM users WHERE id IN (326, 311, 403) order by field(id, 326, 311, 403);


-- Практическое задание теме “Агрегация данных”.

-- Подсчитайте средний возраст пользователей в таблице users
-- Видимо имелось ввиду profiles? Соединения мы еще не проходили
SELECT avg(datediff(now(), birthday) / 365)  FROM profiles

-- Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.
SELECT dayofweek(DATE_FORMAT(birthday,'2021-%m-%d %T')), count(*) FROM profiles group by 1

--(по желанию) Подсчитайте произведение чисел в столбце таблицы
use vk;
SELECT exp(sum(log(users.value))) FROM users

/* Задача 1
Установите СУБД MySQL. Создайте в домашней директории файл .my.cnf, задав в нем логин и пароль, который указывался при установке.

[client]
user=root
password=1234

Согласно официальной документации в ОС Windows файл может располагаться тут:
https://dev.mysql.com/doc/refman/8.0/en/option-files.html
Table 4.1 Option Files Read on Windows Systems

Я разместил в BASEDIR

*/

/* Задача 2
Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, числового id и строкового name.
*/

-- создаем базу
create database if not exists example; 

-- созадем таблицу, если такая таблица уже существует, то удаляем
drop table if exists example.users;
create table example.users(
	id serial primary key,
	name varchar(255) 
)

/* Задача 3
Создайте дамп базы данных example из предыдущего задания, разверните содержимое дампа в новую базу данных sample.
*/

mysqldump.exe example > example.sql

mysql
create database sample;
exit

mysql.exe sample < example.sql

/* Задача 4
(по желанию) Ознакомьтесь более подробно с документацией утилиты mysqldump. Создайте дамп единственной таблицы help_keyword базы данных mysql. 
Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.

*/

-- Любое всегда истинное условие + лимит

mysqldump --where="true limit 100" mysql help_keyword > sql_help_keyword.sql 




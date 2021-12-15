-- i. Заполнить все таблицы БД vk данными (по 10-20 записей в каждой таблице) 
-- Запросы в приложенном файле

-- ii. Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке
use vk;
select distinct firstname from users order by 1;

-- iii. Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false). Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)

alter table profiles 
add column is_active tinyint default 1;
update profiles set is_active = 0 where datediff(now(), birthday) / 365 < 18; 

-- iv. Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)
delete from messages where  created_at > now();

-- v. Написать название темы курсового проекта (в комментарии)
-- Система управления складом. 
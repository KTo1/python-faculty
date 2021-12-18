-- ВЫПОЛНИТЬ СКРИПТ "тестовые данные", ВНИМАНИЕ!!! Скрипт сотрет все данные в базе!
-- выполнять частями, по процессу. 

-- Выбираем организацию (вариант настроек)
set @result = '';
call select_options(1, @result);
select @result;

-- Выбираем/создаем пользователей
set @result = '';
call select_user(3, 'Гаврилов Иван Семёнович', 3, @result);
call select_user(5, 'Лопатин Андрей Мирославович', 5, @result);
select @result;

-- сейчас размещенные заказы видны в представлении orders_placed
select * from orders_placed;


-- Будем работать с заказом №4
-- распределяем по складам, остатки смотрим в представлении remains
update orders_goods set storehouses_id = 3 where orders_id = 4 and id = 7;
update orders_goods set storehouses_id = 5 where orders_id = 4 and id = 8;

-- Проверяем, поле склад заполнено  
Select * from orders_goods where orders_id = 4;

-- устанавливаем статус готов к сборке
set @result = '';
call change_order_status(4, 2, @result);
select @result;

-- сейчас заказы видны в представлении orders_ready
select * from orders_ready;

-- назначаем комплектовщиков
set @result = '';
call set_order_picker(4, 3, @result);
select @result;
call set_order_picker(4, 5, @result);
select @result;

-- Проверяем, поле пользователь заполнено  
Select * from orders_goods where orders_id = 4;

-- теперь запрос "Сборочная ведомость" для каждого комплектовщика не пустой
set @result = '';
call select_user(3, 'Гаврилов Иван Семёнович', 3, @result);
call assembly_statement(@result);

call select_user(5, 'Лопатин Андрей Мирославович', 5, @result);
call assembly_statement(@result);

-- выполняем сборку
insert into orders_goods_collected(orders_goods_id, cells_id, exp_date, quantity) values (7, 4, '2023-03-08', 3);
insert into orders_goods_collected(orders_goods_id, cells_id, exp_date, quantity) values (8, 6, '2024-02-24', 1);

-- проверяем
select * from orders_goods_collected;

-- завершаем сборку на первом складе
set @result = '';
call pickup_completed(4, 3, @result);
select @result;

-- завершаем сборку на втором складе
set @result = '';
call pickup_completed(4, 5, @result);
select @result;

-- Заказ переведен в статус выполнен, остатки списаны со склада, записи в собранных товарах не активны, убеждаемся в этом в представлении remians
select * from orders_goods_collected;
select * from remains;
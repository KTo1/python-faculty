use store;

-- about
insert into options (name, description, ITN, IEC, scanprefix_cells, scanprefix_weight, statuses_ready_id, statuses_placed_id, statuses_completed_id) 
values ('Название нашей фирмы краткое', 'Название нашей фирмы полное', 'наш ИНН', 'наш КПП', '155', '250', 2, 1, 4);

-- order_statuses
insert into orders_statuses(id, name) values (1, 'Размещен');
insert into orders_statuses(id, name) values (2, 'Готов к сборке');
insert into orders_statuses(id, name) values (3, 'Собирается');
insert into orders_statuses(id, name) values (4, 'Выполнен');
insert into orders_statuses(id, name) values (5, 'Отменен');

-- errors
insert into errors (id, description) values ('45001', 'Статус не существует');
insert into errors (id, description) values ('45002', 'Заказ не существует');
insert into errors (id, description) values ('45003', 'Срок годности уже истек');
insert into errors (id, description) values ('45004', 'Ячейка обязательна для заполнения');
insert into errors (id, description) values ('45005', 'Склад не существует');
insert into errors (id, description) values ('45006', 'Ячейка не существует');
insert into errors (id, description) values ('45007', 'Товар не существует');
insert into errors (id, description) values ('45008', 'Пользователь не существует');
insert into errors (id, description) values ('45009', 'Пользователь уже назначен на другой заказ');
insert into errors (id, description) values ('45010', 'У пользователя не задан склад');
insert into errors (id, description) values ('45011', 'Вариант настроек не существует');
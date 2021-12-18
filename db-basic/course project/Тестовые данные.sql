-- тестовые данные
use store;

set FOREIGN_KEY_CHECKS = 0; 
truncate table  options;
truncate table  errors;
truncate table  storehouses_cells;
truncate table  barcodes_goods;
truncate table  barcodes_cells;
truncate table  orders_goods;
truncate table  storehouses;
truncate table  users;
truncate table  cells;
truncate table  goods;
truncate table  partners;
truncate table  remains_flow;
truncate table  orders;
truncate table  barcodes;
truncate table  orders_statuses;
set FOREIGN_KEY_CHECKS = 1; 

-- about
insert into options(name, description, ITN, IEC, scanprefix_cells, scanprefix_weight, statuses_ready_id, statuses_placed_id, statuses_completed_id) values ('Северный центр позитроники', 'Вместе к светлому будущему!', '7017071707', '4564654', '155', '250', 2, 1, 4);
	
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

-- users
set @result = '';
call select_user(1, 'Дроздов Александр Тимофеевич', 1, @result);
call select_user(2, 'Крылов Тигран Александрович', 2, @result);
call select_user(3, 'Гаврилов Иван Семёнович', 3, @result);
call select_user(4, 'Соловьев Владимир Артемьевич', 4, @result);
call select_user(5, 'Лопатин Андрей Мирославович', 5, @result);
call select_user(6, 'Быков Максим Тимофеевич', 6, @result);
call select_user(7, 'Марков Михаил Тимофеевич', 7, @result);
call select_user(8, 'Фролова Алия Львовна', 8, @result);
call select_user(9, 'Смирнов Борис Макарович', 9, @result);
call select_user(10, 'Левина Ариана Михайловна', 10, @result);

-- products
insert into goods(name) values ('Сетевое хранилище WD My Cloud EX2 Ultra WDBSHB0000NCH-EEUE');
insert into goods(name) values ('Сетевое хранилище WD My Cloud Home Duo WDBMUT0120JWT-EESN');
insert into goods(name) values ('Сетевое хранилище Qnap D2 Rev. B');
insert into goods(name) values ('Сетевое хранилище ZYXEL NAS326-EU0101F');
insert into goods(name) values ('Сетевое хранилище ZYXEL NAS542-EU0101F');
insert into goods(name) values ('Сетевое хранилище Qnap D4');
insert into goods(name) values ('Сетевое хранилище Qnap D2 Pro');
insert into goods(name) values ('Сетевое хранилище Qnap D1 Rev.B');
insert into goods(name) values ('Сетевое хранилище Qnap D4 Pro');
insert into goods(name) values ('Сетевое хранилище Qnap TS-451+-2G');

-- storehouses
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Томск №1', 'Томск, Ленина 112', '69(0761)934-65-96', 1);
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Томск №2', 'Томск, Пушкина 31', '18(02)292-47-96', 2);
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Томск №3', 'Томск, Говорова 39', '42(322)438-87-54', 3);
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Екатеринбуг №1', 'Екатеринбуг, Ленина 112', '198(29)122-46-04', 4);
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Екатеринбуг №2', 'Екатеринбуг, Пушкина 31', '5(5128)138-01-66', 5);
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Екатеринбуг №3', 'Екатеринбуг, Говорова 39', '38(189)203-55-05', 6);
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Москва №1', 'Москва, Ленина 112', '318(2077)062-22-99', 7);
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Москва №2', 'Москва, Пушкина 31', '75(6498)230-28-06', 8);
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Москва №3', 'Москва, Говорова 39', '8(392)136-46-93', 9);
insert into storehouses(name, address, phone, storekeeper_id) values ('Склад Москва №4', 'Москва, Лермонтова 56', '50(36)251-58-18', 10);

-- partners
insert into partners(name, address, phone) values ('ООО "ДИАМИС"',	'Шатура, спуск Ладыгина, 22', '247(91)212-58-71');
insert into partners(name, address, phone) values ('ООО "ЭВИКОН"',	'Ногинск, спуск Ладыгина, 16', '073(86)493-55-27');
insert into partners(name, address, phone) values ('ООО "НИРГО"', 'Талдом, пл. 1905 года, 3', '09(7178)004-59-17');
insert into partners(name, address, phone) values ('ООО "ДЕАНТ"', 'Егорьевск, бульвар Гоголя, 44', '240(372)653-27-05');
insert into partners(name, address, phone) values ('ИП "Кулаков Максимилиан Михайлович"', 'Луховицы, въезд Чехова, 94', '045(24)258-74-05');
insert into partners(name, address, phone) values ('ИП "Лобанов Иосиф Андреевич"',	'Воскресенск, пер. Будапештсткая, 36', '2(26)981-63-48');
insert into partners(name, address, phone) values ('ИП "Кузнецов Леонард Эльдарович"',	'Луховицы, проезд Бухарестская, 34', '5(968)710-13-60');
insert into partners(name, address, phone) values ('ИП "Моисеев Зиновий Ефимович"', 'Егорьевск, въезд Ломоносова, 75', '1(63)659-04-72');
insert into partners(name, address, phone) values ('ФЛ Ершов Болеслав Мартынович',	'Дмитров, пр. Гагарина, 85', '1(9324)839-64-98');
insert into partners(name, address, phone) values ('ФЛ Лихачёв Вячеслав Викторович', 'Павловский Посад, спуск Балканская, 99', '689(9502)513-09-51');

-- cells
insert into cells(name) values ('AA');
insert into cells(name) values ('AB');
insert into cells(name) values ('AC');
insert into cells(name) values ('AD');
insert into cells(name) values ('AE');
insert into cells(name) values ('BA');
insert into cells(name) values ('BB');
insert into cells(name) values ('BC');
insert into cells(name) values ('BD');
insert into cells(name) values ('BE');

-- storehouses_cells
insert into storehouses_cells(storehouses_id, cells_id ) values (1, 1);
insert into storehouses_cells(storehouses_id, cells_id ) values (1, 2);
insert into storehouses_cells(storehouses_id, cells_id ) values (2, 1);
insert into storehouses_cells(storehouses_id, cells_id ) values (2, 2);
insert into storehouses_cells(storehouses_id, cells_id ) values (3, 3);
insert into storehouses_cells(storehouses_id, cells_id ) values (3, 4);
insert into storehouses_cells(storehouses_id, cells_id ) values (4, 3);
insert into storehouses_cells(storehouses_id, cells_id ) values (4, 4);
insert into storehouses_cells(storehouses_id, cells_id ) values (5, 6);
insert into storehouses_cells(storehouses_id, cells_id ) values (5, 7);
insert into storehouses_cells(storehouses_id, cells_id ) values (6, 6);
insert into storehouses_cells(storehouses_id, cells_id ) values (6, 7);
insert into storehouses_cells(storehouses_id, cells_id ) values (7, 10);
insert into storehouses_cells(storehouses_id, cells_id ) values (8, 10);
insert into storehouses_cells(storehouses_id, cells_id ) values (9, 10);
insert into storehouses_cells(storehouses_id, cells_id ) values (10, 10);

-- remains_flow
set @result = '';
call modify_remains(1, 1, 1, '2022-01-04', 10, @result);
call modify_remains(1, 2, 2, '2022-08-04', 10, @result);
call modify_remains(2, 1, 3, '2022-07-01', 10, @result);
call modify_remains(2, 2, 4, '2023-06-04', 10, @result);
call modify_remains(3, 3, 4, '2023-05-03', 10, @result);
call modify_remains(3, 4, 5, '2023-12-10', 10, @result);
call modify_remains(4, 3, 4, '2023-04-14', 10, @result);
call modify_remains(4, 4, 5, '2023-03-08', 10, @result);
call modify_remains(5, 6, 6, '2024-02-24', 10, @result);
call modify_remains(5, 7, 7, '2024-11-15', 10, @result);
call modify_remains(6, 6, 8, '2024-09-04', 10, @result);
call modify_remains(6, 7, 9, '2024-07-08', 10, @result);
call modify_remains(7, 10, 10, '2024-01-14', 5, @result);
call modify_remains(7, 10, 10, '2024-02-24', 5, @result);
call modify_remains(8, 10, 10, '2022-03-12', 5, @result);
call modify_remains(8, 10, 10, '2022-04-04', 5, @result);
call modify_remains(9, 10, 10, '2022-06-07', 5, @result);
call modify_remains(9, 10, 10, '2022-08-03', 5, @result);
call modify_remains(10, 10, 10, '2022-09-02', 5, @result);
call modify_remains(10, 10, 10, '2022-07-01', 5, @result);

-- orders как размещается заказ? на фирму
insert into orders(id, partners_id, date) values (1, 1, '2021-12-01');
insert into orders(id, partners_id, date) values (2, 2, '2021-12-02');
insert into orders(id, partners_id, date) values (3, 3, '2021-12-03');
insert into orders(id, partners_id, date) values (4, 4, '2021-12-04');
insert into orders(id, partners_id, date) values (5, 5, '2021-12-05');
insert into orders(id, partners_id, date) values (6, 6, '2021-12-06');
insert into orders(id, partners_id, date) values (7, 7, '2021-12-07');
insert into orders(id, partners_id, date) values (8, 8, '2021-12-08');
insert into orders(id, partners_id, date) values (9, 9, '2021-12-09');
insert into orders(id, partners_id, date) values (10, 10, '2021-12-10');
-- orders_goods
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (1, 1, 1, 1);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (1, 1, 2, 1);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (2, 1, 1, 1);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (2, 1, 2, 1);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (3, 1, 3, 2);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (3, 1, 4, 2);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (4, 1, 5, 3);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (4, 1, 6, 1);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (5, 1, 1, 1);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (6, 1, 1, 6);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (7, 1, 7, 4);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (7, 1, 8, 1);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (7, 1, 9, 1);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (8, 1, 2, 2);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (9, 1, 2, 2);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (10, 1, 9, 1);
insert into orders_goods(orders_id, statuses_id, goods_id, quantity) values (10, 1, 10, 10);

-- barcodes
insert into barcodes (id, code) values(1, '155aoJ7Ha');
insert into barcodes (id, code) values(2, '155mIulCm');
insert into barcodes (id, code) values(3, '155c7RMNd');
insert into barcodes (id, code) values(4, '1550O43DX');
insert into barcodes (id, code) values(5, '155ZRABme');
insert into barcodes (id, code) values(6, '1552Drn22');
insert into barcodes (id, code) values(7, '155TRI2tx');
insert into barcodes (id, code) values(8, '155YGUVvV');
insert into barcodes (id, code) values(9, '155A5Rqhh');
insert into barcodes (id, code) values(10, '155cVPA5W');
insert into barcodes (id, code) values(11, 'nl42YoePv');
insert into barcodes (id, code) values(12, 'ZCXXSRlMx');
insert into barcodes (id, code) values(13, 'vw4TBl2JX');
insert into barcodes (id, code) values(14, '1Y91GOC20');
insert into barcodes (id, code) values(15, 'zk4RqoVBa');
insert into barcodes (id, code) values(16, 'iJ3ziVNPj');
insert into barcodes (id, code) values(17, '7ws1WYahO');
insert into barcodes (id, code) values(18, 'fp9cqXWqz');
insert into barcodes (id, code) values(19, 'Pp7XXzBN0');
insert into barcodes (id, code) values(20, 'RyNX0k6jO');

-- barcodes_goods
insert into barcodes_goods(barcodes_id, goods_id) values (1, 1);
insert into barcodes_goods(barcodes_id, goods_id) values (2, 2);
insert into barcodes_goods(barcodes_id, goods_id) values (3, 3);
insert into barcodes_goods(barcodes_id, goods_id) values (4, 4);
insert into barcodes_goods(barcodes_id, goods_id) values (5, 5);
insert into barcodes_goods(barcodes_id, goods_id) values (6, 6);
insert into barcodes_goods(barcodes_id, goods_id) values (7, 7);
insert into barcodes_goods(barcodes_id, goods_id) values (8, 8);
insert into barcodes_goods(barcodes_id, goods_id) values (9, 9);
insert into barcodes_goods(barcodes_id, goods_id) values (10, 10);

-- barcodes_cells
insert into barcodes_cells(barcodes_id, cells_id) values (1, 1);
insert into barcodes_cells(barcodes_id, cells_id) values (2, 2);
insert into barcodes_cells(barcodes_id, cells_id) values (3, 3);
insert into barcodes_cells(barcodes_id, cells_id) values (4, 4);
insert into barcodes_cells(barcodes_id, cells_id) values (5, 5);
insert into barcodes_cells(barcodes_id, cells_id) values (6, 6);
insert into barcodes_cells(barcodes_id, cells_id) values (7, 7);
insert into barcodes_cells(barcodes_id, cells_id) values (8, 8);
insert into barcodes_cells(barcodes_id, cells_id) values (9, 9);
insert into barcodes_cells(barcodes_id, cells_id) values (10, 10);



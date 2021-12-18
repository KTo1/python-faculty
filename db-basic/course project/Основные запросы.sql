-- запрос «настройка» 
insert into options(name, description, itn, iec, scanprefix_cells, scanprefix_weight, statuses_ready_id, statuses_placed_id, statuses_completed_id) 
values ('северный центр позитроники', 'вместе к светлому будущему!', '7017071707', '4564654', '155', '250', 2, 1, 4); 

-- запрос «добавление заказа»
start transaction;
insert into orders(id, partners_id) 
values (1, 1);

insert into orders_goods(orders_id, statuses_id, goods_id, quantity) 
values (last_inserted_id(), 1, 1, 1);

insert into orders_goods(orders_id, statuses_id, goods_id, quantity) 
values (last_inserted_id(), 1, 2, 1);
commit;

-- запрос «сборка товарной позиции»
-- если запись добавляется:
insert into orders_goods_collected (orders_goods_id, cells_id, exp_date, quantity) 
values (1, 1, ‘2022-31-12’, 1);
-- если запись существует:
update orders_goods_collected 
   set quantity = quantity + 1 
 where id = 1 and cells_id = 1;

-- запрос «заказы за период поступившие»
set @data_start = '2021-12-01';
set @data_end = '2021-12-05';

select 
    orders.id,
    partners.name as partner,
    goods.name as product,
    orders.description,
    sum(orders_goods.quantity) as total
from
    orders_goods as orders_goods
    left join orders as orders 
	  on orders.id = orders_goods.orders_id
    left join goods as goods 
	  on goods.id = orders_goods.goods_id
    inner join (select statuses_placed_id from options where id = get_options()) as op 
	  on op.statuses_placed_id = orders_goods.statuses_id 
    left join partners as partners 
	  on partners.id = orders.partners_id
where orders.date between @data_start and @data_end
group by orders.id, partners.name, goods.name, orders.description with rollup
order by orders.id, partners.name, product;

-- запрос «заказы, за период выполненные с разбивкой по комплектовщикам»
set @data_start = '2021-12-01';
set @data_end = '2021-12-05';

select 
    orders.id,
    partners.name as partner,
    users.name as picker,
    goods.name as product,
    orders.description,
    sum(orders_goods.quantity) as total
from
    orders_goods as orders_goods
    left join orders as orders 
	  on orders.id = orders_goods.orders_id
    left join goods as goods 
	  on goods.id = orders_goods.goods_id
    inner join (select statuses_completed_id from options where id = get_options()) as op 
	  on op.statuses_completed_id = orders_goods.statuses_id
    left join partners as partners 
	  on partners.id = orders.partners_id
    left join users as users 
	  on users.id = orders_goods.users_id 
where orders.date between @data_start and @data_end
group by orders.id, partners.name,  users.name, goods.name, orders.description with rollup
order by orders.id, partners.name,  users.name, product;
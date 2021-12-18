-- система управления складом

drop database if exists store;
create database store;
use store;

drop table if exists options;
create table options(
	id serial primary key, 
    name varchar(150),
	description varchar(150),
	itn  varchar(15),
	iec  varchar(15),
	scanprefix_cells varchar(4),
	scanprefix_weight varchar(4),
    statuses_ready_id tinyint unsigned,
    statuses_placed_id tinyint unsigned,
    statuses_completed_id tinyint unsigned
) comment 'наша организация, общие настройки';

drop table if exists errors;
create table errors(
	id varchar(5) primary key, 
	description varchar(200)
) comment 'коды и иописания ошибок';

drop table if exists users;
create table users(
	id serial primary key, 
	name varchar(150),
    works_storehouses_id bigint unsigned, 
	description varchar(150)    
) comment 'пользователи';	  

drop table if exists storehouses;
create table storehouses(
	id serial primary key, 
    name varchar(150),
	description varchar(150),
	address varchar(200),
	phone varchar(150),
	storekeeper_id bigint unsigned, 
	
	foreign key (storekeeper_id) references users(id) on delete set null on update cascade,    
	index storehouses_name_idx(name)
) comment 'склады';

drop table if exists goods;
create table goods(
	id serial primary key, 
	name varchar(150),
	description varchar(150),
	
	index goods_name_idx(name)
) comment 'товары';

drop table if exists partners;
create table partners(
	id serial primary key, 
	name varchar(150),
	description varchar(150),
	address varchar(200),
	phone varchar(150),
	
	index partners_name_idx(name)
) comment 'партнеры';	  

drop table if exists cells;
create table cells(
	id serial primary key, 
	name varchar(10),
	description varchar(50),
	
	index cells_name_idx(name)
) comment 'ячейки';	  

drop table if exists storehouses_cells;
create table storehouses_cells(
	id serial primary key, 
    storehouses_id bigint unsigned not null,
	cells_id bigint unsigned not null,
	
    foreign key (storehouses_id) references storehouses(id) on delete cascade on update cascade,
	foreign key (cells_id) references cells(id) on delete cascade on update cascade	
) comment 'ячейки на складах';	  

drop table if exists orders_statuses;
create table orders_statuses(
	id tinyint unsigned primary key, 
	name varchar(50)
) comment 'статусы';	  

drop table if exists orders;
create table orders(
	id serial primary key, 
	date datetime default current_timestamp,
	partners_id bigint unsigned default 0,
	description varchar(150),
	
	foreign key (partners_id) references partners(id) on delete set null on update cascade,
    index orders_date_idx(date)
) comment 'заказы';	  

drop table if exists orders_goods;
create table orders_goods(
	id serial primary key, 
	orders_id bigint unsigned not null,
	statuses_id tinyint unsigned default 0,
	storehouses_id bigint unsigned,
	users_id bigint unsigned,
	goods_id bigint unsigned,
	quantity smallint,
	
	foreign key (orders_id) references orders(id) on delete cascade on update cascade,	
	foreign key (statuses_id) references orders_statuses(id) on delete set null on update cascade,
	foreign key (storehouses_id) references storehouses(id) on delete set null on update cascade,
	foreign key (users_id) references users(id) on delete set null on update cascade,	
	foreign key (goods_id) references goods(id) on delete set null on update cascade
) comment 'заказы строки';	 

drop table if exists orders_goods_collected;
create table orders_goods_collected(
	id serial primary key,
	orders_goods_id bigint unsigned, 
	cells_id bigint unsigned,
	exp_date datetime not null,
	quantity smallint,
	is_active boolean default true,
    
	foreign key (orders_goods_id) references orders_goods(id) on delete cascade on update cascade,	
	foreign key (cells_id) references cells(id) on delete set null on update cascade
) comment 'заказы строки собранные';	 

drop table if exists remains_flow;
create table remains_flow(
	id serial primary key, 
	storehouses_id bigint unsigned,
	exp_date datetime not null default current_timestamp,
	date datetime not null default current_timestamp,
	cells_id bigint unsigned,	
	goods_id bigint unsigned,
	quantity smallint,
	
	foreign key (cells_id) references cells(id) on delete set null on update cascade,
	foreign key (storehouses_id) references storehouses(id) on delete set null on update cascade,
	foreign key (goods_id) references goods(id) on delete set null on update cascade
) comment 'движения остатки товаров на складах';	 

drop table if exists barcodes;
create table barcodes(
	id serial primary key, 
	code varchar(128),
	
	index barcodes_code_idx(code)
) comment 'штрих коды';	 

drop table if exists barcodes_goods;
create table barcodes_goods(
	id serial primary key, 
	barcodes_id bigint unsigned not null,
	goods_id bigint unsigned not null,

	foreign key (barcodes_id) references barcodes(id) on delete cascade on update cascade,
	foreign key (goods_id) references goods(id) on delete cascade on update cascade
) comment 'штрих коды товаров';	

drop table if exists barcodes_cells;
create table barcodes_cells(
	id serial primary key, 
	barcodes_id bigint unsigned not null,
	cells_id bigint unsigned not null,

	foreign key (barcodes_id) references barcodes(id) on delete cascade on update cascade,
	foreign key (cells_id) references cells(id) on delete cascade on update cascade
) comment 'штрих коды ячеек';	

-- триггер запрещает запись в регистр остатков строк с пустыми ячейками и сроками годности
drop trigger if exists before_insert_remains_flow;
delimiter //
create trigger before_insert_remains_flow before insert on remains_flow
for each row begin
	if new.exp_date < now() then
		signal sqlstate '45003' set message_text = 'exp date must be greater then now';
    end if;
	if new.cells_id is null or new.cells_id = 0 then
		signal sqlstate '45004' set message_text = 'cell must be fill';
    end if;
end//
delimiter ;

-- создает или обновляет и выбирает пользователя
drop procedure if exists select_user;
delimiter //
create procedure select_user(users_id bigint, users_name varchar(150), works_storehouses_id bigint, out result varchar(200))
deterministic
begin
	declare code varchar(5) default '00000';
	declare error_string varchar(200);
    declare users_exist int;
    declare storehouses_exist int;	
    
	declare continue handler for sqlexception
    begin
		get stacked diagnostics condition 1 code = returned_sqlstate, error_string = message_text;
    end;
    
	select id into storehouses_exist 
	  from storehouses 
	 where id = works_storehouses_id;
	
	select id into users_exist
	  from users 
	 where id = users_id;    
    
    if users_exist is null then
		insert into users(id, name, works_storehouses_id) 
		values (users_id, users_name, works_storehouses_id);
    else
		update users as u 
		   set u.name = users_name, u.works_storehouses_id = works_storehouses_id 
		 where u.id = users_id; 
    end if;
    
    set @current_user_id = users_id;
    
	if code = '00000' then 
		set result = 'ok';
    else 
		set result = concat('error occured (', code, ',', error_string, ')');
    end if;
    
end//
delimiter ;

-- добавляет движение в таблицу остатков, отрицательное - расход, положительное приход на склад.
drop procedure if exists modify_remains;
delimiter //
create procedure modify_remains(storehouses_id bigint, cells_id bigint, goods_id bigint, exp_date varchar(19), quantity smallint, out result varchar(200))
deterministic
begin
   
	declare code varchar(5) default '00000';
	declare error_string varchar(200);    
    declare storehouses_exist int;
    declare cells_exist int;
    declare goods_exist int;

	declare continue handler for sqlexception
    begin
		get stacked diagnostics condition 1 code = returned_sqlstate, error_string = message_text;
    end;

	select id into storehouses_exist 
	  from storehouses 
	 where id = storehouses_id;
	 
    select id into cells_exist 
	  from cells 
	 where id = cells_id;
	 
	select id into goods_exist 
	  from goods 
	 where id = goods_id;
    
    if storehouses_exist is null then
        set code = '45005';
        select description into error_string from errors where id = code;        
    elseif cells_exist is null then    
        set code = '45006';
        select description into error_string from errors where id = code;        
    elseif goods_exist is null then    
        set code = '45007';   
		select description into error_string from errors where id = code;        
    else
		insert into remains_flow(storehouses_id, cells_id, goods_id, exp_date, quantity) 
		values (storehouses_id, cells_id, goods_id, exp_date, quantity);
    end if;
    
	if code = '00000' then 
		set result = 'ok';
    else 
		set result = concat('error occured (', code, ',', error_string, ')');
    end if;
	
end//    
delimiter ;

-- устанавливает статус всем товарным позициям заказа
drop procedure if exists change_order_status;
delimiter //
create procedure change_order_status(orders_id bigint, statuses_id tinyint, out result varchar(200)) 
deterministic
begin

	declare code varchar(5) default '00000';
	declare error_string varchar(200);
    declare statuses_exist int;
    declare orders_exist int;
    
	declare continue handler for sqlexception
    begin
		get stacked diagnostics condition 1 code = returned_sqlstate, error_string = message_text;
    end;
    
	select id into statuses_exist 
	  from orders_statuses 
	 where id = statuses_id;
	 
    select id into orders_exist 
	  from orders 
	 where id = orders_id;
    
    if statuses_exist is null then
        set code = '45001';
        select description into error_string 
		  from errors 
		 where id = code;
    elseif orders_exist is null then    
        set code = '45002';
        select description into error_string 
		  from errors 
		 where id = code;
    else
		update orders_goods as o 
		   set o.statuses_id = statuses_id 
		 where o.orders_id = orders_id;
    end if;

	if code = '00000' then 
		set result = 'ok';
    else 
		set result = concat('error occured (', code, ',', error_string, ')');
    end if;
    
end//
delimiter ;

-- назначает коплектовщика на заказа
drop procedure if exists set_order_picker;
delimiter //
create procedure set_order_picker(orders_id bigint, users_id bigint, out result varchar(200))
deterministic
begin
	declare code varchar(5) default '00000';
	declare error_string varchar(200);
    declare orders_exist int;
    declare users_exist int;	
    declare user_busy int;
    declare works_storehouses_id int;
    
	declare continue handler for sqlexception
    begin
		get stacked diagnostics condition 1 code = returned_sqlstate, error_string = message_text;
    end;
    
    select users.works_storehouses_id into works_storehouses_id 
	  from users 
	 where users.id = users_id;
        
	select og.id into user_busy	
	  from orders_goods as og
	 where og.statuses_id = 3 and og.users_id = users_id;    
    
	select id into orders_exist 
	  from orders 
	 where id = orders_id;
	 
    select id into users_exist 
	  from users 
	 where id = users_id;    
    
    if users_exist is null then
        set code = '45008';
        select description into error_string 
		  from errors 
		 where id = code;
    elseif orders_exist is null then    
	    set code = '45002';
		select description into error_string 
		  from errors 
		 where id = code;        
    elseif user_busy is not null then
		set code = '45009';    
		select description into error_string 
		  from errors 
		 where id = code;        
	elseif works_storehouses_id is null then
        set code = '45010';    
		select description into error_string 
		  from errors 
		 where id = code;        
    else
		start transaction;
		update orders_goods as o 
		   set o.users_id = users_id 
		 where o.orders_id = orders_id and o.storehouses_id = works_storehouses_id;
		 
        update orders_goods as o 
		   set o.statuses_id = 3 
		 where o.orders_id = orders_id and o.storehouses_id = works_storehouses_id;
    end if;
        
	if code = '00000' then 
		set result = 'ok';
        commit;
    else 
		set result = concat('error occured (', code, ',', error_string, ')');
        rollback;
    end if;
    
end//
delimiter ;

-- завершает сборку части заказа, по выбранному комлектовщику, если заказ собран полностью, то 
-- деактивирует собранные товары по заказу и списывает остатки со склада.
drop procedure if exists pickup_completed;
delimiter //
create procedure pickup_completed(orders_id bigint, users_id bigint, out result varchar(200))
deterministic
begin
   
	declare code varchar(5) default '00000';
	declare error_string varchar(200);    
    declare orders_exist int;
    declare users_exist int;
	declare statuses_completed_id int;
    declare order_completed int;
    
    declare orders_goods_id bigint;
    declare storehouses_id bigint;
    declare goods_id bigint;
    declare cells_id bigint;
    declare exp_date datetime;
    declare quantity int;
    declare done int default 0;

    declare orders_goods_cursor cursor for 
			select og.id, og.storehouses_id, o.cells_id, o.exp_date, og.goods_id, o.quantity 
			  from orders_goods_collected as o
				inner join orders_goods as og 
					    on og.id = o.orders_goods_id and og.orders_id = orders_id
             where o.is_active = true;
    
    declare continue handler for sqlstate '02000' set done = 1;
	declare continue handler for sqlexception
    begin
		get stacked diagnostics condition 1 code = returned_sqlstate, error_string = message_text;
    end;
            
	select op.statuses_completed_id into statuses_completed_id 
	  from options as op 
	 where id = get_options();
	 
    select id into orders_exist 
	  from cells 
	 where id = orders_id;
	 
	select id into users_exist 
	  from goods 
	 where id = users_id;
    
    if orders_exist is null then
        set code = '45002';
        select description into error_string 
		  from errors 
		 where id = code;        
    elseif users_exist is null then    
        set code = '45008';  
        select description into error_string 
		  from errors 
		 where id = code;        
    else		
		update orders_goods as og 
		   set og.statuses_id = statuses_completed_id 
		 where og.users_id = users_id and og.orders_id = orders_id;
    end if;
    
    select 
		case when count(id) = og_completed.count_id_completed then 
				true 
			else 
				false 
			end into order_completed 
	  from orders_goods as og 
			left join (select count(id) as count_id_completed 
						 from orders_goods as og 
						where og.orders_id = orders_id and statuses_id = statuses_completed_id) as og_completed
				   on true  
	 where og.orders_id = orders_id;
    
    if order_completed = 1 then
		start transaction;
		open orders_goods_cursor;
        while done = 0 do
			fetch orders_goods_cursor into orders_goods_id, storehouses_id, cells_id, exp_date, goods_id, quantity;
			if done = 0 then 
				call modify_remains(storehouses_id, cells_id, goods_id, exp_date, (-1) * quantity, result);
                update orders_goods_collected 
				   set is_active = false 
				 where orders_goods_collected.orders_goods_id = orders_goods_id;
			end if;
        end while;  
        close orders_goods_cursor;
        
    end if;
    
	if code = '00000' then 
		set result = 'ok';
        commit;
    else 
		set result = concat('error occured (', code, ',', error_string, ')');
        rollback;
    end if;
	
end//    
delimiter ;

-- печатает сброчную ведомость
drop procedure if exists assembly_statement;
delimiter //
create procedure assembly_statement(out result varchar(200))
deterministic
begin

	declare code varchar(5) default '00000';
	declare error_string varchar(200);    
 
	declare oid bigint;
	declare cell varchar(10);
	declare gid bigint;
    declare gid_prev bigint default 0;
	declare product varchar(150);
	declare exp_date datetime;
	declare rem_q tinyint;
    declare ord_q tinyint;
    declare tmp_q tinyint default 0;
	declare done int default 0;   
        
    declare orders_goods_cursor cursor for 
			select o.oid, remains.cell, remains.gid, remains.product, remains.exp_date, remains.quantity as rem_q, o.quantity as ord_q
			from remains_on_works_storehouses as remains
					inner join
							(select o.orders_id as oid, o.quantity, g.id as gid
							   from orders_goods as o
							left join goods as g on g.id = o.goods_id
							inner join users as users 
									on users.works_storehouses_id = o.storehouses_id
								   and users.id = get_current_user_id()
							     where o.statuses_id = 3) as o 
							on o.gid = remains.gid
		order by remains.product , remains.exp_date;  
             
	declare continue handler for sqlstate '02000' set done = 1;
	declare continue handler for sqlexception
    begin
		get stacked diagnostics condition 1 code = returned_sqlstate, error_string = message_text;
    end;
        

	drop table if exists tmp_table;
	create temporary table tmp_table (
		toid bigint,
		tcell varchar(10),
		tproduct varchar(150),
		texp_date datetime,
		quantity_remains tinyint,
		quantity_collect tinyint
	);    
    
	open orders_goods_cursor;
	while done = 0 do
		fetch orders_goods_cursor into oid, cell, gid, product, exp_date, rem_q, ord_q;
		 if done = 0 then
			if gid != gid_prev then
				set tmp_q = ord_q;
            end if;    
			set tmp_q = tmp_q - rem_q;
            if tmp_q >= 0 then
				insert into tmp_table(toid, tcell, tproduct, texp_date, quantity_remains, quantity_collect) values (oid, cell, product, exp_date, rem_q, rem_q);
            else
				insert into tmp_table(toid, tcell, tproduct, texp_date, quantity_remains, quantity_collect) values (oid, cell, product, exp_date, rem_q, rem_q + tmp_q);
            end if;
            set gid_prev = gid;
		end if;
	end while;  
	close orders_goods_cursor;	
	
	select toid as order_id, tcell as cell, tproduct as product, texp_date as exp_date, sum(quantity_remains) as quantity_remains, sum(quantity_collect) as quantity_collect
     from tmp_table 
	where quantity_collect > 0 
	group by toid, tcell, tproduct, texp_date
	order by toid, tcell, tproduct, texp_date;
    
	if code = '00000' then 
		set result = 'ok';
    else 
		set result = concat('error occured (', code, ',', error_string, ')');
    end if;
       
end//    
delimiter ;

-- устанавливает переменную - идентификатор текущего пользователя
drop procedure if exists set_current_user_id;
delimiter //
create procedure set_current_user_id(user_id bigint)
deterministic
begin
	set @current_user_id = user_id;
end//    
delimiter ;

-- возвращает переменную - идентификатор текущего пользователя
drop function if exists get_current_user_id;
delimiter //
create function get_current_user_id()
returns bigint deterministic
begin
	return @current_user_id;
end//
delimiter ;    

-- устанавливает переменную - идентификатор текущих настроек
drop procedure if exists select_options;
delimiter //
create procedure select_options(options_id bigint, out result varchar(200))
deterministic
begin

	declare code varchar(5) default '00000';
	declare error_string varchar(200);    
    declare options_exist int;
    
	declare continue handler for sqlexception
    begin
		get stacked diagnostics condition 1 code = returned_sqlstate, error_string = message_text;
    end;
        
   	select id into options_exist 
	  from options 
	 where id = options_id;
    
	if options_exist is null then    
        set code = '45011';  
        select description into error_string 
		  from errors 
		 where id = code;        
    end if;
    
	if code = '00000' then 
		set result = 'ok';
    else 
		set result = concat('error occured (', code, ',', error_string, ')');
    end if;
    
	set @current_options_id = options_id;
    
end//    
delimiter ;

-- возвращает переменную - идентификатор текущих настроек
drop function if exists get_options;
delimiter //
create function get_options()
returns bigint deterministic
begin
	return @current_options_id;
end//
delimiter ;    

-- отображает заказы в статусе "размещен"
drop view if exists orders_placed;
create view orders_placed as
    select 
        orders.id as oid,
        partners.id as pid,
        partners.name as partner,
        goods.id as gid,
        goods.name as product,
        orders_goods.quantity,
        orders.description
    from
        orders_goods as orders_goods
         left join orders as orders 
			    on orders.id = orders_goods.orders_id
         left join goods as goods 
			    on goods.id = orders_goods.goods_id
        inner join (select statuses_placed_id 
					  from options 
					 where id = get_options()) as op 
				on op.statuses_placed_id = orders_goods.statuses_id
         left join partners as partners 
		        on partners.id = orders.partners_id
         left join orders_statuses as orders_statuses 
			    on orders_statuses.id = orders_goods.statuses_id
    order by orders.id, partner , product;

-- отображает заказы в статусе "готов к сборке"
drop view if exists orders_ready;
create view orders_ready as select 
    orders.id as oid,
	partners.id as pid,
    partners.name as partner,
    storehouses.id as sid,
    storehouses.name as store,
	goods.id as gid,
    goods.name as product,
    orders_goods.quantity,
    orders.description
from
    orders_goods as orders_goods
     left join orders as orders 
	        on orders.id = orders_goods.orders_id
     left join goods as goods 
			on goods.id = orders_goods.goods_id
    inner join (select statuses_ready_id 
				  from options 
				 where id = get_options()) as op 
		    on op.statuses_ready_id = orders_goods.statuses_id
     left join partners as partners 
			on partners.id = orders.partners_id
     left join orders_statuses as orders_statuses 
			on orders_statuses.id = orders_goods.statuses_id
     left join storehouses as storehouses
		    on orders_goods.storehouses_id = storehouses.id
order by orders.id, partner, product;

-- показывает остатки товаров по всем складам
drop view if exists remains;
create view remains as 
			select 
				 store.id as sid,
				 store.name as storehouse,
                 goods.id as gid,
				 goods.name as product,
                 cells.id as cid,
				 cells.name as cell,
				 remains_flow.exp_date,
				 sum(remains_flow.quantity) as quantity
			 from remains_flow as remains_flow
				left join cells as cells 
					   on cells.id = remains_flow.cells_id
				left join goods as goods 
					   on goods.id = remains_flow.goods_id
				left join storehouses as store 
					   on store.id = remains_flow.storehouses_id
		 group by product, cell, exp_date;
    
-- показывает остатки товаров по текущему складу пользователя
drop view if exists remains_on_works_storehouses;
create view remains_on_works_storehouses as 
			select 
				  goods.id as gid,
				  goods.name as product,
                  cells.id as cid,
				  cells.name as cell,
				  remains_flow.exp_date,
				  sum(remains_flow.quantity) as quantity
			from remains_flow as remains_flow
				inner join users as users 
						on users.works_storehouses_id = remains_flow.storehouses_id
					   and users.id = get_current_user_id()
				 left join cells as cells 
					    on cells.id = remains_flow.cells_id
				 left join goods as goods 
					    on goods.id = remains_flow.goods_id
			group by product, cell, exp_date;
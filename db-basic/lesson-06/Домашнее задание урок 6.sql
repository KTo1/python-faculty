-- Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех общался с выбранным пользователем (написал ему сообщений).
use vk;
set @user_id = 1;
select (select firstname from users where id = from_user_id ), from_user_id, count(*) from messages as m 
where
	to_user_id = @user_id
group by 
	1, 2
order by 
	3 desc
limit 
	1
	
use vk;
set @user_id = 1;
select u.firstname, from_user_id, count(*) from messages as m 
left join users as u 
	on m.from_user_id = u.id 
where 
	m.to_user_id = @user_id 
group by 
	u.firstname, from_user_id 
order by 
	3 desc 
limit 
	1 


-- Подсчитать общее количество лайков, которые получили пользователи младше 10 лет.
use vk;
select count(*)  from likes as l 
where
	datediff(now(), (select birthday from profiles as p where p.user_id in  
						(select user_id from media as m where m.id = l.media_id)
					)
			) / 365.25 <= 10;

use vk;
select count(*)  from likes as l 
left join media as m 
	on m.id = l.media_id
left join profiles as p 
	on m.user_id = p.user_id
where
	datediff(now(), birthday) / 365.25 <= 10
	
	
-- Определить кто больше поставил лайков (всего): мужчины или женщины.
use vk;
select (select gender from profiles as p where p.user_id = l.user_id), count(*) from likes as l 
group 
	by 1
order by
	2 desc
limit 
	1   	
	
use vk;
select gender, count(*) from likes as l 
left join 
	profiles as p on l.user_id = p.user_id 
group 
	by gender
order by
	2 desc
limit 
	1   	
/*** Leet Code Scratch pad ***/
--Exchange Seats
create table dbo.seat (
id int identity(1,1),
student varchar(30)
)
Go

insert into dbo.seat (student)
values ('Abbot')
, ('Doris')
, ('Emerson')
, ('Green')
, ('Jeames')
Go

-- -- Solution 1
declare @max_id int
set @max_id = (select max(id) from seat)
select case 
        when id > 1 and id % 2 = 0 
                then id-1 
        else 
              case when id = @max_id 
                then id 
              else 
                id+1 
              end 
        end as id, student
from seat
Go

-- -- Solution 2
select id, coalesce(
				case when id % 2 = 1 then lead(student,1) over (order by id) else null end
				, case when id % 2 = 0 then lag(student,1) over (order by id) else null end
				, student
			)
from seat
Go

--Duplicate Email addresses
create table dbo.person (
id int identity(1,1)
, Email varchar(255))
Go

insert into dbo.person (Email)
values ('a@b.com'),('c@d.com'),('a@b.com')

-- -- Solution 1
select Email
from Person
group by Email
    having count(1) > 1

-- -- Solution 2
SELECT DISTINCT t1.Email
FROM Person t1
JOIN Person t2
ON t1.email = t2.email and t1.id <> t2.id
Go

-- Customers Who Never Order
create table dbo.Customers (
Id int identity(1,1),
Name varchar(255))

insert into dbo.Customers (Name)
values ('Joe'), ('Henry'), ('Sam'), ('Max')

create table dbo.Orders (
Id int identity(1,1),
CustomerId int)

insert into dbo.Orders (CustomerId)
values (3), (1)
Go

select c.Name as Customers
from Customers c
left join Orders o
    on c.Id = o.CustomerId
where o.Id is null
Go

SELECT Name as Customers
FROM Customers (NOLOCK)
WHERE Id NOT IN (SELECT DISTINCT CustomerId 
				 FROM Orders (NOLOCK))
Go

--Human Traffic of Stadium
create table dbo.stadium (
id int identity(1,1)
, visit_date date
, people int)
Go
--truncate table dbo.stadium
insert into dbo.stadium (visit_date, people)
--select visit_date, people from dbo.stadium_raw
values ('2017-01-01', 10),
('2017-01-02', 109),
('2017-01-03', 150),
('2017-01-04', 100)
--('2017-01-05', 145),
--('2017-01-06', 1455),
--('2017-01-07', 199),
--('2017-01-08', 188)
Go

-- --Solution 1
select id, visit_date, people
from (
    select id, visit_date, people
    , id-lag(id,2) over (order by id) as distance_to_prev_prev_visit
    , id-lag(id,1) over (order by id) as distance_to_prev_visit     
    , id-lead(id,1) over (order by id) as distance_to_next_visit
    , id-lead(id,2) over (order by id) as distance_to_next_next_visit 
    from stadium
    where people >= 100
    ) as sub_query
where (distance_to_prev_prev_visit = 2 and distance_to_prev_visit = 1)
 or (distance_to_prev_visit = 1 and distance_to_next_visit = -1)
 or (distance_to_next_visit = -1 and distance_to_next_next_visit = -2)
 Go

-- --Solution 2
select distinct t1.id, t1.visit_date, t1.people
from stadium t1, stadium t2, stadium t3
where
(abs(t1.id - t2.id) <= 2 and abs(t2.id - t3.id) <= 2 and abs(t1.id - t3.id) <=2)
and
(t1.people >= 100 and t2.people >= 100 and t3.people >= 100)
and (t1.id <> t2.id and t2.id<> t3.id and t1.id <> t3.id)
order by t1.id
Go

--Rank Scores
create table dbo.Scores (
Id int identity(1,1)
, Score decimal(3,2))

insert into dbo.Scores (Score)
values (3.50), (3.65), (4.00), (3.85), (4.00), (3.65)

-- -- Solution 1
select Score, dense_rank() over (order by Score desc) as Rank
from Scores
order by Score desc

-- -- Solution 2
;with cte as
(
select Score, row_number() over (order by Score desc) as rownum
from (select distinct Score from Scores) s
)
select cte.Score, cte.rownum as Rank
from Scores
join cte
    on Scores.Score = cte.Score
order by 1 desc

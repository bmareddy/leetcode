-- Rising Temperature
create table dbo.Weather (
Id int identity(1,1),
RecordDate date,
Temperature int
)

insert into dbo.Weather (RecordDate, Temperature)
values ('2015-01-01', 10),
('2015-01-02', 25),
('2015-01-03', 20),
('2015-01-04', 30)

-- --Solution 1
select id
from (
    select id, Temperature
    , lag(Temperature, 1) over (order by RecordDate asc) as Temperature_previous_date
    from Weather
) temp_table
where Temperature > Temperature_previous_date
Go

select today.id
from Weather today
join Weather yesterday
	on yesterday.RecordDate = dateadd(D,-1,today.RecordDate)
where today.Temperature > yesterday.Temperature
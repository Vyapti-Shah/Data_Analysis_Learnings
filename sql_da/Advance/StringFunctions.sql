-- String Functions (TRIM, LTRIM, RTRIM, Replace, Substring, Upper, Lower, Charindex, Concat)
drop table if exists EmployeeErrors

create table EmployeeErrors(
EmployeeID varchar(50),
FirstName varchar(50),
LastName varchar(50))

insert into EmployeeErrors values
('1001','Vyaptio','Shah'),
('  1002','Sejal','Shah'),
('1003','SAnjay','Shah - Fired')

select * from EmployeeErrors

-- TRIM, LTRIM, RTRIM
select EmployeeID, trim(EmployeeID) as IDTRIM --gets rid of blanck spaces on all sides
from EmployeeErrors
select EmployeeID, ltrim(EmployeeID) as IDLTRIM --gets rid of blanck spaces from left side
from EmployeeErrors
select EmployeeID, rtrim(EmployeeID) as IDRTRIM --gets rid of blanck spaces from right side
from EmployeeErrors

-- Replace
select LastName, replace(LastName, ' - Fired','') as LastNameFixed
from EmployeeErrors

-- Substring
select substring(FirstName,1,3) from EmployeeErrors

select err.FirstName, substring(err.FirstName,1,3), dem.FirstName, substring(dem.FirstName,1,3)
from EmployeeErrors err
join [SQL Tutorial]..EmployeeDemographics dem
on substring(err.FirstName,1,3) = substring(dem.FirstName,1,3)

-- Upper and Lower
select FirstName, upper(FirstName) as UpperCase, lower(FirstName) as LowerCase
from EmployeeErrors

-- Locate (works in MySQL)
-- select FirstName, locate('a',FirstName) from EmployeeErrors
-- For SQL Server charindex() is used
select FirstName, charindex('a',FirstName) as PositionOfA from EmployeeErrors

-- Concat
select concat(FirstName,'',LastName) as ErrorFullName from EmployeeErrors
-- Union, Union All
-- join combines data based 2 different tables having on a same column whereas
-- uninon combines data of the all the tables and put it in one table having all the different columns

--create table WareHouseEmployeeDemographics
--(EmployreeID int,
--FirstName varchar(50),
--LastName varchar(50),
--Age int,
--Gender varchar(50))

--insert into WareHouseEmployeeDemographics values
--(1013, 'Naman', 'Shah', 30, 'Male'),
--(1050, 'Sachi', 'Shah', 22, 'Female'),
--(1051, 'Daksh', 'Shah', 20, 'Male'),
--(1052, 'Samaira', 'Shah', 19, 'Female')


select * from [SQL Tutorial].dbo.EmployeeDemographics
select * from [SQL Tutorial].dbo.WareHouseEmployeeDemographics


select * from [SQL Tutorial].dbo.EmployeeDemographics 
full outer join [SQL Tutorial].dbo.WareHouseEmployeeDemographics
on EmployeeDemographics.EmployeeID = WareHouseEmployeeDemographics.EmployeeID

select * from [SQL Tutorial].dbo.EmployeeDemographics
union --it does not show duplicates
select * from [SQL Tutorial].dbo.WareHouseEmployeeDemographics

select * from [SQL Tutorial].dbo.EmployeeDemographics
union all --it also shows duplicates
select * from [SQL Tutorial].dbo.WareHouseEmployeeDemographics

select EmployeeDemographics.EmployeeID, EmployeeDemographics.FirstName, EmployeeDemographics.Age
from [SQL Tutorial].dbo.EmployeeDemographics
union  --this gives an incorrect table as it combines firstname with jobtitle and age with salary
select EmployeeSalary.EmployeeID, EmployeeSalary.JobTitle, EmployeeSalary.Salary
from [SQL Tutorial].dbo.EmployeeSalary
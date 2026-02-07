
--Select Statement -> top, distinct, as, max, min, avg
select * from EmployeeDemographics
select FirstName, LastName from EmployeeDemographics
select top 5 * from EmployeeDemographics
select distinct(EmployeeID) from EmployeeDemographics
select distinct(Gender) from EmployeeDemographics
select count(LastName) from EmployeeDemographics
select count(LastName) as LastNameCount from EmployeeDemographics
select * from EmployeeSalary
select min(Salary) from EmployeeSalary
select avg(Salary) from EmployeeSalary
select * from [SQL Tutorial].dbo.EmployeeSalary

--Where Statement -> =, <>, <, >, and, or, like, null, not null, in
select * from EmployeeDemographics where FirstName = 'Vyapti'
select * from EmployeeDemographics where FirstName <> 'Vyapti' --<> means not equals to
select * from EmployeeDemographics where Age >= 30
select * from EmployeeDemographics where Age <= 30 and Gender = 'Female'
select * from EmployeeDemographics where Age <= 30 or Gender = 'Female'
select * from EmployeeDemographics where LastName like 'S%' -- last name starts with S
select * from EmployeeDemographics where FirstName like 'S%' -- first name starts with S
select * from EmployeeDemographics where FirstName like '%S%'  -- first name has S anywhere in it
select * from EmployeeDemographics where FirstName like 'a%u%' -- first name starts with A and has u anywhere in it
select * from EmployeeDemographics where FirstName is null 
select * from EmployeeDemographics where FirstName is not null 
select * from EmployeeDemographics where FirstName in ('Vyapti','Sejal') -- it is basically a multiple = 
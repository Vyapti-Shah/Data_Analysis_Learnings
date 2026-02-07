-- Aliasing

select FirstName + ' ' + LastName as FullName 
from [SQL Tutorial].dbo.EmployeeDemographics
-- using or not using 'as' does not matter
select LastName + ' ' + FirstName  FullName 
from [SQL Tutorial].dbo.EmployeeDemographics

select avg(Age) as AvgAge
from [SQL Tutorial].dbo.EmployeeDemographics

select Demo.EmployeeID, Sal.EmployeeID
from [SQL Tutorial].dbo.EmployeeDemographics as Demo
join [SQL Tutorial].dbo.EmployeeSalary as Sal
on Demo.EmployeeID = Sal.EmployeeID

select a.EmployeeID, a.FirstName, b.JobTitle, c.Age
from [SQL Tutorial].dbo.EmployeeDemographics as a
left join [SQL Tutorial].dbo.EmployeeSalary as b
on a.EmployeeID = b.EmployeeID
left join [SQL Tutorial].dbo.WareHouseEmployeeDemographics as c
on a.EmployeeID = c.EmployeeID
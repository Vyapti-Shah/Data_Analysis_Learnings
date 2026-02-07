-- Inner Joins, Full/Left/Right Outer Joins
select * from [SQL Tutorial].dbo.EmployeeDemographics
select * from [SQL Tutorial].dbo.EmployeeSalary

select * 
from [SQL Tutorial].dbo.EmployeeDemographics --left
inner join [SQL Tutorial].dbo.EmployeeSalary --right
on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

select * 
from [SQL Tutorial].dbo.EmployeeSalary --left
full outer join [SQL Tutorial].dbo.EmployeeDemographics --right
on EmployeeSalary.EmployeeID = EmployeeDemographics.EmployeeID

select * 
from [SQL Tutorial].dbo.EmployeeSalary --left
left outer join [SQL Tutorial].dbo.EmployeeDemographics --right
on EmployeeSalary.EmployeeID = EmployeeDemographics.EmployeeID --the left table is considered 

select * 
from [SQL Tutorial].dbo.EmployeeSalary --left
right outer join [SQL Tutorial].dbo.EmployeeDemographics --right
on EmployeeSalary.EmployeeID = EmployeeDemographics.EmployeeID --the right table is considered 

select EmployeeSalary.EmployeeID, FirstName, LastName, JobTitle, Salary
from [SQL Tutorial].dbo.EmployeeSalary --left
right outer join [SQL Tutorial].dbo.EmployeeDemographics --right
on EmployeeSalary.EmployeeID = EmployeeDemographics.EmployeeID

select EmployeeDemographics.EmployeeID, FirstName, LastName, JobTitle, Salary
from [SQL Tutorial].dbo.EmployeeDemographics --left
inner join [SQL Tutorial].dbo.EmployeeSalary --right
on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
where FirstName <> 'Vyapti' order by Salary desc


select EmployeeSalary.JobTitle, EmployeeSalary.Salary
from [SQL Tutorial].dbo.EmployeeDemographics inner join [SQL Tutorial].dbo.EmployeeSalary
on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
where JobTitle = 'Salesman' 

select EmployeeSalary.JobTitle, avg(Salary)
from [SQL Tutorial].dbo.EmployeeDemographics inner join [SQL Tutorial].dbo.EmployeeSalary
on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
where JobTitle = 'Salesman' group by JobTitle


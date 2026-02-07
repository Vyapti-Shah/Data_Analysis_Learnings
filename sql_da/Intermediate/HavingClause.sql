-- Having Clause

select JobTitle, count(JobTitle)
from [SQL Tutorial].dbo.EmployeeDemographics
join [SQL Tutorial].dbo.EmployeeSalary
on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
--where count(JobTitle) > 1 this gives error so use having clause
group by JobTitle
having count(JobTitle) > 1 

select JobTitle, avg(Salary)
from [SQL Tutorial].dbo.EmployeeDemographics
join [SQL Tutorial].dbo.EmployeeSalary
on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
--where count(JobTitle) > 1 this gives error so use having clause
group by JobTitle
having avg(Salary) > 50000
order by avg(Salary)

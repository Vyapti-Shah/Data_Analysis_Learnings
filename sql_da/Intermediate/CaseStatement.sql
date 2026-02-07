-- Case Statement
select FirstName,LastName, Age, 
case
	when Age=35 then 'Cool'
	when Age>32 then 'Old'
	when Age between 30 and 32 then 'Young'
	else 'Baby'
end
from [SQL Tutorial].dbo.EmployeeDemographics
where Age is not null
order by Age

select FirstName, LastName, JobTitle, Salary,
case
	when JobTitle = 'Salesman' then  Salary + (Salary * 0.10)
	when JobTitle = 'Accountant' then  Salary + (Salary * 0.05)
	when JobTitle = 'HR' then  Salary + (Salary * 0.01)
	else Salary + (Salary * 0.03)
end as [Salary After Raise]
from [SQL Tutorial].dbo.EmployeeDemographics
join [SQL Tutorial].dbo.EmployeeSalary
on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
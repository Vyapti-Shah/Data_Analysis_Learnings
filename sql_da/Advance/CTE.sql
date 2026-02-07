--CTE (Common Table Expression)
-- The CTE is not stored anywhere so we need to run it all the time while selecting it

with CTE_Employee as(
select FirstName, LastName, Gender, Salary,
count(Gender) over (partition by Gender) as TotalGender,
avg(Salary) over (partition by Gender) as AvgSalary
from [SQL Tutorial]..EmployeeDemographics dem
join [SQL Tutorial]..EmployeeSalary sal
on dem.EmployeeID = sal.EmployeeID
where Salary > '50000'
)
select FirstName, AvgSalary from CTE_Employee

--select * from CTE_Employee -> this won't work as for cte the select statement works only when directly after the CTE brackets
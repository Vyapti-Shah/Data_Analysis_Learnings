--Partition By

select FirstName, LastName, Gender, Salary,
count(Gender) over (partition by Gender) as TotalGender
from [SQL Tutorial]..EmployeeDemographics dem
join [SQL Tutorial]..EmployeeSalary sal
on dem.EmployeeID = sal.EmployeeID

select Gender, count(Gender)
from [SQL Tutorial]..EmployeeDemographics dem
join [SQL Tutorial]..EmployeeSalary sal
on dem.EmployeeID = sal.EmployeeID
group by Gender
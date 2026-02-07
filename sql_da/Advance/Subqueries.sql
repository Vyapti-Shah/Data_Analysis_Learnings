-- Subqueries (in the Select, From and Where Statement)

select * from EmployeeSalary

-- Subquery using select
select EmployeeID, Salary, (select avg(Salary) from EmployeeSalary) as AllAvgSalary
from EmployeeSalary

-- Subquery using partition by
select EmployeeID, Salary, avg(Salary) over () as AllAvgSalary
from EmployeeSalary

-- Subquery using group by (doesn't have any change from orginal)
select EmployeeID, Salary, avg(Salary) as AllAvgSalary
from EmployeeSalary
group by EmployeeID, Salary
order by 1,2

-- Subquery using from
select * from (select EmployeeID, Salary, avg(Salary) over () as AllAvgSalary 
              from EmployeeSalary) a

-- Subquery using where
select EmployeeID, JobTitle, Salary
from EmployeeSalary
where EmployeeID in (select EmployeeID from EmployeeDemographics where Age>30)
--Temp Tables
--The temp table does not get stored in the database but it is stored somewhere

--Table 1
drop table if exists #temp_Employee --this helps to run the create and insert steps again when executed without error
create table #temp_Employee(
EmployeeID int,
JobTitle varchar(100),
Salary int)

insert into #temp_Employee values(
'1001','HR','45000')

insert into #temp_Employee select * from [SQL Tutorial]..EmployeeSalary
select * from #temp_Employee


--Table 2
drop table if exists #temp_Employee1 --this helps to run the create and insert steps again when executed without error
create table #temp_Employee1(
JobTitle varchar(50),
EmployeesPerJob int,
AvgAge int,
AvgSalary int)

insert into #temp_Employee1 
select JobTitle , count(JobTitle), avg(Age), avg(Salary)
from [SQL Tutorial]..EmployeeDemographics dem
join [SQL Tutorial]..EmployeeSalary sal
on dem.EmployeeID = sal.EmployeeID
group by JobTitle

select * from #temp_Employee1
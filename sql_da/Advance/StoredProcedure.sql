-- Stored Procedure

--create procedure TEST as  --go to Programmability>>Stored Procedures
--select * from EmployeeDemographics
exec TEST

--create procedure Temp_Employee as
--create table #temp_Employee1(
--JobTitle varchar(50),
--EmployeesPerJob int,
--AvgAge int,
--AvgSalary int)
--insert into #temp_Employee1 
--select JobTitle , count(JobTitle), avg(Age), avg(Salary)
--from [SQL Tutorial]..EmployeeDemographics dem
--join [SQL Tutorial]..EmployeeSalary sal
--on dem.EmployeeID = sal.EmployeeID
--group by JobTitle
--select * from #temp_Employee1
--exec Temp_Employee

--step : then go to stored procedures and click modify by right clicking dbo.Temp_Employee and make the following changes in the code there
--ALTER procedure [dbo].[Temp_Employee] 
--@JobTitle nvarchar(100) as
--create table #temp_Employee1(
--JobTitle varchar(50),
--EmployeesPerJob int,
--AvgAge int,
--AvgSalary int)
--insert into #temp_Employee1 
--select JobTitle , count(JobTitle), avg(Age), avg(Salary)
--from [SQL Tutorial]..EmployeeDemographics dem
--join [SQL Tutorial]..EmployeeSalary sal
--on dem.EmployeeID = sal.EmployeeID
--where JobTitle = @JobTitle
--group by JobTitle
exec Temp_Employee @JobTitle = 'Salesman'
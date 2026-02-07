-- Updating/Deleting Data

--create table UpdateDeleteEmployeeDemographics
--(EmployeeID int,
--FirstName varchar(50),
--LastName varchar(50),
--Age int,
--Gender varchar(50))

--insert into EmployeeDemographics values
--(1001, 'Vyapti', 'Shah', 28, 'Female'),
--(1002, 'Vaishnavi', 'Shetty', 29, 'Female'),
--(1003, 'Sanjay', 'Shah', 35, 'Male'),
--(1004, 'Sejal', 'Shah', 31, 'Female'),
--(1005, 'Tirth', 'Sanhgavi', 32, 'Male'),
--(1006, 'Aayush', 'Sheth', 35, 'Male'),
--(1007, 'Shalmalee', 'Thakur',29 , 'Female'),
--(1008, 'Jayantilal', 'Shah', 40, 'Male'),
--(1009, 'Jinit', 'Vora', 30, 'Male')

select * from [SQL Tutorial].dbo.UpdateDeleteEmployeeDemographics

--update [SQL Tutorial].dbo.UpdateDeleteEmployeeDemographics
--set EmployeeID = 1010
--where FirstName = 'Shalmalee' and LastName = 'Thakur'
--select * from [SQL Tutorial].dbo.UpdateDeleteEmployeeDemographics

--update [SQL Tutorial].dbo.UpdateDeleteEmployeeDemographics
--set Age = 30, Gender = 'Female'
--where FirstName = 'Shalmalee' and LastName = 'Thakur'
--select * from [SQL Tutorial].dbo.UpdateDeleteEmployeeDemographics

--delete from [SQL Tutorial].dbo.UpdateDeleteEmployeeDemographics
--where EmployeeID = 1005
--select * from [SQL Tutorial].dbo.UpdateDeleteEmployeeDemographics

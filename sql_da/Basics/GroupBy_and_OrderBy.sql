--Group by and Order by

select distinct(Gender) from EmployeeDemographics
select Gender, count(Gender) from EmployeeDemographics group by Gender
-- in distinct it just shows what value is in there which is unique whereas 
-- in group by its showing the unique value and also rolling them all up into one column that we can use for other things

select Gender, Age, count(Gender) from EmployeeDemographics group by Gender, Age

select Gender, Age, count(Gender) from EmployeeDemographics where Age>30 group by Gender, Age

select Gender, Age, count(Gender) as CountGender from EmployeeDemographics 
where Age>30 group by Gender, Age order by CountGender

select * from EmployeeDemographics order by Age desc, Gender desc

select * from EmployeeDemographics order by 4 asc, 5 desc --it changes the 4th column as ascending and 5th column to descending

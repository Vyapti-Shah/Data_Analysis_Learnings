--Regular Expression (regex)

drop table if exists Employees

create table Employees(
ID int primary key,
Name nvarchar(50),
Email nvarchar(50),
Phone nvarchar(20))

insert into Employees values
(1,'Vyapti','vyapti123@gmail.com','12345b'),
(2,'Sejal','8sejal@gmail.com','56789'),
(3,'Sanjay','sanjay45@gmail.com','90123a'),
(4,'Vaishnavi','vaishnavi09@gmail.com','34567')

select * from Employees

--using like
select * from Employees where Name like 'v%i' --name starts with v and ends with i

--using patindex (finds where digit appears in email)
select Name, Email, patindex('%[0-9]%',Email) as DigitPosition from Employees

--using charindex
select Name, charindex('gmail',Email) as GmailPosition from Employees

--using like with []
select * from Employees where Phone like '%[a-zA-Z]%' --employees whose phone numbers contains letters

--using like with [^0-9]
select * from Employees where Phone not like '%[^0-9]%' ----employees whose phone numbers are only digits

--varchar -> variable character (1 byte per character) and text with english letters only
--nvarchar -> national variable character (2 byte per character) and text with multiple languages or special symbols
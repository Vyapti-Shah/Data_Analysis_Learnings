--Sys Tables -> it shows the info about the tables/columns/objects stored in the tables of database
select name, object_id, create_date from sys.tables
select name, column_id, object_id from sys.columns where object_id = OBJECT_ID('Students')
-- 02_views.sql
CREATE VIEW vwEmployees AS SELECT Id,Name,Dept FROM Employee;
GO
ALTER VIEW vwEmployees AS SELECT * FROM Employee;
GO
DROP VIEW vwEmployees;
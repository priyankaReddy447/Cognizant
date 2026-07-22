-- 09_stored_procedures.sql
CREATE PROC GetEmployees AS SELECT * FROM Employee;
GO
EXEC GetEmployees;
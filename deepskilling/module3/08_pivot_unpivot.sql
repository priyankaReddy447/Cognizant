-- 08_pivot_unpivot.sql
-- PIVOT example
SELECT * FROM (SELECT Dept,Salary FROM Employee) s PIVOT(SUM(Salary) FOR Dept IN([HR],[IT])) p;
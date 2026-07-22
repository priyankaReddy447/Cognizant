-- 05_grouping_sets_cube_rollup.sql
SELECT Dept,SUM(Salary) Total FROM Employee GROUP BY ROLLUP(Dept);
SELECT Dept,SUM(Salary) Total FROM Employee GROUP BY CUBE(Dept);
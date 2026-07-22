-- 04_window_functions.sql
SELECT Name,Salary,ROW_NUMBER() OVER(ORDER BY Salary DESC) RN,RANK() OVER(ORDER BY Salary DESC) Rnk,DENSE_RANK() OVER(ORDER BY Salary DESC) DRnk FROM Employee;
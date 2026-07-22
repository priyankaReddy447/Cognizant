-- 14_transactions.sql
BEGIN TRAN; UPDATE Employee SET Salary=Salary+1000; COMMIT;
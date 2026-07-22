-- 13_try_catch_exception_handling.sql
BEGIN TRY SELECT 1/0; END TRY BEGIN CATCH SELECT ERROR_MESSAGE() AS ErrorMessage; END CATCH;
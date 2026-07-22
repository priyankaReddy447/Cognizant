-- 10_user_defined_functions.sql
CREATE FUNCTION dbo.GetBonus(@s DECIMAL(10,2)) RETURNS DECIMAL(10,2) AS BEGIN RETURN @s*0.1 END;
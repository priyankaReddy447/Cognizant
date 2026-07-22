-- 07_merge_statement.sql
-- MERGE example skeleton
MERGE Employee AS T USING Employee AS S ON T.Id=S.Id WHEN MATCHED THEN UPDATE SET T.Name=S.Name;
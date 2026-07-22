-- 11_triggers.sql
CREATE TRIGGER trgInsert ON Employee AFTER INSERT AS PRINT 'Inserted';
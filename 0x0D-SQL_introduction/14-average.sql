--This will compute the average score of all records in the table second_table.
INSERT INTO average_scores (average)
SELECT AVG(score)
FROM second_table;

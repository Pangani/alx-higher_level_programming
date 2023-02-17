-- lisst records by name and score if name exists
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY score DESC;

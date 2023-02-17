-- Displays 3 cities with highest average temperature
SELECT `city`, AVG(`value`) AS `average`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `average` DESC
LIMIT 3;

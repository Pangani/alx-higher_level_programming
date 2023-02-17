-- displays the average temperature by city ordered by temperature
SELECT `city`, `temperature` 
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;

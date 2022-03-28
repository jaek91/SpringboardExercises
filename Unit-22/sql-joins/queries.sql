
-- write your queries here
--Joins SQL exercise-- (Jae Kim)


-- first problem
SELECT * FROM owners FULL JOIN vehicles ON owners.id = vehicles.owner_id;

-- second problem
SELECT first_name, last_name, COUNT(owner_id) as count FROM owners 
JOIN vehicles ON owners.id = vehicles.owner_id
GROUP BY first_name, last_name
ORDER BY first_name ASC;

--third problem
 SELECT first_name, last_name, ROUND(AVG(price)) as average_price, COUNT(owner_id) FROM owners 
 JOIN vehicles ON owners.id = vehicles.owner_id  
 GROUP BY first_name, last_name
 HAVING COUNT(owner_id) > 1 AND ROUND(AVG(price)) > 10000
 ORDER BY first_name DESC;
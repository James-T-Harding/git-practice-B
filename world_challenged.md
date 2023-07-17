# World Challenges.

### 1. Using COUNT, get the number of cities in the USA.
```SQL
    SELECT i.name
    FROM country o
	    JOIN city i ON o.Code = i.CountryCode
    where o.name = 'United States'
```



### 2. Find out the population and life expectancy for people in Argentina.
```SQL
SELECT Population, LifeExpectancy 
FROM country
WHERE Name="Argentina"
```

### 3. Using IS NOT NULL, ORDER BY, and LIMIT, which country has the highest life expectancy?
```SQL
SELECT name
FROM country
WHERE LifeExpectancy IS NOT NULL
ORDER BY LifeExpectancy DESC LIMIT 1
```

### 4. Using JOIN ... ON, find the capital city of Spain.
```SQL
SELECT i.Name
FROM country o 
	JOIN city i ON i.id = o.Capital
WHERE o.name = "Spain"
```

### 5. Using JOIN ... ON, list all the languages spoken in the Southeast Asia region.
```SQL
SELECT l.Language
FROM country o
	JOIN countrylanguage l ON l.CountryCode = o.Code
WHERE Region = "Southeast Asia"
```


### 6. Using a single query, list 25 cities around the world that start with the letter F.
```SQL
SELECT name
FROM city 
WHERE name LIKE 'f%'
LIMIT 25
```


### 7. Using COUNT and JOIN ... ON, get the number of cities in China.
```SQL
SELECT COUNT(i.id)
FROM country o
	JOIN city i ON o.Code = i.CountryCode
WHERE o.name = "China"
```

### 8. Using IS NOT NULL, ORDER BY, and LIMIT, which country has the lowest population? Discard non-zero populations.
```SQL
SELECT name
FROM country
WHERE population IS NOT NULL
ORDER BY population ASC LIMIT 1
```


### 9. Using aggregate functions, return the number of countries the database contains.
```SQL
SELECT COUNT(Code)
FROM country
```

### 10. What are the top ten largest countries by area?
```SQL
SELECT name
FROM country
ORDER BY SurfaceArea DESC LIMIT 10
```

### 11. List the five largest cities by population in Japan.
```SQL
SELECT i.name
FROM country o
	JOIN city i ON o.Code = i.CountryCode
WHERE o.name = "Japan"
ORDER BY i.Population DESC LIMIT 5
```

### 12. List the names and country codes of every country with Elizabeth II as its Head of State. You will need to fix the mistake first!
```SQL
UPDATE country
SET HeadOfState = "Elizabeth II"
WHERE HeadOfState = "Elisabeth II";

SELECT name
FROM country
WHERE HeadOfState = "Elizabeth II";
```

### 13. List the top ten countries with the smallest population-to-area ratio. Discard any countries with a ratio of 0.
```SQL
SELECT name
FROM country
WHERE Population != 0
ORDER BY Population/SurfaceArea ASC LIMIT 10
```

### 14. List every unique world language.
```SQL
SELECT distinct Language from countrylanguage
```

### 15. List the names and GNP of the world's top 10 richest countries.
```SQL
SELECT name, GNP
FROM country
ORDER BY GNP DESC LIMIT 10
```

### 16. List the names of, and number of languages spoken by, the top ten most multilingual countries.
```SQL
SELECT o.name, COUNT(language) as Language_Count
FROM country o
	JOIN countrylanguage l ON l.CountryCode = o.Code
GROUP BY o.name
ORDER BY Language_Count DESC LIMIT 10
```

### 17. List every country where over 50% of its population can speak German.
```SQL
SELECT o.name
FROM country o
	JOIN countrylanguage l ON l.CountryCode = o.Code
WHERE Language = "German" and Percentage > 50
```

### 18. Which country has the worst life expectancy? Discard zero or null values.
```SQL
SELECT name
FROM country
WHERE LifeExpectancy IS NOT NULL 
AND LifeExpectancy != 0
ORDER BY LifeExpectancy DESC LIMIT 1
```

### 19. List the top three most common government forms.
```SQL
SELECT GovernmentForm
from country
GROUP BY GovernmentForm
ORDER BY COUNT(Code) DESC LIMIT 3
```

### 20. How many countries have gained independence since records began?
```SQL
SELECT COUNT(Code) 
FROM country
WHERE IndepYear IS NOT NULL
```
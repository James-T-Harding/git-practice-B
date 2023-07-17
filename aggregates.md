## Group by
### Sum
This is a script designed to find the percentage of a countries population that dwell in cities(presuming that all cities are listed here).

``` sql
SELECT co.name, 100 * SUM(ci.population) / co.population as "City Dwelling Percentage"  
FROM country co  
    JOIN city ci on co.code = ci.CountryCode  
GROUP BY co.Code  
``` 
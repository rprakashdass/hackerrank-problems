SELECT DISTINCT CITY FROM STATION
WHERE (
    CITY NOT LIKE '%a' AND CITY NOT LIKE '%E' AND  CITY NOT LIKE '%i' AND CITY NOT LIKE '%O' AND  CITY NOT LIKE '%U'
    ) AND (
    CITY NOT LIKE 'a%' AND CITY NOT LIKE 'E%' AND  CITY NOT LIKE 'i%' AND CITY NOT LIKE 'O%' AND  CITY NOT LIKE 'U%'
    );
-- @block
-- Get all ports
SELECT * FROM ports;

-- @block
-- Get all regions
SELECT * FROM regions;

-- @block
-- Join regions on ports
SELECT *
FROM ports
JOIN regions
ON ports.parent_slug = regions.slug;







-- @block
-- Query 1
SELECT prices.orig_code, prices.dest_code, prices.day, ROUND(AVG(prices.price), 0)

FROM
(SELECT *
FROM regions
INNER JOIN ports
ON regions.parent_slug = ports.parent_slug) AS result

FULL OUTER JOIN prices
ON prices.orig_code = result.code
WHERE prices.orig_code = 'CNGGZ' AND prices.dest_code = 'EETLL' AND day BETWEEN '2016-01-01' AND '2016-01-10'
GROUP BY prices.orig_code, prices.dest_code, prices.day;

-- @block
-- Query 2
SELECT prices.day, ROUND(AVG(prices.price), 0) AS average_price

FROM
(SELECT *
FROM regions
INNER JOIN ports
ON regions.parent_slug = ports.parent_slug) AS result

FULL OUTER JOIN prices
ON prices.orig_code = result.code
WHERE prices.orig_code = 'CNGGZ' AND prices.dest_code = 'EETLL' AND day BETWEEN '2016-01-01' AND '2016-01-10'
GROUP BY prices.day;

-- @block

SELECT day,
    CASE
        WHEN COUNT(prices.price) >= 3 THEN ROUND(AVG(prices.price), 0)
        WHEN COUNT(prices.price) < 3 THEN NULL
    END AS average_price
FROM prices
    WHERE prices.orig_code IN ('CNGZZ')
    AND prices.dest_code IN ('EETLL')
    AND day >= '2016-01-01'
    AND day <= '2016-01-10'
GROUP BY day
ORDER BY day

-- @block
-- Get Location Codes

SELECT ports.code
FROM ports
JOIN regions
ON ports.parent_slug = regions.slug
WHERE regions.parent_slug = 'EETLL' OR ports.code = 'EETLL' OR ports.parent_slug = 'EETLL';

-- @block
-- Get Location Codes

SELECT ports.code
FROM ports
INNER JOIN regions
ON ports.parent_slug = regions.slug
WHERE regions.parent_slug = 'balticddd' OR ports.code = 'EETLLddd' OR ports.parent_slug = 'north_europe_main';
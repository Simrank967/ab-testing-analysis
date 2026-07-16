SELECT
    "most ads day" AS day,
    COUNT(*) AS users,
    SUM(converted) AS conversions,
    ROUND(AVG(converted) * 100, 2) AS conversion_rate
FROM marketing
GROUP BY "most ads day"
ORDER BY conversion_rate DESC;
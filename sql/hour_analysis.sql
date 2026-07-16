SELECT
    "most ads hour" AS hour,
    COUNT(*) AS users,
    SUM(converted) AS conversions,
    ROUND(AVG(converted) * 100, 2) AS conversion_rate
FROM marketing
GROUP BY "most ads hour"
ORDER BY conversion_rate DESC;
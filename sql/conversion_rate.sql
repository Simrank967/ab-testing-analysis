SELECT
    "test group" AS test_group,
    COUNT(*) AS total_users,
    SUM(converted) AS conversions,
    ROUND(AVG(converted) * 100, 2) AS conversion_rate
FROM marketing
GROUP BY "test group";
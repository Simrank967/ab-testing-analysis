-- Segment users based on ad exposure

SELECT
    CASE
        WHEN "total ads" <= 10 THEN 'Low Exposure (<=10)'
        WHEN "total ads" <= 25 THEN 'Medium Exposure (11-25)'
        ELSE 'High Exposure (>25)'
    END AS ad_exposure,

    "test group",

    COUNT(*) AS users,

    SUM(converted) AS conversions,

    ROUND(AVG(converted) * 100, 2) AS conversion_rate

FROM marketing

GROUP BY ad_exposure, "test group"

ORDER BY ad_exposure, "test group";
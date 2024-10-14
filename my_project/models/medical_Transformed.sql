-- models/medical_transformed.sql
{{ config(materialized='table') }}

WITH filtered_data AS (
    SELECT
        "Channel Title",
        "Channel Username",
        "ID",
        "Message",
        "Date",
        "Media Path"
    FROM {{ ref('medical_data') }}
    WHERE "Message" IS NOT NULL  -- Filter out rows where the Message is NULL
)

SELECT
    "Channel Title",
    "Channel Username",
    COUNT("ID") AS total_messages,
    MIN("Date") AS first_message,
    MAX("Date") AS last_message
FROM filtered_data
GROUP BY "Channel Title", "Channel Username"
ORDER BY total_messages DESC

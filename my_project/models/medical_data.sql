-- models/medical_data.sql
{{ config(materialized='table') }}

WITH filtered_data AS (
    SELECT 
        "Channel Title",
        "Channel Username",
        "ID",
        "Message",
        "Date",
        "Media Path"
    FROM public.medical_data  -- Reference the table in the public schema
    WHERE "Message" IS NOT NULL
)

SELECT * 
FROM filtered_data

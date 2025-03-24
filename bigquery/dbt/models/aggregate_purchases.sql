WITH user_purchases AS (
    SELECT
        user_id,
        SUM(price * quantity) AS total_spent,
        COUNT(DISTINCT product_id) AS total_products
    FROM
        {{ ref('raw_ecommerce_data') }}
    GROUP BY
        user_id
)

SELECT * FROM user_purchases;

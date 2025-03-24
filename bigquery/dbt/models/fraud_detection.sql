-- Fraud detection logic to identify high-risk transactions

WITH fraud_transactions AS (
    SELECT
        user_id,
        product_id,
        category,
        price,
        quantity,
        timestamp,
        fraud_flag
    FROM
        {{ ref('raw_ecommerce_data') }}
    WHERE
        fraud_flag = TRUE
)

SELECT * FROM fraud_transactions;

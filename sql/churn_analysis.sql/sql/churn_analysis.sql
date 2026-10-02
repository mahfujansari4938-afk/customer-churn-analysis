-- Customer Churn Analysis

-- 1. Total customers
SELECT COUNT(*) AS total_customers
FROM customer_churn;


-- 2. Churn count
SELECT Churn, COUNT(*) AS customer_count
FROM customer_churn
GROUP BY Churn;


-- 3. Churn rate
SELECT
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 2
    ) AS churn_rate
FROM customer_churn;


-- 4. Average monthly charges by churn
SELECT
    Churn,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
FROM customer_churn
GROUP BY Churn;


-- 5. Churn by contract
SELECT
    Contract,
    Churn,
    COUNT(*) AS customer_count
FROM customer_churn
GROUP BY Contract, Churn
ORDER BY Contract;


-- 6. Churn by payment method
SELECT
    PaymentMethod,
    Churn,
    COUNT(*) AS customer_count
FROM customer_churn
GROUP BY PaymentMethod, Churn
ORDER BY PaymentMethod;

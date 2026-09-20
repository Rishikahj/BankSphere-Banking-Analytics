USE banksphere;

DROP TABLE IF EXISTS bank_customers;

CREATE TABLE bank_customers (
    id INT,
    credit_score INT,
    gender VARCHAR(20),
    age INT,
    occupation VARCHAR(100),
    balance BIGINT,
    monthly_income BIGINT,
    origin_province VARCHAR(100),
    tenure_years INT,
    married INT,
    number_of_cards INT,
    number_of_services INT,
    active_member BOOLEAN,
    last_active_date DATE,
    last_transaction_value BIGINT,
    created_date DATE,
    exit BOOLEAN,
    customer_segment VARCHAR(50),
    engagement_score INT,
    loyalty_level VARCHAR(50),
    digital_behavior VARCHAR(50),
    risk_score INT,
    risk_segment VARCHAR(50),
    cluster_group INT
);
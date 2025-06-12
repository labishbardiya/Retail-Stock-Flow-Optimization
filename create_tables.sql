CREATE TABLE Stores (
    store_id VARCHAR(10) PRIMARY KEY,
    region VARCHAR(50)
);

CREATE TABLE Products (
    product_id VARCHAR(10) PRIMARY KEY,
    category VARCHAR(50)
);

CREATE TABLE Calendar (
    date DATE PRIMARY KEY,
    seasonality VARCHAR(20),
    weather VARCHAR(20),
    is_holiday BOOLEAN
);

CREATE TABLE Inventory_Transactions (
    transaction_id SERIAL PRIMARY KEY,
    date DATE REFERENCES Calendar(date),
    store_id VARCHAR(10) REFERENCES Stores(store_id),
    product_id VARCHAR(10) REFERENCES Products(product_id),
    inventory_level INT,
    units_sold INT,
    units_ordered INT,
    demand_forecast FLOAT,
    price FLOAT,
    discount FLOAT,
    competitor_price FLOAT
);
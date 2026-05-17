-- CREACIÓN DE LAS TABLAS PARA EL EJERCICIO


-- TABLA CUSTOMERS
CREATE TABLE customers (
    id SMALLINT PRIMARY KEY,
    first_name VARCHAR(64),
    last_name VARCHAR(64)
);

-- TABLA CAMPAIGNS
CREATE TABLE campaigns(
    id SMALLINT PRIMARY KEY,
    customer_id SMALLINT,
    name VARCHAR(64)
);

-- TABLA EVENTS
CREATE TABLE events(
    dt VARCHAR(19),
    campaing_id SMALLINT,
    status VARCHAR(64)
);
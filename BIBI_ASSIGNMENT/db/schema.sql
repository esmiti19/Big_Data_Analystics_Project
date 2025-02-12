CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    visitor_id VARCHAR(255),
    item_id VARCHAR(255),
    event_type VARCHAR(50),
    timestamp TIMESTAMP
);

CREATE TABLE item_properties (
    item_id VARCHAR(255),
    property_name VARCHAR(255),
    property_value VARCHAR(255),
    PRIMARY KEY (item_id, property_name)
);

CREATE TABLE category_tree (
    category_id VARCHAR(255) PRIMARY KEY,
    parent_category_id VARCHAR(255),
    category_name VARCHAR(255)
);

use db1;

DROP TABLE customer;
DROP TABLE magazine;
DROP TABLE newspaper;
DROP TABLE sub_magazine;
DROP TABLE sub_newspaper;

CREATE TABLE customer (
    id_no INT,
    c_name VARCHAR(20) unique,
    address VARCHAR(40),
    PRIMARY KEY (id_no)
);

CREATE TABLE magazine (
    pm_name VARCHAR(20),
    frequency VARCHAR(10),
    no_of_issue INT,
    subscriptionrate DECIMAL(10 , 5 ),
    PRIMARY KEY (pm_name)
);

CREATE TABLE newspaper (
    pn_name VARCHAR(20),
    frequency VARCHAR(20),
    no_of_issues INT,
    subscriptionrate DECIMAL(10 , 5 ),
    PRIMARY KEY (pn_name)
);

CREATE TABLE sub_magazine (
    tm_no INT,
    id_no INT,
    pm_name VARCHAR(20),
    start_date DATE,
    end_date DATE,
    actual_end_date DATE,
    active_flag BOOLEAN,
    PRIMARY KEY (tm_no),
    FOREIGN KEY (id_no)
        REFERENCES customer (id_no),
    FOREIGN KEY (pm_name)
        REFERENCES magazine (pm_name)
);

CREATE TABLE sub_newspaper (
    tn_no INT,
    id_no INT,
    pn_name VARCHAR(20),
    start_date DATE,
    end_date DATE,
    actual_end_date DATE,
    active_flag BOOLEAN,
    PRIMARY KEY (tn_no),
    FOREIGN KEY (id_no)
        REFERENCES customer (id_no),
    FOREIGN KEY (pn_name)
        REFERENCES newspaper (pn_name)
);
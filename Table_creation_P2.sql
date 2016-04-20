use subscriptiondb;

DROP TABLE magazine_subscription_rate;
DROP TABLE daily_newspaper_rate;
DROP TABLE weekly_newspaper_rate;
DROP TABLE sub_newspaper_daily;
DROP TABLE sub_newspaper_weekly;
DROP TABLE sub_magazine;
DROP TABLE newspaper_daily;
DROP TABLE newspaper_weekly;
DROP TABLE magazine;
DROP TABLE customer;

CREATE TABLE magazine (
    pm_name VARCHAR(20),
    frequency VARCHAR(10),
    editorm_name VARCHAR(20),
    PRIMARY KEY (pm_name)
);

CREATE TABLE sub_magazine (
    id_no INT,
    pm_name VARCHAR(20),
    no_of_issues INT,
    start_date DATE,
    end_date DATE NOT NULL,   
    actual_end_date DATE,
    active_flag BOOLEAN,
    cost DECIMAL(10,5),
    PRIMARY KEY (id_no,pm_name),
    FOREIGN KEY (id_no)
        REFERENCES customer (id_no),
    FOREIGN KEY (pm_name)
        REFERENCES magazine (pm_name)
);

CREATE TABLE magazine_subscription_rate (
    pm_name VARCHAR(20),
    state VARCHAR(20),
    rate DECIMAL(10 , 5 ),
    PRIMARY KEY (pm_name, state),
    FOREIGN KEY (pm_name)
        REFERENCES magazine (pm_name)
);

CREATE TABLE newspaper_daily(
    pn_name VARCHAR(20),
    editor_nd_name VARCHAR(20),
    PRIMARY KEY (pn_name)
);

CREATE TABLE sub_newspaper_daily (
    id_no INT,
    pnd_name VARCHAR(20),
    start_date DATE,
    end_date DATE,
    actual_end_date DATE,
    active_flag BOOLEAN,
    sub_type int,
    cost DECIMAL(10,5),
    PRIMARY KEY (id_no, pnd_name),
    FOREIGN KEY (id_no)
        REFERENCES customer (id_no),
    FOREIGN KEY (pnd_name)
        REFERENCES newspaper_daily (pn_name)
);

CREATE TABLE daily_newspaper_rate (
    id_no INT,
    dnr_name VARCHAR(20),
    rate DECIMAL(10 , 5 ),
    PRIMARY KEY (id_no,dnr_name),
    FOREIGN KEY (id_no)
        REFERENCES sub_newspaper_daily (id_no),
    FOREIGN KEY (dnr_name)
        REFERENCES sub_newspaper_daily (pnd_name)
);

CREATE TABLE newspaper_weekly(
    pn_name VARCHAR(20),
    editor_nw_name VARCHAR(20),
    PRIMARY KEY (pn_name)
);

CREATE TABLE sub_newspaper_weekly (
    id_no INT,
    pnw_name VARCHAR(20),
    start_date DATE,
    end_date DATE,
    actual_end_date DATE,
    active_flag BOOLEAN,
    cost DECIMAL(10,5),
    PRIMARY KEY (id_no, pnw_name),
    FOREIGN KEY (id_no)
        REFERENCES customer (id_no),
    FOREIGN KEY (pnw_name)
        REFERENCES newspaper_weekly (pn_name)
);

CREATE TABLE weekly_newspaper_rate (
    id_no INT,
    wnr_name VARCHAR(20),
    rate DECIMAL(10 , 5 ),
    PRIMARY KEY (id_no,wnr_name),
    FOREIGN KEY (id_no)
        REFERENCES sub_newspaper_weekly (id_no),
    FOREIGN KEY (wnr_name)
        REFERENCES sub_newspaper_weekly (pnw_name)
);

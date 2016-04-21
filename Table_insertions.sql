INSERT INTO customer(cname, address) VALUES("L.Robert","101 Fischer Lane");
INSERT INTO customer(cname, address) VALUES("K.William","102 Norrington West");
INSERT INTO customer(cname, address) VALUES("F.Rocky","221 Baket st.");
INSERT INTO customer(cname, address) VALUES("A.Fredrick","104 Bloomington Heights");
INSERT INTO customer(cname, address) VALUES("S.Smith","104 Bloomington Heights");

INSERT INTO magazine (pm_name , frequency, editorm_name) values ("Vogue", "Weekly", "D.Cramer");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("NewsToday", "Monthly", "M.White");

INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("NewsToday" , "Alaska" , 15);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("NewsToday" , "Alabama" , 15);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("NewsToday" , "Texas" , 5);

INSERT INTO sub_magazine (id_no, pm_name, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost ) 
values (1, "NewsToday", 1, current_date(), '2017-05-19','2017-05-19',1,180);

SELECT 
    m1.pm_name, m1.frequency, m2.state, m2.rate
FROM
    magazine m1,
    magazine_subscription_rate m2
WHERE
    m1.pm_name = m2.pm_name    ;
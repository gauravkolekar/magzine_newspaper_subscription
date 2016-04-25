INSERT INTO customer(cname, address) VALUES("L.Robert","101 Fischer Lane");
INSERT INTO customer(cname, address) VALUES("K.William","102 Norrington West");
INSERT INTO customer(cname, address) VALUES("F.Rocky","221 Baket st.");
INSERT INTO customer(cname, address) VALUES("A.Fredrick","104 Bloomington Heights");
INSERT INTO customer(cname, address) VALUES("S.Smith","104 Bloomington Heights");
INSERT INTO customer(cname, address) VALUES("L.Mark","101 Random Lane");
INSERT INTO customer(cname, address) VALUES("K.Justin","102 Criag West");
INSERT INTO customer(cname, address) VALUES("F.Tucker","221 Baker st.");
INSERT INTO customer(cname, address) VALUES("A.John","107 Cloomington Heights");
INSERT INTO customer(cname, address) VALUES("S.Sam","110 Connery St");
INSERT INTO customer(cname, address) VALUES("L.Root","101 Fischer Lane");
INSERT INTO customer(cname, address) VALUES("R.William","Philly West");
INSERT INTO customer(cname, address) VALUES("Cramer","Tim Lane");
INSERT INTO customer(cname, address) VALUES("Mark","Bloomington Heights");
INSERT INTO customer(cname, address) VALUES("P.Smith","110 Bloomington Lane");

INSERT INTO magazine (pm_name , frequency, editorm_name) values ("Vogue", "Weekly", "D.Cramer");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("NewsToday", "Monthly", "M.White");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("Finance", "Yearly", "M.Carrol");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("Health", "Monthly", "M.Carl");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("AutoCar", "Weekly", "Rachel");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("Scientific America", "Weekly", "D.Wenner");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("Statistics Dose", "Monthly", "M.Ralph");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("Business Standard", "Yearly", "M.Carl");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("Diet", "Weekly", "M.Wolf");
INSERT INTO magazine (pm_name , frequency, editorm_name) values ("AutoCard", "Weekly", "Mitchell");

INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("Vogue" , "Alaska" , 15);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("NewsToday" , "Alabama" , 15);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("Finance" , "Texas" , 5);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("Health" , "Alabama" , 15);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("AutoCar" , "Texas" , 5);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("Scientific America" , "Alaska" , 15);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("Statistics Dose" , "Alabama" , 15);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("Business Standard" , "Texas" , 5);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("Diet" , "Alabama" , 15);
INSERT INTO magazine_subscription_rate (pm_name, state, rate ) VALUES ("AutoCard" , "Texas" , 5);

INSERT INTO sub_magazine (id_no, pm_name, state, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost ) 
values (1, "Vogue", "Alaska",1, current_date(), '2017-05-19','2017-05-19',1,10500);

INSERT INTO sub_magazine (id_no, pm_name, state, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost ) 
values (2, "NewsToday", "Alabama",1, current_date(), '2017-05-19','2017-05-19',1,5500);


INSERT INTO newspaper_daily (pn_name , editor_nd_name) values ("Daily News", "D.Cramer");
INSERT INTO newspaper_daily (pn_name , editor_nd_name) values ("NewsDaily", "M.White");
INSERT INTO newspaper_daily (pn_name , editor_nd_name) values ("Finance Times", "M.Carrol");


INSERT INTO daily_newspaper_rate (dnr_name, state, rate ) VALUES ("Daily News" , "Alaska" , 15);
INSERT INTO daily_newspaper_rate (dnr_name, state, rate ) VALUES ("NewsDaily" , "Alabama" , 15);
INSERT INTO daily_newspaper_rate (dnr_name, state, rate ) VALUES ("Finance Times" , "Texas" , 5);

INSERT INTO sub_newspaper_daily(id_no, pnd_name, state, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost)
values (3, "Daily News","Alaska",1, current_date(), '2017-05-19','2017-05-19',1,10500);

INSERT INTO sub_newspaper_daily(id_no, pnd_name, state, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost)
values (4, "NewsDaily","Alabama",1, current_date(), '2017-05-19','2017-05-19',1,5500);

INSERT INTO newspaper_weekly (pn_name , editor_nw_name) values ("Weekly News", "D.Cramer");
INSERT INTO newspaper_weekly (pn_name , editor_nw_name) values ("NewsWeekly", "M.White");
INSERT INTO newspaper_weekly (pn_name , editor_nw_name) values ("Roman Times", "M.Carrol");

INSERT INTO weekly_newspaper_rate (wnr_name, state, rate ) VALUES ("Weekly News" , "Alaska" , 15);
INSERT INTO weekly_newspaper_rate (wnr_name, state, rate ) VALUES ("NewsWeekly" , "Alabama" , 15);
INSERT INTO weekly_newspaper_rate (wnr_name, state, rate ) VALUES ("Roman Times" , "Texas" , 5);

INSERT INTO sub_newspaper_weekly(id_no, pnw_name, state, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost)
values (5, "Weekly News","Alaska",1, current_date(), '2017-05-19','2017-05-19',1,10500);

INSERT INTO sub_newspaper_weekly(id_no, pnw_name, state, no_of_issues, start_date, end_date, actual_end_date, active_flag, cost)
values (6, "NewsWeekly","Alabama",1, current_date(), '2017-05-19','2017-05-19',1,5500);
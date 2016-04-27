DELIMITER $$
USE `db1`$$
CREATE PROCEDURE `Active_flag_handle_newsd` ()
BEGIN



Update sub_newspaper_daily set active_flag = 0 where end_date < current_date();

commit;

END$$

DELIMITER ;
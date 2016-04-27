DELIMITER $$
USE `db1`$$
CREATE PROCEDURE `Active_flag_handle` ()
BEGIN



Update sub_magazine set active_flag = 0 where end_date < current_date();

commit;

END$$

DELIMITER ;
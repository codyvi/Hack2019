DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetAllMembers`()
BEGIN
   SELECT *  FROM Member;
   END$$
DELIMITER ;
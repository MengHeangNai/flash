CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;

DROP TABLE IF EXISTS `sellers`;
 
CREATE TABLE `sellers` (
  `seller_id` varchar(45) NOT NULL,
  `seller_zip_code_prefix` decimal(5,0) DEFAULT NULL,
  `seller_city` varchar(45) DEFAULT NULL,
  `seller_state` char(2) DEFAULT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 

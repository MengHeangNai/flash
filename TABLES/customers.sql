 

CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;


DROP TABLE IF EXISTS `customers`;
 
CREATE TABLE `customers` (
  `customer_id` varchar(45) NOT NULL,
  `customer_unique_id` varchar(45) NOT NULL,
  `customer_zip_code_prefix` int DEFAULT NULL,
  `customer_city` varchar(25) DEFAULT NULL,
  `customer_state` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `customer_id_UNIQUE` (`customer_id`),
  UNIQUE KEY `customer_unique_id_UNIQUE` (`customer_unique_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
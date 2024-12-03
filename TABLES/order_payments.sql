
CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;


DROP TABLE IF EXISTS `order_payments`;
 
CREATE TABLE `order_payments` (
  `order_id` varchar(45) NOT NULL,
  `payment_sequential` int DEFAULT NULL,
  `payment_type` varchar(15) DEFAULT NULL,
  `payment_installments` int DEFAULT NULL,
  `payment_value` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

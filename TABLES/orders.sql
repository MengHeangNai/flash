CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;

DROP TABLE IF EXISTS `orders`;
 
CREATE TABLE `orders` (
  `order_id` varchar(45) NOT NULL,
  `customer_id` varchar(45) DEFAULT NULL,
  `order_status` varchar(15) DEFAULT NULL,
  `order_purchase_timestamp` datetime DEFAULT NULL,
  `order_approved_at` datetime DEFAULT NULL,
  `order_delivered_carrier_date` datetime DEFAULT NULL,
  `order_delivered_customer_date` datetime DEFAULT NULL,
  `order_estimated_delivery_date` datetime DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 
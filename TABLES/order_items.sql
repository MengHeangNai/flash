CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;

DROP TABLE IF EXISTS `order_items`;
 
CREATE TABLE `order_items` (
  `order_id` varchar(45) NOT NULL,
  `order_item_id` int DEFAULT NULL,
  `product_id` varchar(45) DEFAULT NULL,
  `seller_id` varchar(45) DEFAULT NULL,
  `shipping_limit_date` datetime DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `freight_value` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

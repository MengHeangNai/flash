CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;

DROP TABLE IF EXISTS `product_category_name_translation`;
 
CREATE TABLE `product_category_name_translation` (
  `product_category_name` varchar(45) NOT NULL,
  `product_category_name_english` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`product_category_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

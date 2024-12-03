CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;

DROP TABLE IF EXISTS `products`;
 
CREATE TABLE `products` (
  `product_id` varchar(45) NOT NULL,
  `product_category_name` varchar(60) DEFAULT NULL,
  `product_name_lenght` int DEFAULT NULL,
  `product_description_lenght` int DEFAULT NULL,
  `product_photos_qty` int DEFAULT NULL,
  `product_weight_g` decimal(10,3) DEFAULT NULL,
  `product_length_cm` decimal(10,0) DEFAULT NULL,
  `product_height_cm` decimal(10,0) DEFAULT NULL,
  `product_width_cm` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
 

CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;

DROP TABLE IF EXISTS `geolocation`;
 
CREATE TABLE `geolocation` (
  `geolocation_zip_code_prefix` int NOT NULL,
  `geolocation_lat` decimal(9,6) DEFAULT NULL,
  `geolocation_lng` decimal(9,6) DEFAULT NULL,
  `geolocation_city` varchar(45) DEFAULT NULL,
  `geolocation_state` char(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

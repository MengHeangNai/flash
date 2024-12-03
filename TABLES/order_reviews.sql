CREATE DATABASE IF NOT EXISTS shopsphere;
USE shopsphere;

DROP TABLE IF EXISTS `order_reviews`;
 
CREATE TABLE `order_reviews` (
  `review_id` varchar(45) NOT NULL,
  `order_id` varchar(45) DEFAULT NULL,
  `review_score` int DEFAULT NULL,
  `review_comment_title` varchar(50) DEFAULT NULL,
  `review_comment_message` varchar(250) DEFAULT NULL,
  `review_creation_date` datetime DEFAULT NULL,
  `review_answer_timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

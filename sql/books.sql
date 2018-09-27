CREATE TABLE `books` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `price` varchar(16) DEFAULT NULL,
  `typeId` bigint(20) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `press` varchar(255) DEFAULT NULL,
  `number` int DEFAULT NULL,
  `orderId` bigint(20),
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_book_type_id` FOREIGN KEY (`typeId`) REFERENCES `book_type` (`id`),
  CONSTRAINT `FK_book_order_id` FOREIGN KEY (`orderId`) REFERENCES `order` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
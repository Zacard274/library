CREATE TABLE `books` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `price` varchar(16) DEFAULT NULL,
  `type_id` bigint(20) DEFAULT NULL,
  `author` varchar(256) DEFAULT NULL,
  `press` varchar(255) DEFAULT NULL,
  `number` int DEFAULT NULL,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_book_type_id` FOREIGN KEY (`type_id`) REFERENCES `book_type` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
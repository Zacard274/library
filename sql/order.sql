CREATE TABLE `order` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bookId` bigint(20) DEFAULT NULL,
  `sum` varchar(16) DEFAULT NULL,
  `orderStatus` tinyint(3) DEFAULT NULL,
  `orderType` tinyint(3) DEFAULT NULL,
  `removed` tinyint(1) DEFAULT NULL,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
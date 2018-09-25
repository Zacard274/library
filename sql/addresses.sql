CREATE TABLE `addresses`(
`id` bigint(20) NOT NULL,
`userId` bigint(20) NOT NULL,
`address` varchar(255) DEFAULT NULL,
`selected` tinyint(1) DEFAULT NULL,
`removed` tinyint(1) DEFAULT 0,
PRIMARY KEY (`id`),
FOREIGN KEY (`userId`) REFERENCES `user` (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
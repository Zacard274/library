CREATE TABLE `oauth2session` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `accessToken` varchar(255) DEFAULT NULL,
  `accessTokenExpireTime` datetime DEFAULT NULL,
  `refreshToken` varchar(255) DEFAULT NULL,
  `removed` tinyint(1) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `uniqueId` varchar(255) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniqueId` (`uniqueId`),
  KEY `FKABA7E99B47140EFE` (`user_id`),
  CONSTRAINT `FKABA7E99B47140EFE` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
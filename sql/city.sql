-- MySQL dump 10.13  Distrib 5.7.21, for osx10.13 (x86_64)
--
-- Host: localhost    Database: fan
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `city` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `isVisible` tinyint(1) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `northEastLatitude` double DEFAULT NULL,
  `northEastLongitude` double DEFAULT NULL,
  `southWestLatitude` double DEFAULT NULL,
  `southWestLongitude` double DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `denyOrder` tinyint(1) DEFAULT NULL,
  `areaCode` varchar(255) DEFAULT NULL,
  `localNumberLength` int(11) DEFAULT NULL,
  `meicanExtensionNumberPrefix` varchar(255) DEFAULT NULL,
  `isInBadWeather` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cityUrlIndex` (`url`)
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES (1,1,39.904214,116.407413,'北京',40.2164962,116.7829835,39.6612714,116.0119343,'beijing',0,'10',8,'',0),(2,1,23.129163,113.264435,'广州',23.555094,113.7332153,22.6961015,112.7224731,'guangzhou',0,'20',8,'8',0),(3,1,39.1613,117.2147,'天津',39.4468325,117.8118896,38.8032309,116.7791748,'tianjin',0,'22',8,'6',0),(4,1,22.543099,114.057868,'深圳',22.7809313,114.3553162,22.3293893,113.7524414,'shenzhen',0,'755',8,'5',0),(5,1,31.230393,121.473704,'上海',31.6688967,122.1137989,30.7798012,120.8397067,'shanghai',0,'21',8,'9',0),(6,0,NULL,NULL,'安庆',NULL,NULL,NULL,NULL,'anqing',1,'325',NULL,NULL,0),(7,0,NULL,NULL,'鞍山',NULL,NULL,NULL,NULL,'anshan',1,'412',NULL,NULL,0),(8,0,NULL,NULL,'保定',NULL,NULL,NULL,NULL,'baoding',1,'312',NULL,NULL,0),(9,0,NULL,NULL,'包头',NULL,NULL,NULL,NULL,'baotou',1,'472',NULL,NULL,0),(10,0,NULL,NULL,'蚌埠',NULL,NULL,NULL,NULL,'bengbu',1,'552',NULL,NULL,0),(11,0,NULL,NULL,'本溪',NULL,NULL,NULL,NULL,'benxi',1,'414',NULL,NULL,0),(12,0,NULL,NULL,'沧州',NULL,NULL,NULL,NULL,'cangzhou',1,'317',NULL,NULL,0),(13,0,NULL,NULL,'长春',NULL,NULL,NULL,NULL,'changchun',1,'431',NULL,NULL,0),(14,0,NULL,NULL,'常德',NULL,NULL,NULL,NULL,'changde',1,'736',NULL,NULL,0),(15,1,NULL,NULL,'长沙',NULL,NULL,NULL,NULL,'changsha',0,'731',NULL,NULL,0),(16,0,NULL,NULL,'常熟',NULL,NULL,NULL,NULL,'changshu',1,'520',NULL,NULL,0),(17,0,NULL,NULL,'长治',NULL,NULL,NULL,NULL,'changzhi',1,'355',NULL,NULL,0),(18,0,NULL,NULL,'常州',NULL,NULL,NULL,NULL,'changzhou',1,'519',NULL,NULL,0),(19,0,NULL,NULL,'朝阳',NULL,NULL,NULL,NULL,'chaoyang',1,'42',NULL,NULL,0),(20,0,NULL,NULL,'潮州',NULL,NULL,NULL,NULL,'chaozhou',1,'768',NULL,NULL,0),(21,0,NULL,NULL,'承德',NULL,NULL,NULL,NULL,'chengde',1,'314',NULL,NULL,0),(22,1,30.572269,104.066541,'成都',30.85817,104.326172,30.458888,103.824921,'chengdu',1,'28',8,NULL,0),(23,0,NULL,NULL,'赤峰',NULL,NULL,NULL,NULL,'chifeng',1,'476',NULL,NULL,0),(24,0,NULL,NULL,'楚雄',NULL,NULL,NULL,NULL,'chuxiong',1,'878',NULL,NULL,0),(25,0,NULL,NULL,'慈溪',NULL,NULL,NULL,NULL,'cixi',1,'574',NULL,NULL,0),(26,0,NULL,NULL,'大理',NULL,NULL,NULL,NULL,'dali',1,'872',NULL,NULL,0),(27,1,NULL,NULL,'大连',NULL,NULL,NULL,NULL,'dalian',0,'411',NULL,NULL,0),(28,0,NULL,NULL,'丹东',NULL,NULL,NULL,NULL,'dandong',1,'415',NULL,NULL,0),(29,0,NULL,NULL,'大庆',NULL,NULL,NULL,NULL,'daqing',1,'459',NULL,NULL,0),(30,0,NULL,NULL,'大同',NULL,NULL,NULL,NULL,'datong',1,'352',NULL,NULL,0),(31,0,NULL,NULL,'德阳',NULL,NULL,NULL,NULL,'deyang',1,'838',NULL,NULL,0),(32,0,NULL,NULL,'东莞',NULL,NULL,NULL,NULL,'dongguan',1,'769',NULL,NULL,0),(33,0,NULL,NULL,'东阳',NULL,NULL,NULL,NULL,'dongyang',1,'579',NULL,NULL,0),(34,0,NULL,NULL,'东营',NULL,NULL,NULL,NULL,'dongying',1,'546',NULL,NULL,0),(35,0,NULL,NULL,'都江堰',NULL,NULL,NULL,NULL,'dujiangyan',1,'28',NULL,NULL,0),(36,0,NULL,NULL,'奉化',NULL,NULL,NULL,NULL,'fenghua',1,'574',NULL,NULL,0),(37,0,NULL,NULL,'佛山',NULL,NULL,NULL,NULL,'foshan',1,'757',NULL,NULL,0),(38,0,NULL,NULL,'福清',NULL,NULL,NULL,NULL,'fuqing',1,'591',NULL,NULL,0),(39,0,NULL,NULL,'抚顺',NULL,NULL,NULL,NULL,'fushun',1,'413',NULL,NULL,0),(40,0,NULL,NULL,'阜新',NULL,NULL,NULL,NULL,'fuxin',1,'418',NULL,NULL,0),(41,0,NULL,NULL,'富阳',NULL,NULL,NULL,NULL,'fuyang',1,'571',NULL,NULL,0),(42,1,NULL,NULL,'福州',NULL,NULL,NULL,NULL,'fuzhou',0,'591',NULL,NULL,0),(43,0,NULL,NULL,'桂林',NULL,NULL,NULL,NULL,'guilin',1,'773',NULL,NULL,0),(44,0,NULL,NULL,'哈尔滨',NULL,NULL,NULL,NULL,'haerbin',1,'451',NULL,NULL,0),(45,0,NULL,NULL,'海城',NULL,NULL,NULL,NULL,'haicheng',1,'412',NULL,NULL,0),(46,0,NULL,NULL,'海口',NULL,NULL,NULL,NULL,'haikou',1,'898',NULL,NULL,0),(47,0,NULL,NULL,'海宁',NULL,NULL,NULL,NULL,'haining',1,'573',NULL,NULL,0),(48,0,NULL,NULL,'邯郸',NULL,NULL,NULL,NULL,'handan',1,'310',NULL,NULL,0),(49,1,NULL,NULL,'杭州',NULL,NULL,NULL,NULL,'hangzhou',0,'571',8,NULL,0),(50,0,NULL,NULL,'合肥',NULL,NULL,NULL,NULL,'hefei',1,'551',NULL,NULL,0),(51,0,NULL,NULL,'衡阳',NULL,NULL,NULL,NULL,'hengyang',1,'734',NULL,NULL,0),(52,0,NULL,NULL,'淮北',NULL,NULL,NULL,NULL,'huaibei',1,'561',NULL,NULL,0),(53,0,NULL,NULL,'怀化',NULL,NULL,NULL,NULL,'huaihua',1,'745',NULL,NULL,0),(54,0,NULL,NULL,'淮南',NULL,NULL,NULL,NULL,'huainan',1,'554',NULL,NULL,0),(55,0,NULL,NULL,'黄石',NULL,NULL,NULL,NULL,'huangshi',1,'714',NULL,NULL,0),(56,0,NULL,NULL,'呼和浩特',NULL,NULL,NULL,NULL,'huhehaote',1,'471',NULL,NULL,0),(57,0,NULL,NULL,'惠州',NULL,NULL,NULL,NULL,'huizhou',1,'752',NULL,NULL,0),(58,0,NULL,NULL,'葫芦岛',NULL,NULL,NULL,NULL,'huludao',1,'429',NULL,NULL,0),(59,0,NULL,NULL,'湖州',NULL,NULL,NULL,NULL,'huzhou',1,'572',NULL,NULL,0),(60,0,NULL,NULL,'建德',NULL,NULL,NULL,NULL,'jiande',1,'571',NULL,NULL,0),(61,0,NULL,NULL,'江门',NULL,NULL,NULL,NULL,'jiangmen',1,'750',NULL,NULL,0),(62,0,NULL,NULL,'江阴',NULL,NULL,NULL,NULL,'jiangyin',1,'510',NULL,NULL,0),(63,0,NULL,NULL,'嘉兴',NULL,NULL,NULL,NULL,'jiaxing',1,'573',NULL,NULL,0),(64,0,NULL,NULL,'吉林',NULL,NULL,NULL,NULL,'jilin',1,'432',NULL,NULL,0),(65,0,NULL,NULL,'即墨',NULL,NULL,NULL,NULL,'jimo',1,'532',NULL,NULL,0),(66,0,NULL,NULL,'济南',NULL,NULL,NULL,NULL,'jinan',1,'531',NULL,NULL,0),(67,0,NULL,NULL,'景洪',NULL,NULL,NULL,NULL,'jinghong',1,'691',NULL,NULL,0),(68,0,NULL,NULL,'荆州',NULL,NULL,NULL,NULL,'jingzhou',1,'716',NULL,NULL,0),(69,0,NULL,NULL,'金华',NULL,NULL,NULL,NULL,'jinhua',1,'579',NULL,NULL,0),(70,0,NULL,NULL,'锦州',NULL,NULL,NULL,NULL,'jinzhou',1,'416',NULL,NULL,0),(71,0,NULL,NULL,'九江',NULL,NULL,NULL,NULL,'jiujiang',1,'792',NULL,NULL,0),(72,0,NULL,NULL,'开平',NULL,NULL,NULL,NULL,'kaiping',1,'750',NULL,NULL,0),(73,0,NULL,NULL,'昆明',NULL,NULL,NULL,NULL,'kunming',1,'871',NULL,NULL,0),(74,0,NULL,NULL,'昆山',NULL,NULL,NULL,NULL,'kunshan',1,'512',NULL,NULL,0),(75,0,NULL,NULL,'廊坊',NULL,NULL,NULL,NULL,'langfang',1,'316',NULL,NULL,0),(76,0,NULL,NULL,'兰州',NULL,NULL,NULL,NULL,'lanzhou',1,'931',NULL,NULL,0),(77,0,NULL,NULL,'辽阳',NULL,NULL,NULL,NULL,'liaoyang',1,'419',NULL,NULL,0),(78,0,NULL,NULL,'辽源',NULL,NULL,NULL,NULL,'liaoyuan',1,'437',NULL,NULL,0),(79,0,NULL,NULL,'丽江',NULL,NULL,NULL,NULL,'lijiang',1,'888',NULL,NULL,0),(80,0,NULL,NULL,'临安',NULL,NULL,NULL,NULL,'linan',1,'571',NULL,NULL,0),(81,0,NULL,NULL,'临汾',NULL,NULL,NULL,NULL,'linfen',1,'357',NULL,NULL,0),(82,0,NULL,NULL,'临海',NULL,NULL,NULL,NULL,'linhai',1,'576',NULL,NULL,0),(83,0,NULL,NULL,'临沂',NULL,NULL,NULL,NULL,'linyi',1,'539',NULL,NULL,0),(84,0,NULL,NULL,'丽水',NULL,NULL,NULL,NULL,'lishui',1,'578',NULL,NULL,0),(85,0,NULL,NULL,'溧阳',NULL,NULL,NULL,NULL,'liyang',1,'519',NULL,NULL,0),(86,0,NULL,NULL,'龙岩',NULL,NULL,NULL,NULL,'longyan',1,'597',NULL,NULL,0),(87,0,NULL,NULL,'洛阳',NULL,NULL,NULL,NULL,'luoyang',1,'379',NULL,NULL,0),(88,0,NULL,NULL,'马鞍山',NULL,NULL,NULL,NULL,'maanshan',1,'555',NULL,NULL,0),(89,0,NULL,NULL,'茂名',NULL,NULL,NULL,NULL,'maoming',1,'668',NULL,NULL,0),(90,0,NULL,NULL,'眉山',NULL,NULL,NULL,NULL,'meishan',1,'28',NULL,NULL,0),(91,0,NULL,NULL,'绵阳',NULL,NULL,NULL,NULL,'mianyang',1,'816',NULL,NULL,0),(92,0,NULL,NULL,'牡丹江',NULL,NULL,NULL,NULL,'mudanjiang',1,'453',NULL,NULL,0),(93,0,NULL,NULL,'南昌',NULL,NULL,NULL,NULL,'nanchang',1,'791',NULL,NULL,0),(94,0,NULL,NULL,'南充',NULL,NULL,NULL,NULL,'nanchong',1,'817',NULL,NULL,0),(95,1,NULL,NULL,'南京',NULL,NULL,NULL,NULL,'nanjing',0,'25',8,NULL,0),(96,1,NULL,NULL,'南宁',NULL,NULL,NULL,NULL,'nanning',1,'771',8,NULL,0),(97,0,NULL,NULL,'南通',NULL,NULL,NULL,NULL,'nantong',1,'513',NULL,NULL,0),(98,0,NULL,NULL,'宁波',NULL,NULL,NULL,NULL,'ningbo',1,'574',NULL,NULL,0),(99,0,NULL,NULL,'盘锦',NULL,NULL,NULL,NULL,'panjin',1,'427',NULL,NULL,0),(100,0,NULL,NULL,'平湖',NULL,NULL,NULL,NULL,'pinghu',1,'573',NULL,NULL,0),(101,0,NULL,NULL,'莆田',NULL,NULL,NULL,NULL,'putian',1,'591',NULL,NULL,0),(102,0,NULL,NULL,'濮阳',NULL,NULL,NULL,NULL,'puyang',1,'393',NULL,NULL,0),(103,0,NULL,NULL,'迁安',NULL,NULL,NULL,NULL,'qianan',1,'44',NULL,NULL,0),(104,1,NULL,NULL,'青岛',NULL,NULL,NULL,NULL,'qingdao',1,'532',8,NULL,0),(105,0,NULL,NULL,'清远',NULL,NULL,NULL,NULL,'qingyuan',1,'763',NULL,NULL,0),(106,0,NULL,NULL,'秦皇岛',NULL,NULL,NULL,NULL,'qinhuangdao',1,'335',NULL,NULL,0),(107,0,NULL,NULL,'齐齐哈尔',NULL,NULL,NULL,NULL,'qiqihaer',1,'452',NULL,NULL,0),(108,0,NULL,NULL,'泉州',NULL,NULL,NULL,NULL,'quanzhou',1,'595',NULL,NULL,0),(109,0,NULL,NULL,'曲靖',NULL,NULL,NULL,NULL,'qujing',1,'874',NULL,NULL,0),(110,0,NULL,NULL,'衢州',NULL,NULL,NULL,NULL,'quzhou',1,'570',NULL,NULL,0),(111,0,NULL,NULL,'瑞安',NULL,NULL,NULL,NULL,'ruian',1,'577',NULL,NULL,0),(112,0,NULL,NULL,'上虞',NULL,NULL,NULL,NULL,'shangyu',1,'575',NULL,NULL,0),(113,0,NULL,NULL,'汕头',NULL,NULL,NULL,NULL,'shantou',1,'754',NULL,NULL,0),(114,0,NULL,NULL,'韶关',NULL,NULL,NULL,NULL,'shaoguan',1,'751',NULL,NULL,0),(115,0,NULL,NULL,'绍兴',NULL,NULL,NULL,NULL,'shaoxing',1,'575',NULL,NULL,0),(116,0,NULL,NULL,'沈阳',NULL,NULL,NULL,NULL,'shenyang',1,'24',NULL,NULL,0),(117,0,NULL,NULL,'石家庄',NULL,NULL,NULL,NULL,'shijiazhuang',1,'311',NULL,NULL,0),(118,0,NULL,NULL,'石狮',NULL,NULL,NULL,NULL,'shishi',1,'595',NULL,NULL,0),(119,0,NULL,NULL,'十堰',NULL,NULL,NULL,NULL,'shiyan',1,'719',NULL,NULL,0),(120,0,NULL,NULL,'四平',NULL,NULL,NULL,NULL,'siping',1,'434',NULL,NULL,0),(121,0,NULL,NULL,'松原',NULL,NULL,NULL,NULL,'songyuan',1,'438',NULL,NULL,0),(122,0,NULL,NULL,'宿迁',NULL,NULL,NULL,NULL,'suqian',1,'527',NULL,NULL,0),(123,1,NULL,NULL,'苏州',NULL,NULL,NULL,NULL,'suzhou',0,'512',NULL,NULL,0),(124,0,NULL,NULL,'台山',NULL,NULL,NULL,NULL,'taishan',1,'750',NULL,NULL,0),(125,0,NULL,NULL,'太原',NULL,NULL,NULL,NULL,'taiyuan',1,'351',NULL,NULL,0),(126,0,NULL,NULL,'台州',NULL,NULL,NULL,NULL,'taizhou',1,'576',NULL,NULL,0),(127,0,NULL,NULL,'唐山',NULL,NULL,NULL,NULL,'tangshan',1,'315',NULL,NULL,0),(128,0,NULL,NULL,'天台',NULL,NULL,NULL,NULL,'tiantai',1,'576',NULL,NULL,0),(129,0,NULL,NULL,'通辽',NULL,NULL,NULL,NULL,'tongliao',1,'475',NULL,NULL,0),(130,0,NULL,NULL,'铜陵',NULL,NULL,NULL,NULL,'tongling',1,'562',NULL,NULL,0),(131,0,NULL,NULL,'桐乡',NULL,NULL,NULL,NULL,'tongxiang',1,'573',NULL,NULL,0),(132,0,NULL,NULL,'潍坊',NULL,NULL,NULL,NULL,'weifang',1,'536',NULL,NULL,0),(133,0,NULL,NULL,'威海',NULL,NULL,NULL,NULL,'weihai',1,'631',NULL,NULL,0),(134,0,NULL,NULL,'温岭',NULL,NULL,NULL,NULL,'wenling',1,'576',NULL,NULL,0),(135,0,NULL,NULL,'温州',NULL,NULL,NULL,NULL,'wenzhou',1,'577',NULL,NULL,0),(136,1,NULL,NULL,'武汉',NULL,NULL,NULL,NULL,'wuhan',0,'27',NULL,NULL,0),(137,0,NULL,NULL,'芜湖',NULL,NULL,NULL,NULL,'wuhu',1,'553',NULL,NULL,0),(138,1,NULL,NULL,'无锡',NULL,NULL,NULL,NULL,'wuxi',1,'510',8,NULL,0),(139,1,NULL,NULL,'厦门',NULL,NULL,NULL,NULL,'xiamen',0,'592',7,NULL,0),(140,1,NULL,NULL,'西安',NULL,NULL,NULL,NULL,'xian',1,'29',NULL,NULL,0),(141,0,NULL,NULL,'襄樊',NULL,NULL,NULL,NULL,'xiangfan',1,'710',NULL,NULL,0),(142,0,NULL,NULL,'咸阳',NULL,NULL,NULL,NULL,'xianyang',1,'29',NULL,NULL,0),(143,0,NULL,NULL,'西宁',NULL,NULL,NULL,NULL,'xining',1,'971',NULL,NULL,0),(144,0,NULL,NULL,'徐州',NULL,NULL,NULL,NULL,'xuzhou',1,'516',NULL,NULL,0),(145,0,NULL,NULL,'盐城',NULL,NULL,NULL,NULL,'yancheng',1,'515',NULL,NULL,0),(146,0,NULL,NULL,'阳江',NULL,NULL,NULL,NULL,'yangjiang',1,'662',NULL,NULL,0),(147,0,NULL,NULL,'扬州',NULL,NULL,NULL,NULL,'yangzhou',1,'514',NULL,NULL,0),(148,0,NULL,NULL,'延吉',NULL,NULL,NULL,NULL,'yanji',1,'433',NULL,NULL,0),(149,0,NULL,NULL,'烟台',NULL,NULL,NULL,NULL,'yantai',1,'535',NULL,NULL,0),(150,0,NULL,NULL,'宜昌',NULL,NULL,NULL,NULL,'yichang',1,'717',NULL,NULL,0),(151,0,NULL,NULL,'银川',NULL,NULL,NULL,NULL,'yinchuan',1,'951',NULL,NULL,0),(152,0,NULL,NULL,'营口',NULL,NULL,NULL,NULL,'yingkou',1,'417',NULL,NULL,0),(153,0,NULL,NULL,'义乌',NULL,NULL,NULL,NULL,'yiwu',1,'579',NULL,NULL,0),(154,0,NULL,NULL,'宜兴',NULL,NULL,NULL,NULL,'yixing',1,'510',NULL,NULL,0),(155,0,NULL,NULL,'永康',NULL,NULL,NULL,NULL,'yongkang',1,'579',NULL,NULL,0),(156,0,NULL,NULL,'乐清',NULL,NULL,NULL,NULL,'yueqing',1,'577',NULL,NULL,0),(157,0,NULL,NULL,'玉环',NULL,NULL,NULL,NULL,'yuhuan',1,'576',NULL,NULL,0),(158,0,NULL,NULL,'运城',NULL,NULL,NULL,NULL,'yuncheng',1,'359',NULL,NULL,0),(159,0,NULL,NULL,'玉溪',NULL,NULL,NULL,NULL,'yuxi',1,'877',NULL,NULL,0),(160,0,NULL,NULL,'余姚',NULL,NULL,NULL,NULL,'yuyao',1,'574',NULL,NULL,0),(161,0,NULL,NULL,'张家口',NULL,NULL,NULL,NULL,'zhangjiakou',1,'313',NULL,NULL,0),(162,0,NULL,NULL,'湛江',NULL,NULL,NULL,NULL,'zhanjiang',1,'759',NULL,NULL,0),(163,0,NULL,NULL,'肇庆',NULL,NULL,NULL,NULL,'zhaoqing',1,'578',NULL,NULL,0),(164,0,NULL,NULL,'郑州',NULL,NULL,NULL,NULL,'zhengzhou',1,'371',NULL,NULL,0),(165,0,NULL,NULL,'镇江',NULL,NULL,NULL,NULL,'zhenjiang',1,'511',NULL,NULL,0),(166,0,NULL,NULL,'中山',NULL,NULL,NULL,NULL,'zhongshan',1,'760',NULL,NULL,0),(167,0,NULL,NULL,'舟山',NULL,NULL,NULL,NULL,'zhoushan',1,'580',NULL,NULL,0),(168,1,NULL,NULL,'珠海',NULL,NULL,NULL,NULL,'zhuhai',0,'756',NULL,NULL,0),(169,0,NULL,NULL,'诸暨',NULL,NULL,NULL,NULL,'zhuji',1,'575',NULL,NULL,0),(170,0,NULL,NULL,'株洲',NULL,NULL,NULL,NULL,'zhuzhou',1,'733',NULL,NULL,0),(171,0,NULL,NULL,'淄博',NULL,NULL,NULL,NULL,'zibo',1,'533',NULL,NULL,0),(172,0,NULL,NULL,'遵化',NULL,NULL,NULL,NULL,'zunhua',1,'315',NULL,NULL,0),(173,1,NULL,NULL,'重庆',NULL,NULL,NULL,NULL,'chongqing',0,'023',NULL,NULL,0);
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-22 19:52:35

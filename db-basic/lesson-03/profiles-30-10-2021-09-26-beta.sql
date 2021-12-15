-- MariaDB dump 10.19  Distrib 10.5.12-MariaDB, for Linux (x86_64)
--
-- Host: mysql.hostinger.ro    Database: u574849695_25
-- ------------------------------------------------------
-- Server version	10.5.12-MariaDB-cll-lve

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles` (
  `user_id` bigint(20) unsigned NOT NULL,
  `gender` char(1) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `photo_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `hometown` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `profiles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles`
--

LOCK TABLES `profiles` WRITE;
/*!40000 ALTER TABLE `profiles` DISABLE KEYS */;
INSERT INTO `profiles` VALUES (101,'f','1982-03-11',NULL,'1972-01-29 23:14:25','axkn'),(102,'f','2000-11-14',NULL,'2016-12-01 23:17:33','rkps'),(103,'m','2005-03-30',NULL,'1971-01-31 05:41:06','zrdm'),(105,'m','2015-12-19',NULL,'1972-12-24 17:11:23','qnnm'),(109,'f','1987-09-07',NULL,'2010-12-30 22:18:37','qxjn'),(111,'f','1981-05-26',NULL,'2003-11-27 23:43:24','mnmb'),(112,'f','2010-08-05',NULL,'1992-11-03 07:14:36','gopj'),(115,'m','1996-03-04',NULL,'1995-03-15 04:47:16','xjos'),(116,'f','2013-03-24',NULL,'1972-10-21 02:13:58','hwzd'),(117,'f','1970-12-25',NULL,'2008-03-10 21:18:36','jkpj'),(118,'m','1971-02-15',NULL,'2005-12-19 15:21:49','cknp'),(120,'f','1991-11-20',NULL,'2007-09-17 02:31:54','tqwt'),(122,'f','1993-04-28',NULL,'2009-08-24 16:52:03','kuga'),(126,'f','1970-03-28',NULL,'1988-09-20 05:40:16','thip'),(129,'m','1984-11-06',NULL,'1986-08-19 02:09:12','rquj'),(130,'f','2015-06-19',NULL,'2003-07-02 12:54:29','uwhz'),(131,'f','1977-06-22',NULL,'1999-02-18 15:11:24','xnqu'),(132,'f','1995-01-20',NULL,'2009-02-23 08:46:35','mdut'),(134,'m','1992-10-04',NULL,'1973-02-15 09:24:40','mllg'),(138,'f','1981-09-30',NULL,'1992-09-04 11:10:09','mmgh'),(141,'m','1978-05-19',NULL,'2012-04-25 10:15:39','knge'),(142,'f','2006-08-04',NULL,'1976-02-11 20:14:02','btto'),(145,'m','1977-10-29',NULL,'2018-07-13 18:41:55','xyub'),(146,'f','2006-04-06',NULL,'1986-07-18 23:54:27','duym'),(148,'f','1993-05-05',NULL,'1995-05-18 13:32:06','xpnt'),(149,'m','2020-05-09',NULL,'1988-05-25 05:46:30','oqjx'),(151,'f','1984-05-25',NULL,'1981-08-13 05:00:33','wzmj'),(152,'m','2004-03-03',NULL,'1984-10-14 04:00:05','vkzs'),(153,'f','2002-07-13',NULL,'1975-04-07 20:46:39','gklz'),(154,'f','2021-09-30',NULL,'1979-01-30 10:11:12','kzly'),(155,'m','2017-01-01',NULL,'2019-07-16 00:04:53','vgbt'),(156,'f','2012-05-03',NULL,'2008-03-25 03:18:58','klfs'),(157,'m','2004-08-18',NULL,'2009-12-26 08:52:34','fwst'),(160,'f','1989-09-25',NULL,'1993-10-28 12:15:05','rnry'),(162,'m','2020-08-02',NULL,'1987-07-15 15:46:47','bfgn'),(163,'f','2020-06-08',NULL,'1998-11-21 00:29:12','vbpg'),(164,'f','2007-07-29',NULL,'2011-12-13 17:58:56','uryr'),(166,'m','1989-04-21',NULL,'1978-11-07 12:46:35','vhml'),(167,'m','2012-09-03',NULL,'2004-08-04 06:05:20','wgke'),(168,'m','2020-06-05',NULL,'1984-05-20 22:46:57','sxyy'),(171,'f','2001-06-07',NULL,'2020-09-29 06:29:01','qgxk'),(172,'f','1973-03-01',NULL,'2010-08-01 12:36:40','azum'),(173,'m','1997-09-19',NULL,'1995-10-09 03:10:35','gesd'),(175,'f','2007-04-19',NULL,'2021-09-08 00:50:41','cpph'),(176,'m','1979-07-06',NULL,'2002-06-08 19:47:44','tnot'),(178,'m','1973-11-09',NULL,'1979-09-27 07:47:55','jvka'),(180,'m','2015-06-26',NULL,'1987-12-09 16:21:00','ohbb'),(181,'m','1982-01-04',NULL,'2003-07-28 23:57:09','adsr'),(182,'f','1999-12-28',NULL,'1983-07-11 11:00:07','hpmy'),(183,'f','2006-12-21',NULL,'2009-11-26 07:16:27','hfbq'),(185,'m','1987-06-19',NULL,'2000-01-25 14:15:08','yowa'),(192,'m','2019-04-25',NULL,'1980-05-20 21:33:49','fylr'),(193,'f','1971-02-25',NULL,'1995-09-14 21:09:13','txct'),(195,'m','2008-11-15',NULL,'1991-09-05 01:36:42','vjjy'),(199,'m','2002-05-02',NULL,'2015-10-06 14:19:10','dxaw'),(200,'f','1973-02-11',NULL,'1981-12-24 02:36:31','ylho');
/*!40000 ALTER TABLE `profiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-30  9:26:01

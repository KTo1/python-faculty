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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lastname` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Фамиль',
  `email` varchar(120) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password_hash` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  KEY `users_firstname_lastname_idx` (`firstname`,`lastname`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='юзеры';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (101,'Estell','Williamson','darren37@example.com','e4176953a07d102c4e3eac3f31abb41863766596',0),(102,'Eugene','Oberbrunner','cartwright.phoebe@example.net','69c2b90911ccd524dc4e85c7253125c3103a8375',843),(103,'Aniya','Mosciski','else.white@example.org','e85a24ac22ab5e31966af68cce797ca5511cfdef',1),(105,'Taryn','Dicki','stamm.christa@example.net','31d143c9bc7fe1b5738fcd7d647ea5605542a16f',81),(109,'Estefania','O\'Reilly','o\'conner.camille@example.com','62739778e6f06868c04893804411ee80b046fcae',54),(111,'Delta','McClure','pierce.jacobs@example.org','becad601767ed2f9e6dc3f205daad5382140c875',995161),(112,'Bertha','Bahringer','reed.kohler@example.com','890d716ef7ab193cc7bac78d4eee942d7eb90d42',169),(115,'April','Heller','djohns@example.com','7ace06b8ed803596019ac9923af0fd98ad16944d',31),(116,'Myrl','Johnson','qwilderman@example.net','750e106733cd5337df624a5c34a5975be1d4a86b',200),(117,'Johnathon','Reilly','athena.daniel@example.net','00a715dcd77a7a307f2f5e36154be93697400882',724262),(118,'Alvena','Fisher','sydni99@example.com','0022d9df1671397579feef45f754947bf0841111',803778),(120,'Sonia','Bailey','pjenkins@example.org','acf6a7d54d40a8ac9c1a06cc9deef6bda9cbdeae',1691776802),(122,'Lemuel','Beahan','fritsch.alexander@example.org','51674f82dae12d7f281c9c92620a3b534963a9da',2040083687),(126,'Gilberto','Veum','abbie.stoltenberg@example.com','f51bfec2ed2bbb26cd892900cc880c12dc277616',825),(129,'Theresia','Lindgren','marvin.dameon@example.net','f0c8879331b05702595a1c1ef1fe668582dd4da5',861),(130,'Freddy','Kuvalis','mborer@example.org','a8e9f3e1b8b837f0eaa11ef4448398bfb9f44348',622385),(131,'Florine','Kiehn','oswaldo.lind@example.net','877408b9cd8d02d66f9156e887c61a8c78f39ebb',1406604328),(132,'Audreanne','Heidenreich','miller.stracke@example.net','d7f81141de4bb5ec5dcd5c6483c5b0dc6daff7a4',77),(134,'Kaleigh','Krajcik','anabel.bernhard@example.org','ba66e7d6cd3c74842c4f20b551245a89bccfd2e6',970415),(138,'Angie','Thompson','matilde32@example.com','ed73448d0f71bb9f43d7d5f1c49c57a3cb0b1eb7',68),(141,'Hayley','Gleichner','bashirian.ethyl@example.net','775390331e9c4a52293551c4b74ef9d6022c7da5',15),(142,'Bobby','Gleichner','rutherford.janae@example.org','e28be9b1cd3975c1fa99cf238616b70d55a1c3de',38),(145,'Mozelle','Schaden','neal.treutel@example.net','b256db6ec8d4c341523abb137502aea68f63d06d',28),(146,'Candido','Quitzon','addie.hettinger@example.net','60148afec62f60815a34f14ee405512330c93d32',421940),(148,'Giovanny','Rau','hoeger.josie@example.net','ae3f5086daa3551689c51965338756c2b56223f5',447),(149,'Freddy','Schaden','virginia.veum@example.org','e0c7f1c16900d3aabc93539c49521325d108d68f',211812),(151,'Rosalia','Rolfson','elna37@example.org','b025922abf5e008ba729a9085711042216006f95',843356),(152,'Modesto','Altenwerth','swift.nickolas@example.com','4c865b3f2e5b49d902172b3b480ba10eb51e7a6d',5596824390),(153,'Kaylin','Nienow','iwiegand@example.org','82457752b583bd3e278723939f3cc44e763f024e',972525),(154,'Charity','Schroeder','qgerhold@example.com','d58d50d5a06db4f3d94ebfbd9434d47eb60dcd0b',805),(155,'Gaetano','Bechtelar','mayer.iva@example.org','18687ceb77dcfa301d5fd8c3b474f5f0885ba097',659747),(156,'Seth','O\'Keefe','gus89@example.net','95630395929a02f7acd16725b51d088bb7f6fdca',402555),(157,'Lucious','Stehr','bschultz@example.net','dfd3334e12516e511278f2404ed9253edd27bea0',530),(160,'Miller','Graham','eloy.vandervort@example.net','d788b12d5bf7fab12a90f349310f399245b8743c',414),(162,'Jana','Turcotte','dillan.rau@example.net','a767f81db83ed69a53d2ccda774cbeea5fa07580',383975633),(163,'Darrell','Ledner','caden43@example.org','7846fbf0b617db9153a95b18a874bd7875a6382f',836662),(164,'Odie','Dooley','vswift@example.net','92a28b20687d950b3f3f1438aca18aa1d151f668',890338),(166,'Harrison','O\'Hara','leuschke.demond@example.org','c8e8bf845c4ba70c618f9c346b41372c2cbd1562',801753),(167,'Coralie','Walsh','katherine87@example.org','44bf7b91dcf81c98ca58ebec785df0fdcc810028',566),(168,'Lazaro','Bechtelar','beer.nannie@example.org','3128d474545f238b212a8836deb228b75ccb79f8',670),(171,'Marilou','Hettinger','deion55@example.com','28111d58a4531274174b1ae941b4baaa8dcbf1a8',381977),(172,'Alejandra','Turner','carmstrong@example.org','97bf0641283b4ab8aa8d3122f46361bb9a9ff693',8542617546),(173,'Alena','Upton','fstreich@example.net','6d3f94304db390ddaa796f9eb1b4d26178a276d6',810),(175,'Gregg','Hamill','nola01@example.com','76482eae8d488140673e1c4057ec8bba334d4c2a',375960),(176,'Alayna','Kreiger','tamara53@example.net','e8acf4c40d62ff4b2ee9b96c501803827a372010',8),(178,'Paula','Fadel','bridie.hessel@example.org','425768cfd6266e1ab4b5d3d8779b44e28c24a577',517676),(180,'Jordi','Murray','emil62@example.org','ccec60e8b49ce0b8fc671dd41ac36907ef3a9ea9',98),(181,'Franco','Treutel','myost@example.net','e4e156252230f37c4281d3cae094c2eca45932f7',846),(182,'Michaela','Zboncak','esta08@example.org','05e4fba5529b8afbd73a1df3a2cff5006628cf75',478),(183,'Liam','Considine','wmante@example.net','35fa42c4c93c97a902a634563e9f746a20fbaeb5',61),(185,'Name','Lowe','maggio.ena@example.net','4d57484996ce79feb4ec0846226ae1bc9761abf7',84),(192,'Providenci','Borer','sthompson@example.net','689d387582e0e991cb8e06d4feb6dd1562e1e84b',210480),(193,'Braden','Hermann','goldner.kamren@example.com','e328ca44a04ff1f46048506a431b10e0ecf91248',219),(195,'Emerson','Boehm','sspinka@example.org','c38e3f00b9a7525e5f1908d05cb72095c5d914d1',609),(199,'Tyree','Fisher','lebsack.arely@example.org','047f0a5704b6ae4c6c002b7956153e404a5c149d',514019),(200,'Stuart','Hirthe','georgette35@example.org','b3564dc7d8985ae27f434d214fa9ed739177c13a',614899);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-30  9:24:37

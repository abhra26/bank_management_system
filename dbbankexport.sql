-- MySQL dump 10.13  Distrib 8.0.19, for macos10.15 (x86_64)
--
-- Host: localhost    Database: bank
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `acntcard`
--

DROP TABLE IF EXISTS `acntcard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acntcard` (
  `accntid` bigint NOT NULL,
  `cardno` bigint NOT NULL,
  `type` text NOT NULL,
  PRIMARY KEY (`cardno`),
  KEY `accntid` (`accntid`),
  CONSTRAINT `acntcard_ibfk_1` FOREIGN KEY (`accntid`) REFERENCES `users` (`accntid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acntcard`
--

LOCK TABLES `acntcard` WRITE;
/*!40000 ALTER TABLE `acntcard` DISABLE KEYS */;
INSERT INTO `acntcard` VALUES (9,4093891182298,'Credit'),(9,4657198935176,'Credit'),(18,4182386271031556,'Debit'),(2,4721655349055032,'credit'),(14,5125183578809397,'Debit'),(19,5210376816895949,'Debit'),(1,5412088017153251,'debit');
/*!40000 ALTER TABLE `acntcard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `acnttype`
--

DROP TABLE IF EXISTS `acnttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acnttype` (
  `accntid` bigint NOT NULL,
  `type` text NOT NULL,
  KEY `accntno` (`accntid`),
  CONSTRAINT `acnttype_ibfk_1` FOREIGN KEY (`accntid`) REFERENCES `users` (`accntid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acnttype`
--

LOCK TABLES `acnttype` WRITE;
/*!40000 ALTER TABLE `acnttype` DISABLE KEYS */;
INSERT INTO `acnttype` VALUES (1,'debit'),(2,'credit'),(8,'Credit'),(9,'Savings'),(11,'Debit'),(14,'Savings'),(15,'Debit'),(16,'Savings'),(17,'Debit'),(18,'Credit'),(19,'Credit');
/*!40000 ALTER TABLE `acnttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `adminid` text NOT NULL,
  `adminpass` int NOT NULL,
  `name` text NOT NULL,
  `phone` bigint NOT NULL,
  `email` text NOT NULL,
  `aadhar` bigint NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `card_applications`
--

DROP TABLE IF EXISTS `card_applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `card_applications` (
  `custid` text NOT NULL,
  `accntid` bigint NOT NULL,
  `name` text NOT NULL,
  `dob` text NOT NULL,
  `phone` bigint NOT NULL,
  `aadhar` bigint NOT NULL,
  `income` bigint NOT NULL,
  `card_type` text NOT NULL,
  `card_company` text NOT NULL,
  `occupation` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `card_applications`
--

LOCK TABLES `card_applications` WRITE;
/*!40000 ALTER TABLE `card_applications` DISABLE KEYS */;
INSERT INTO `card_applications` VALUES ('cstmr1',9,'Shruti Saha','2002-10-29',9836276787,234543234,6000000,'CREDIT','VISA','software engineer');
/*!40000 ALTER TABLE `card_applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cardlog`
--

DROP TABLE IF EXISTS `cardlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardlog` (
  `cardno` bigint NOT NULL,
  `cvv` int NOT NULL,
  `status` text NOT NULL,
  `expirydate` text NOT NULL,
  `company` text NOT NULL,
  `balance` bigint DEFAULT NULL,
  `cardlimit` bigint NOT NULL,
  `pin` int NOT NULL,
  KEY `cardno` (`cardno`),
  CONSTRAINT `cardlog_ibfk_1` FOREIGN KEY (`cardno`) REFERENCES `acntcard` (`cardno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardlog`
--

LOCK TABLES `cardlog` WRITE;
/*!40000 ALTER TABLE `cardlog` DISABLE KEYS */;
INSERT INTO `cardlog` VALUES (4721655349055032,567,'blocked','12-09-2030','visa',1000017200,200000,0),(5412088017153251,890,'open','13-10-2030','mastercard',1100150400,200000,0),(4093891182298,631,'open','2045-3','visa',200000,200000,0),(4657198935176,308,'open','2043-8','visa',149500,200000,0),(4182386271031556,607,'open','2024-11','visa',199500,200000,0),(5125183578809397,269,'open','2023-11','mastercard',200000,200000,3327),(5210376816895949,190,'open','2032-6','mastercard',200000,200000,7879);
/*!40000 ALTER TABLE `cardlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creditacnts`
--

DROP TABLE IF EXISTS `creditacnts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creditacnts` (
  `custid` text NOT NULL,
  `accntid` bigint NOT NULL,
  `business` text,
  `granin` bigint NOT NULL,
  `profit` bigint DEFAULT NULL,
  `ssn` int NOT NULL,
  `turnover` bigint DEFAULT NULL,
  `debt` bigint NOT NULL,
  `timelimit` text,
  KEY `accntid` (`accntid`),
  CONSTRAINT `creditacnts_ibfk_1` FOREIGN KEY (`accntid`) REFERENCES `users` (`accntid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creditacnts`
--

LOCK TABLES `creditacnts` WRITE;
/*!40000 ALTER TABLE `creditacnts` DISABLE KEYS */;
INSERT INTO `creditacnts` VALUES ('cstmr2',2,'rainet_abhra.co kolkata,west bengal',500000,0,123,0,0,'NA'),('cstmr7',7,'patanjali, kolkata, west bengal',500000000,100000,234,500100000,0,'NA'),('cstmr8',8,'jaishree bicycles PVT. LTD. , Kolkata, West Bengal',700000,500000,456,1200000,0,'NA'),('cstmr14',18,'lokhnath paper house, Kolkata, West Bengal',6000000,200000,567,6200000,0,'NA'),('cstmr15',19,'abhraneelsaha.pvt.ltd Kolkata West Bengal',500000,100000,0,600000,0,'NA');
/*!40000 ALTER TABLE `creditacnts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request` (
  `custid` text NOT NULL,
  `request` text NOT NULL,
  `req_type` text NOT NULL,
  `reqid` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
INSERT INTO `request` VALUES ('cstmr2','Application submitted for CREDIT card,for spouse too, on account(id):2,card company:VISA.','card_application','req402.2020-10-15.15:36:24.269784.cstmr2.0'),('cstmr14','Application submitted for DEBIT card on account(id):18,card company:VISA','card_application','req266.2020-10-16.14:04:42.321470.cstmr14.18'),('cstmr15','Application submitted for DEBIT card on account(id):19,card company:VISA','card_application','req137.2020-10-22.00:43:53.201377.cstmr15.19');
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_stat_log`
--

DROP TABLE IF EXISTS `service_stat_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_stat_log` (
  `reqid` text NOT NULL,
  `custid` text NOT NULL,
  `accntid` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_stat_log`
--

LOCK TABLES `service_stat_log` WRITE;
/*!40000 ALTER TABLE `service_stat_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `service_stat_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spouse_credit_cards`
--

DROP TABLE IF EXISTS `spouse_credit_cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spouse_credit_cards` (
  `cardno` bigint NOT NULL,
  `name` text NOT NULL,
  `dob` text NOT NULL,
  `aadhar` bigint NOT NULL,
  `occupation` text NOT NULL,
  `income` bigint NOT NULL,
  `custid` text NOT NULL,
  KEY `cardno` (`cardno`),
  CONSTRAINT `spouse_credit_cards_ibfk_1` FOREIGN KEY (`cardno`) REFERENCES `cardlog` (`cardno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spouse_credit_cards`
--

LOCK TABLES `spouse_credit_cards` WRITE;
/*!40000 ALTER TABLE `spouse_credit_cards` DISABLE KEYS */;
INSERT INTO `spouse_credit_cards` VALUES (4657198935176,'Shruti Saha','2002-10-29',234543234,'software engineer',6000000,'cstmr1');
/*!40000 ALTER TABLE `spouse_credit_cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactionlog`
--

DROP TABLE IF EXISTS `transactionlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactionlog` (
  `tid` text NOT NULL,
  `utid` int NOT NULL,
  `date` text NOT NULL,
  `time` text NOT NULL,
  `description` text NOT NULL,
  `cardno` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactionlog`
--

LOCK TABLES `transactionlog` WRITE;
/*!40000 ALTER TABLE `transactionlog` DISABLE KEYS */;
INSERT INTO `transactionlog` VALUES ('txn832.2020-10-09.01:41:36.351276.251',816,'2020-10-09','01:41:36.351276','2000 deposited',5412088017153251),('req140.2020-10-09.01:43:14.114460.cstmr1.0',140,'2020-10-09','01:43:14.112819','customer id cstmr1 blocked due to security reasons',0),('req963.2020-10-10.15:18:46.785261.cstmr1.0',963,'2020-10-10','15:18:46.783289','customer id cstmr1 blocked due to security reasons',0),('req740.2020-10-10.15:20:18.303096.cstmr2.0',740,'2020-10-10','15:20:18.301180','customer id cstmr2 blocked due to security reasons',0),('req834.2020-10-10.15:20:51.469705.cstmr1.18',834,'2020-10-10','15:20:51.467828','Account id 18 blocked for security reasons',0),('req238.2020-10-10.15:24:34.637619.cstmr2.0',238,'2020-10-10','15:24:34.636108','customer id cstmr2 opened',0),('req756.2020-10-10.15:24:44.111963.cstmr1.18',756,'2020-10-10','15:24:44.110280','Account id 18 opened',0),('req121.2020-10-10.15:53:28.507665.cstmr1.18',121,'2020-10-10','15:53:28.506314','account id: 18 deleted',0),('req792.2020-10-10.15:56:13.067528.cstmr1.18',792,'2020-10-10','15:56:13.066118','account id: 18 deleted',0),('req919.2020-10-10.15:59:33.236056.cstmr1.18',919,'2020-10-10','15:59:33.234565','account id: 18 deleted',0),('req728.2020-10-10.16:00:01.344427.cstmr10.12',728,'2020-10-10','16:00:01.342910','account id: 12 deleted',0),('req950.2020-10-10.16:00:01.353703.cstmr10.13',950,'2020-10-10','16:00:01.352323','account id: 13 deleted',0),('req331.2020-10-10.16:00:01.356027.cstmr10.0',331,'2020-10-10','16:00:01.354583','customer:cstmr10 deleted',0),('req449.2020-10-11.01:06:25.470482.cstmr4.0',449,'2020-10-11','01:06:25.469059','email of cstmr4 has been updated to abhraneel2003@gmail.com',0),('req670.2020-10-11.01:08:30.544113.cstmr4.0',670,'2020-10-11','01:08:30.542769','email of cstmr4 has been updated to abhraneel2003@gmail.com',0),('req879.2020-10-11.01:13:04.877911.cstmr2.0',879,'2020-10-11','01:13:04.876068','business of cstmr2 has been updated to rainet_abhra.co kolkata,west bengal',0),('req603.2020-10-11.09:23:39.459583.cstmr1.0',603,'2020-10-11','09:23:39.458217','aadhar of cstmr1 has been updated to 12345432',0),('req574.2020-10-11.09:28:17.975042.cstmr1.1',574,'2020-10-11','09:28:17.973575','aadhar of 1(cstmr1) has been updated to 345678',0),('req190.2020-10-11.23:44:52.793326.cstmr1.0',190,'2020-10-11','23:44:52.789861','request req944.2020-10-11.23:34:31.969630.cstmr1.0 completed',0),('txn379.2020-10-12.09:08:44.369852.251',839,'2020-10-12','09:08:44.369852','20000 withdrawn',5412088017153251),('req443.2020-10-15.15:27:48.169942.cstmr1.0',443,'2020-10-15','15:27:48.168518','request req790.2020-10-15.15:26:15.198063.cstmr1.0 completed',0),('txn363.2020-10-16.13:24:48.375922.176',922,'2020-10-16','13:24:48.375922','50000 withdrawn',4657198935176),('txn539.2020-10-16.13:31:25.435051.176',163,'2020-10-16','13:31:25.435051','500 withdrawn',4657198935176),('txn228.2020-10-16.14:11:57.957873.556',481,'2020-10-16','14:11:57.957873','500 withdrawn',4182386271031556),('req108.2020-10-17.21:39:32.813368.cstmr1.0',108,'2020-10-17','21:39:32.810540','Card assigned to customer id: cstmr1,account: 0',0),('req813.2020-10-17.21:40:05.573529.cstmr1.14',813,'2020-10-17','21:40:05.571394','Card assigned to customer id: cstmr1,account: 14',0),('req486.2020-10-19.10:07:27.021379.cstmr1.14',486,'2020-10-19','10:07:27.018185','Card assigned to customer id: cstmr1,account: 14',0),('txn983.2020-10-22.00:54:16.785771.786',817,'2020-10-22','00:54:16.785771','5000 withdrawn',4184507504719786),('req141.2020-10-22.00:56:14.185923.cstmr15.19',141,'2020-10-22','00:56:14.184620','Account id 19 blocked for security reasons',0),('req466.2020-10-22.15:22:12.795268.cstmr15.19',466,'2020-10-22','15:22:12.792537','cardno: 4184507504719786 deleted',4184507504719786),('req336.2020-10-22.15:22:12.803274.cstmr15.19',336,'2020-10-22','15:22:12.801635','account id: 19 deleted',0),('req233.2020-10-22.15:59:18.551335.cstmr15.19',233,'2020-10-22','15:59:18.549957','Card assigned to customer id: cstmr15,account: 19',0),('req849.2020-10-22.16:17:58.898364.cstmr15.0',849,'2020-10-22','16:17:58.896891','request req615.2020-10-22.16:13:54.473485.cstmr15.0 completed',0),('req581.2020-10-22.16:19:29.748246.cstmr15.19',581,'2020-10-22','16:19:29.746834','Account id 19 blocked for security reasons',0),('req855.2020-10-22.16:22:34.145616.cstmr15.19',855,'2020-10-22','16:22:34.144418','Account id 19 opened',0),('req318.2020-10-22.16:23:03.096124.cstmr15.19',318,'2020-10-22','16:23:03.094476','Account id 19 opened',0),('req177.2020-10-22.16:37:57.139224.cstmr15.19',177,'2020-10-22','16:37:57.137482','email of 19(cstmr15) has been updated to abhraneel2003@gmail.com',0);
/*!40000 ALTER TABLE `transactionlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `custid` varchar(100) NOT NULL,
  `accntid` bigint NOT NULL,
  `passwd` int NOT NULL,
  `email` text NOT NULL,
  `mobile` bigint NOT NULL,
  `city` text NOT NULL,
  `state` text NOT NULL,
  `zipcode` bigint NOT NULL,
  `aadhar` bigint NOT NULL,
  `gender` varchar(1) NOT NULL,
  `name` text NOT NULL,
  `address` text NOT NULL,
  `dob` text NOT NULL,
  `status` varchar(30) NOT NULL DEFAULT 'open',
  PRIMARY KEY (`accntid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('cstmr1',1,1234,'abhraneel2003@gmail.com',1234567890,'kolkata','west bengal',700032,345678,'M','Abhraneel Saha','fgh street','26-09-2003','open'),('cstmr2',2,1234,'binodkumar@gmail.com',2345665432,'kolkata','west bengal',700045,23456,'M','Binod kumar','bvb street','23-08-2002','open'),('cstmr3',3,2345,'abhraneel2003@gmail.com',5678998765,'Kolkata','West Bengal',123456,23456,'M','Arijeet Pramanik','acropolis mall','2002-06-16','open'),('cstmr4',4,5678,'abhraneel2003@gmail.com',7890098765,'Jaipur','Rajasthan',23456,456789,'M','Rahul Singh','F-405,Kalpbuild,kalpananagar','1995-09-25','open'),('cstmr5',5,7890,'niranjan_saha@hotmail.com',9836276787,'Kolkata','West Bengal',700032,345678,'M','Niranjan Saha','F-302 Webstar Sapphire, 1-Kalibari Lane','1971-08-07','open'),('cstmr6',6,1234,'abcxyz@gmail.com',1234554321,'kolkata','west bengal',700032,345678,'F','XYZ ABC','dfg street','2003-09-16','open'),('cstmr7',7,1234,'babaram@gmail.com',4567887654,'kolkata','west bengal',700032,234567,'M','Baba Ramdev','abcv street','1990-08-12','open'),('cstmr8',8,4495,'ssengupta19750309@hotmail.com',7895678458,'Kolkata','West Bengal',700032,234565768756,'F','Shreya Sengupta','1-Kalibari Lane','1975-03-09','open'),('cstmr1',9,1234,'abhraneel2003@gmail.com',9836276787,'Kolkata','West Bengal',700032,12345432,'M','Abhraneel Saha','F-302, Webstar Sapphire, 1-Kalibari Lane','2003-09-26','open'),('cstmr9',11,4495,'HB19800714@gmail.com',4567899876,'Pune','Maharashtra',500042,70023,'O','Hrichik Bhuniya','hdgvue lane ','1980-07-14','open'),('cstmr1',14,1234,'abhraneel2003@gmail.com',4567887654,'kolkata','west bengal',700069,12345432,'O','Balgopal Maharana','vbh street','2003-07-04','open'),('cstmr11',15,3456,'abhraneel2003@gmail.com',56789876,'buvgfyc','gvhgv',12345,1234565432,'M','ali abdal','jhbjhbjh','1980-09-16','open'),('cstmr12',16,1345,'abhraneel2003@gmail.com',5678987,'hfcgfvch','jknkjn',54654,87675,'M','Taimur abdal','jbvhgvh','1990-09-18','open'),('cstmr13',17,0,'abhraneel2003@gmail.com',567890987987,'jefjfv','jdbvjf',700083,2343234334,'M','Rohan Kumar','jfnjhdf','1997-12-09','open'),('cstmr14',18,6789,'abhraneel2003@gmail.com',5678909876,'kolkata','west bengal',700045,45678987,'M','vedant Lal','camac street','2003-07-16','open'),('cstmr15',19,4495,'abhraneel2003@gmail.com',9836276787,'Kolkata','West Bengal',700032,234554345,'M','Abhraneel Saha','F-302 Webstar Sapphire','2003-09-26','open');
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

-- Dump completed on 2020-10-22 17:43:04

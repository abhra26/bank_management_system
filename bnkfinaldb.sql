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
-- Table structure for table `service_stat_log`
--

DROP TABLE IF EXISTS `service_stat_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_stat_log` (
  `reqid` text NOT NULL,
  `custid` text NOT NULL,
  `accntid` bigint DEFAULT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-22 15:18:45

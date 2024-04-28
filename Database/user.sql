-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: face_recognition
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `S_id` int NOT NULL AUTO_INCREMENT,
  `Branch` varchar(255) DEFAULT NULL,
  `batch` varchar(255) DEFAULT NULL,
  `Year` varchar(255) DEFAULT NULL,
  `Semester` varchar(255) DEFAULT NULL,
  `Regd_no` varchar(255) NOT NULL,
  `Roll_no` varchar(255) NOT NULL,
  `s_Name` varchar(255) NOT NULL,
  `Gender` varchar(255) DEFAULT NULL,
  `DOB` varchar(255) DEFAULT NULL,
  `City` varchar(255) DEFAULT NULL,
  `Phone_no` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `Photo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`S_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (3,'MCA','41','2nd','4th','45','45','Rakesh','M','11/10/2001','Puri','7735614966','rakesh@gmail.com','Yes'),(4,'MCA','41','2nd','4th','2205105008','414008','Bhagyashree Panda','F','02/08/2002','Cuttack','9348181894','bhagyashree@gmail.com','Yes'),(5,'MCA','41','2nd','4th','2205105072','404172','Suryapratap Behura','M','04/03/2001','jajpur','9969699969','sberuu@gmail.com','Yes'),(6,'MCA','41','2nd','4th','2205105047','414047','Rinky Sahu','F','02/09/2000','Keonjhar','1234567890','rinky@gmail.com','Yes'),(7,'MCA','41','2nd','4th','2205105075','414075','Tanimarani Behera','F','16\\03\\2002','kendrapara','8917439713','denyyd9@gmail.com','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(45) NOT NULL,
  `user_email` varchar(45) NOT NULL,
  `securityQ` varchar(45) NOT NULL,
  `securityA` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `c_password` varchar(45) NOT NULL,
  PRIMARY KEY (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Rakesh Kumar Sarangi','rakesh@gmail.com','What is Your birth date','11','rakesh1','123');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-16 18:26:16

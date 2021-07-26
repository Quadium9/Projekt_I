-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Wersja serwera:               10.6.3-MariaDB - mariadb.org binary distribution
-- Serwer OS:                    Win64
-- HeidiSQL Wersja:              11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Zrzut struktury bazy danych starsdb
CREATE DATABASE IF NOT EXISTS `starsdb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `starsdb`;

-- Zrzut struktury tabela starsdb.constellations
CREATE TABLE IF NOT EXISTS `constellations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT '',
  `declination` varchar(100) NOT NULL DEFAULT '',
  `symbolism` text NOT NULL,
  `sky_side` varchar(50) NOT NULL DEFAULT '',
  `area` float NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.constellations: ~0 rows (około)
DELETE FROM `constellations`;
/*!40000 ALTER TABLE `constellations` DISABLE KEYS */;
/*!40000 ALTER TABLE `constellations` ENABLE KEYS */;

-- Zrzut struktury tabela starsdb.drawing_constellation
CREATE TABLE IF NOT EXISTS `drawing_constellation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `connected_star` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.drawing_constellation: ~0 rows (około)
DELETE FROM `drawing_constellation`;
/*!40000 ALTER TABLE `drawing_constellation` DISABLE KEYS */;
/*!40000 ALTER TABLE `drawing_constellation` ENABLE KEYS */;

-- Zrzut struktury tabela starsdb.planet
CREATE TABLE IF NOT EXISTS `planet` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT '',
  `id_star` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`Id`),
  KEY `SK` (`id_star`),
  CONSTRAINT `SK` FOREIGN KEY (`id_star`) REFERENCES `stars` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.planet: ~0 rows (około)
DELETE FROM `planet`;
/*!40000 ALTER TABLE `planet` DISABLE KEYS */;
/*!40000 ALTER TABLE `planet` ENABLE KEYS */;

-- Zrzut struktury tabela starsdb.stars
CREATE TABLE IF NOT EXISTS `stars` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `rectascension` varchar(20) NOT NULL,
  `declination` varchar(20) NOT NULL,
  `radial_speed` varchar(20) DEFAULT NULL,
  `distance` varchar(20) DEFAULT NULL,
  `brightness` varchar(20) DEFAULT NULL,
  `star_type` varchar(50) DEFAULT NULL,
  `mass` varchar(20) DEFAULT NULL,
  `greek_symbols` varchar(1) DEFAULT NULL,
  `drawing_star` int(11) DEFAULT NULL,
  `constellation_id` int(11) NOT NULL,
  `discaverer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `DSK` (`drawing_star`),
  KEY `DK` (`discaverer_id`),
  KEY `CK` (`constellation_id`) USING BTREE,
  CONSTRAINT `CK` FOREIGN KEY (`constellation_id`) REFERENCES `constellations` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `DK` FOREIGN KEY (`discaverer_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `DSK` FOREIGN KEY (`drawing_star`) REFERENCES `drawing_constellation` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.stars: ~0 rows (około)
DELETE FROM `stars`;
/*!40000 ALTER TABLE `stars` DISABLE KEYS */;
/*!40000 ALTER TABLE `stars` ENABLE KEYS */;

-- Zrzut struktury tabela starsdb.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `surname` varchar(100) NOT NULL,
  `login` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.user: ~0 rows (około)
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `name`, `surname`, `login`, `password`, `email`) VALUES
	(1, 'admin', 'admin', 'admin', 'admin', 'admin');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;useruseruser
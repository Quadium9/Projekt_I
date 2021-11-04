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
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.constellations: ~1 rows (około)
DELETE FROM `constellations`;
/*!40000 ALTER TABLE `constellations` DISABLE KEYS */;
INSERT INTO `constellations` (`id`, `name`, `declination`, `symbolism`, `sky_side`, `area`) VALUES
	(21, 'test', '-10:20:30.0', 'test', 'CardinalDirection.North', 123.4),
	(23, 'test2', '-10:20:30.0', 'test', 'north', 123.4);
/*!40000 ALTER TABLE `constellations` ENABLE KEYS */;

-- Zrzut struktury tabela starsdb.drawing_constellation
CREATE TABLE IF NOT EXISTS `drawing_constellation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `star_name_in` int(11) NOT NULL DEFAULT 0,
  `star_name_out` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `in` (`star_name_in`),
  CONSTRAINT `in` FOREIGN KEY (`star_name_in`) REFERENCES `stars` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.drawing_constellation: ~1 rows (około)
DELETE FROM `drawing_constellation`;
/*!40000 ALTER TABLE `drawing_constellation` DISABLE KEYS */;
INSERT INTO `drawing_constellation` (`id`, `star_name_in`, `star_name_out`) VALUES
	(21, 17, 19);
/*!40000 ALTER TABLE `drawing_constellation` ENABLE KEYS */;

-- Zrzut struktury tabela starsdb.planet
CREATE TABLE IF NOT EXISTS `planet` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT '',
  `id_star` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `name` (`name`),
  KEY `SK` (`id_star`),
  CONSTRAINT `SK` FOREIGN KEY (`id_star`) REFERENCES `stars` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.planet: ~1 rows (około)
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
  `constellation_id` int(11) NOT NULL,
  `discaverer_id` int(11) DEFAULT NULL,
  `confirmed` varchar(3) NOT NULL DEFAULT 'NO',
  PRIMARY KEY (`Id`),
  KEY `DK` (`discaverer_id`),
  KEY `CK` (`constellation_id`) USING BTREE,
  CONSTRAINT `CK` FOREIGN KEY (`constellation_id`) REFERENCES `constellations` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `DK` FOREIGN KEY (`discaverer_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.stars: ~6 rows (około)
DELETE FROM `stars`;
/*!40000 ALTER TABLE `stars` DISABLE KEYS */;
INSERT INTO `stars` (`Id`, `name`, `rectascension`, `declination`, `radial_speed`, `distance`, `brightness`, `star_type`, `mass`, `greek_symbols`, `constellation_id`, `discaverer_id`, `confirmed`) VALUES
	(17, 'test', '10:20:30.1', '10:20:30.1', '10', '100', '1000', 'Brown dwarf', '10000', 'Ω', 21, 62, 'NO'),
	(19, 'testowy', '10:22:30.1', '10:22:30.1', '10', '100', '1000', 'Brown dwarf', '100001', 'Ω', 21, 62, 'YES'),
	(20, '2', '2h 2m 2s', '2h 2m 2s', '2', '2', '2', 'Unknown', '2', NULL, 23, 62, 'NO'),
	(21, 'Wymagane', '1h 1m 1s', '1h 1m 1s', '3', '3', '3', 'Unknown', '3', NULL, 23, 62, 'NO'),
	(22, 'Wymagane2', '2h 2m 2s', '2h 2m 2s', '', '', '', 'Unknown', '', NULL, 21, 62, 'YES'),
	(23, '4', '4°4′4″', '4h4m4s', '', '', '', 'Unknown', '', NULL, 21, 62, 'NO');
/*!40000 ALTER TABLE `stars` ENABLE KEYS */;

-- Zrzut struktury tabela starsdb.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `surname` varchar(100) NOT NULL,
  `login` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `rules` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `login` (`login`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8mb3;

-- Zrzucanie danych dla tabeli starsdb.user: ~2 rows (około)
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `name`, `surname`, `login`, `password`, `email`, `rules`) VALUES
	(62, 'admin', 'admin', 'admin', 'adminadmin', 'admin@admin.admin', 'admin'),
	(77, 'test', 'test', 'wqe', '12345678', 'test2@test.test', 'user'),
	(79, 'test', 'test', 'wqewqe', 'fweqwewqeq', 'test10@test.test', 'user');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

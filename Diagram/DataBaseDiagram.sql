CREATE TABLE `constellations` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `declination` float,
  `rectascension` float,
  `sky_side` varchar(255),
  `area` float,
  `picture` text
);

CREATE TABLE `stars` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `rectascensionh` tinyint NOT NULL,
  `rectascensionm` tinyint NOT NULL,
  `rectascensions` float NOT NULL,
  `declinationh` tinyint NOT NULL,
  `declinationm` tinyint NOT NULL,
  `declinations` float NOT NULL,
  `radial_speed` float,
  `distance` float,
  `brightness` float,
  `star_type` varchar(255),
  `mass` float,
  `greek_symbols` varchar(255),
  `confirmed` varchar(255) NOT NULL,
  `constellation_id` int NOT NULL,
  `discaverer_id` int
);

CREATE TABLE `user` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `rules` varchar(255) NOT NULL,
  `star_number` int NOT NULL
);

ALTER TABLE `stars` ADD FOREIGN KEY (`constellation_id`) REFERENCES `constellations` (`id`);

ALTER TABLE `stars` ADD FOREIGN KEY (`discaverer_id`) REFERENCES `user` (`id`);

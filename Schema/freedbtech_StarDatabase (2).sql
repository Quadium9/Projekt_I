-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Czas generowania: 19 Maj 2021, 16:35
-- Wersja serwera: 5.7.34-0ubuntu0.18.04.1
-- Wersja PHP: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `freedbtech_StarDatabase`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `constelations`
--

CREATE TABLE `constelations` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `declination` varchar(255) NOT NULL,
  `mainStars` int(11) NOT NULL,
  `symbolism` varchar(1000) NOT NULL,
  `sky_side` int(11) NOT NULL,
  `brightest_star` varchar(255) NOT NULL,
  `area` decimal(60,8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `constelations`
--

INSERT INTO `constelations` (`id`, `name`, `declination`, `mainStars`, `symbolism`, `sky_side`, `brightest_star`, `area`) VALUES
(1, 'Centaurus', '−29.9948788° −64.6957885°', 11, 'While Centaurus now has a high southern latitude, at the dawn of civilization it was an equatorial constellation. Precession has been slowly shifting it southward for millennia, and it is now close to its maximal southern declination.', 1, 'Proxima Centauri\r\n', '1060.00000000');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `planet`
--

CREATE TABLE `planet` (
  `Id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `id_star` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `planet`
--

INSERT INTO `planet` (`Id`, `name`, `id_star`) VALUES
(1, 'b', 1),
(2, 'c', 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `stars`
--

CREATE TABLE `stars` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `rectascension` varchar(255) NOT NULL,
  `declination` varchar(255) NOT NULL,
  `radial_speed` decimal(60,8) NOT NULL,
  `distance` decimal(60,8) NOT NULL,
  `brightness` decimal(60,8) NOT NULL,
  `spectral_type` varchar(255) NOT NULL,
  `mass` decimal(60,8) DEFAULT NULL,
  `star_main` tinyint(1) NOT NULL,
  `constelation_id` int(11) NOT NULL,
  `type` varchar(255) NOT NULL,
  `metallicity` decimal(60,8) NOT NULL,
  `age` decimal(60,2) NOT NULL,
  `link` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `stars`
--

INSERT INTO `stars` (`id`, `name`, `rectascension`, `declination`, `radial_speed`, `distance`, `brightness`, `spectral_type`, `mass`, `star_main`, `constelation_id`, `type`, `metallicity`, `age`, `link`) VALUES
(1, 'Proxima Centauri', '14h 29m 42.94853s', '−62° 40\' 46.1631″', '-22.20400000', '4.24650000', '0.00005000', 'M5.5Ve', '0.12210000', 1, 1, 'Main sequence red dwarf', '0.21000000', '4.85', 'https://en.wikipedia.org/wiki/Proxima_Centauri');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indexes for table `constelations`
--
ALTER TABLE `constelations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `planet`
--
ALTER TABLE `planet`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `id_star` (`id_star`);

--
-- Indexes for table `stars`
--
ALTER TABLE `stars`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `constelations`
--
ALTER TABLE `constelations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT dla tabeli `planet`
--
ALTER TABLE `planet`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT dla tabeli `stars`
--
ALTER TABLE `stars`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `planet`
--
ALTER TABLE `planet`
  ADD CONSTRAINT `planet_ibfk_1` FOREIGN KEY (`id_star`) REFERENCES `stars` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

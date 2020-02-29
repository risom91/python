-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 28, 2020 at 08:38 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `color guess`
--

-- --------------------------------------------------------

--
-- Table structure for table `color_users`
--

CREATE TABLE `color_users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `score` int(3) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `color_users`
--

INSERT INTO `color_users` (`user_id`, `name`, `email`, `password`, `score`) VALUES
(1, 'rishabh', 'r@gmail.com', '1234', 11),
(2, 'ab', '12', '12', 17),
(3, 'rajat', 'raj@gmail.com', '1111', 7),
(7, 'aa', 'aaaa', 'aaaa', 0),
(8, 'gy', 'biugiuh', 'ygiuhi', 0),
(15, 'uihiu', '123', 'uiiub', 0),
(16, 'yugyf', '12bjk', 'igv', 0),
(17, 'a', '11', '11', 8),
(18, 'rahul', '2', '2', 8),
(19, '3', '33', '3', 8),
(20, '4', '4', '4', 0),
(21, '5', '5', '5', 12),
(22, 'ab', 'abb', 'abb', 9),
(23, 'ahuid', '7', '7', 9),
(24, 'fcad', '8', '8', 8),
(25, '6', '6', '6', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `color_users`
--
ALTER TABLE `color_users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `color_users`
--
ALTER TABLE `color_users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

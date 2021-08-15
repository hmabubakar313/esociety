-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 19, 2021 at 10:34 PM
-- Server version: 8.0.25-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `esociety`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments_section`
--

CREATE TABLE `comments_section` (
  `comments` varchar(255) NOT NULL,
  `comments_reply` varchar(255) NOT NULL,
  `user_id` int NOT NULL,
  `post_id` int NOT NULL,
  `comment_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `like_section`
--

CREATE TABLE `like_section` (
  `likes` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  `post_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `post_details`
--

CREATE TABLE `post_details` (
  `post_title` varchar(255) DEFAULT NULL,
  `post` varchar(255) DEFAULT NULL,
  `date_time` datetime(6) DEFAULT NULL,
  `user_id` int NOT NULL,
  `post_id` int NOT NULL,
  `total_likes` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `user_id` int NOT NULL,
  `username` varchar(250) NOT NULL,
  `e_mail` varchar(255) NOT NULL,
  `password` varchar(20) NOT NULL,
  `birthday` date NOT NULL,
  `reg_no` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`user_id`, `username`, `e_mail`, `password`, `birthday`, `reg_no`) VALUES
(2, 'ali', 'ali@ali.com', '123', '2004-02-22', 'bcs-192015'),
(21, 'ali', 'ali@ali.com', '123', '2004-02-02', 'bcs192012'),
(22, 'ali', 'ali@ali.com', '123', '2004-02-02', 'bcs192012'),
(23, 'ali', 'ali@ali.com', '123', '2004-02-02', 'bcs192012'),
(24, 'ali', 'ali@ali.com', '123', '2004-02-02', 'bcs192012');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments_section`
--
ALTER TABLE `comments_section`
  ADD PRIMARY KEY (`comment_id`),
  ADD UNIQUE KEY `1` (`user_id`),
  ADD UNIQUE KEY `2` (`post_id`);

--
-- Indexes for table `like_section`
--
ALTER TABLE `like_section`
  ADD PRIMARY KEY (`likes`),
  ADD UNIQUE KEY `1` (`user_id`),
  ADD UNIQUE KEY `post_id` (`post_id`),
  ADD KEY `2` (`post_id`),
  ADD KEY `post_id_2` (`post_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `post_id_3` (`post_id`),
  ADD KEY `user_id_2` (`user_id`);

--
-- Indexes for table `post_details`
--
ALTER TABLE `post_details`
  ADD PRIMARY KEY (`post_id`),
  ADD UNIQUE KEY `1` (`post_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `user_id_2` (`user_id`),
  ADD KEY `post_id` (`post_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments_section`
--
ALTER TABLE `comments_section`
  MODIFY `comment_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `like_section`
--
ALTER TABLE `like_section`
  MODIFY `likes` tinyint(1) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `post_details`
--
ALTER TABLE `post_details`
  MODIFY `post_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `user_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comments_section`
--
ALTER TABLE `comments_section`
  ADD CONSTRAINT `comments_section_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `post_details` (`post_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `comments_section_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `students` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `like_section`
--
ALTER TABLE `like_section`
  ADD CONSTRAINT `like_section_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `post_details` (`post_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `like_section_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `students` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `post_details`
--
ALTER TABLE `post_details`
  ADD CONSTRAINT `post_details_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `students` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

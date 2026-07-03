-- phpMyAdmin SQL Dump
-- version 5.2.3deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 03, 2026 at 03:31 PM
-- Server version: 8.4.10-0ubuntu0.26.04.1
-- PHP Version: 8.5.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecommerce_products`
--

-- --------------------------------------------------------

--
-- Table structure for table `collection`
--

CREATE TABLE `collection` (
  `collection_id` int NOT NULL,
  `collection_name` varchar(255) NOT NULL,
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `collection`
--

INSERT INTO `collection` (`collection_id`, `collection_name`, `description`) VALUES
(1, 'Gaming Essentials', 'Products for PC gaming setups.'),
(2, 'Office Setup', 'Products for productivity and office work.');

-- --------------------------------------------------------

--
-- Table structure for table `collection_product_xref`
--

CREATE TABLE `collection_product_xref` (
  `product_id` int NOT NULL,
  `collection_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `collection_product_xref`
--

INSERT INTO `collection_product_xref` (`product_id`, `collection_id`) VALUES
(1, 1),
(2, 1),
(3, 1),
(3, 2),
(4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_name`, `price`, `description`) VALUES
(1, 'Gaming Mouse', 49.99, 'High-precision wireless gaming mouse.'),
(2, 'Mechanical Keyboard', 89.99, 'RGB mechanical keyboard with blue switches.'),
(3, '27-inch Monitor', 229.99, '1440p IPS monitor for gaming and productivity.'),
(4, 'USB-C Dock', 119.99, 'Multi-port docking station for laptops.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `collection`
--
ALTER TABLE `collection`
  ADD PRIMARY KEY (`collection_id`);

--
-- Indexes for table `collection_product_xref`
--
ALTER TABLE `collection_product_xref`
  ADD PRIMARY KEY (`product_id`,`collection_id`),
  ADD KEY `collection_id` (`collection_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `collection`
--
ALTER TABLE `collection`
  MODIFY `collection_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `collection_product_xref`
--
ALTER TABLE `collection_product_xref`
  ADD CONSTRAINT `collection_product_xref_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`),
  ADD CONSTRAINT `collection_product_xref_ibfk_2` FOREIGN KEY (`collection_id`) REFERENCES `collection` (`collection_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

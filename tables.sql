-- query for the users table

CREATE TABLE `capstonedb`.`users` (
  `id` INT(11) NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `age` INT(3) NULL,
  `gender` CHAR(1) NULL,
  `state` VARCHAR(45) NULL,
  `street_address` VARCHAR(45) NULL,
  `postal_code` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `latitude` DECIMAL(10,8) NULL,
  `longitude` DECIMAL(10,7) NULL,
  `traffic_source` VARCHAR(45) NULL,
  `created_at` TIMESTAMP(6) NULL,
  PRIMARY KEY (`id`)
  );

-- query for the events table
CREATE TABLE `capstonedb`.`events` (
  `id` INT(11) NOT NULL,
  `user_id` INT(11) NULL,
  `sequence_number` INT(4) NULL,
  `session_id` VARCHAR(100) NULL,
  `created_at` TIMESTAMP NULL,
  `ip_address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `postal_code` VARCHAR(11) NULL,
  `browser` VARCHAR(45) NULL,
  `traffic_source` VARCHAR(45) NULL,
  `uri` VARCHAR(150) NULL,
  `event_type` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

-- Inventory items table creation
  CREATE TABLE `capstonedb`.`inventory_items` (
  `id` INT(11) NOT NULL,
  `product_id` INT(11) NULL,
  `created_at` TIMESTAMP NULL,
  `sold_at` TIMESTAMP NULL,
  `cost` DECIMAL(12,9) NULL,
  `product_category` VARCHAR(45) NULL,
  `product_name` VARCHAR(300) NULL,
  `product_brand` VARCHAR(45) NULL,
  `product_retail_price` DECIMAL(12,9) NULL,
  `product_department` VARCHAR(10) NULL,
  `product_sku` VARCHAR(70) NULL,
  `product_distribution_center_id` INT(3) NULL,
  PRIMARY KEY (`id`));

-- products table
CREATE TABLE `capstonedb`.`products` (
  `id` INT(11) NOT NULL,
  `cost` DECIMAL(12,9) NULL,
  `category` VARCHAR(45) NULL,
  `name` VARCHAR(300) NULL,
  `brand` VARCHAR(45) NULL,
  `retail_price` DECIMAL(12,9) NULL,
  `department` VARCHAR(10) NULL,
  `sku` VARCHAR(70) NULL,
  `distribution_center_id` INT(3) NULL,
  PRIMARY KEY (`id`));

-- order items table
CREATE TABLE `capstonedb`.`order_items` (
  `id` INT(11) NOT NULL,
  `order_id` INT(11) NULL,
  `user_id` INT(11) NULL,
  `product_id` INT(11) NULL,
  `inventory_item_id` INT(11) NULL,
  `status` VARCHAR(45) NULL,
  `created_at` TIMESTAMP NULL,
  `shipped_at` TIMESTAMP NULL,
  `delivered_at` TIMESTAMP NULL,
  `returned_at` TIMESTAMP NULL,
  `sale_price` DECIMAL(4,0) NULL,
  PRIMARY KEY (`id`));

-- orders table
CREATE TABLE `capstonedb`.`orders` (
  `id` INT(11) NOT NULL,
  `user_id` INT(11) NULL,
  `status` VARCHAR(45) NULL,
  `gender` CHAR(1) NULL,
  `created_at` TIMESTAMP NULL,
  `returned_at` TIMESTAMP NULL,
  `shipped_at` TIMESTAMP NULL,
  `delivered_at` TIMESTAMP NULL,
  `num_of_item` INT(3) NULL,
  PRIMARY KEY (`id`));

-- distribution table

CREATE TABLE `capstonedb`.`distribution_centers` (
  `id` INT(11) NOT NULL,
  `name` VARCHAR(45) NULL,
  `latitude` DECIMAL(7,4) NULL,
  `longitude` DECIMAL(7,4) NULL,
  PRIMARY KEY (`id`));
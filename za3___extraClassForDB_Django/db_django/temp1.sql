--
-- Create model Article
--
CREATE TABLE `tabom_article` (
    `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `title` varchar(255) NOT NULL, 
    `updated_at` datetime(6) NOT NULL, 
    `created_at` datetime(6) NOT NULL
);
--
-- Create model User
--
CREATE TABLE `tabom_user` (
    `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `name` varchar(50) NOT NULL, 
    `updated_at` datetime(6) NOT NULL, 
    `created_at` datetime(6) NOT NULL
);
--
-- Create model Like
--
CREATE TABLE `tabom_like` (
    `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `updated_at` datetime(6) NOT NULL, 
    `created_at` datetime(6) NOT NULL, 
    `article_id` bigint NOT NULL, 
    `user_id` bigint NOT NULL
);

ALTER TABLE `tabom_like`
ADD CONSTRAINT `tabom_like_article_id_f750d964_fk_tabom_article_id` FOREIGN KEY (`article_id`) REFERENCES `tabom_article` (`id`);

ALTER TABLE `tabom_like`
ADD CONSTRAINT `tabom_like_user_id_10faa3ec_fk_tabom_user_id` FOREIGN KEY (`user_id`) REFERENCES `tabom_user` (`id`);

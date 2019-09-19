/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50723
Source Host           : localhost:3307
Source Database       : crawl_everything

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2019-09-20 01:19:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article_info
-- ----------------------------
DROP TABLE IF EXISTS `article_info`;
CREATE TABLE `article_info` (
  `article_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '文章id',
  `jk_source` varchar(50) DEFAULT NULL COMMENT '文章来源',
  `jk_title` varchar(200) DEFAULT NULL COMMENT '文章标题',
  `jk_url` varchar(200) DEFAULT NULL COMMENT '文章url',
  `jk_status` varchar(50) DEFAULT '0' COMMENT '状态 0:禁用，1:正常',
  `jk_remark` varchar(500) DEFAULT NULL COMMENT '备注',
  `jk_create` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`article_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='文章相关';

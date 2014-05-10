
use funtyping;
CREATE TABLE IF NOT EXISTS `user`(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(15) NOT NULL DEFAULT '',
  `salt` varchar(15) NOT NULL DEFAULT '',
  `username` varchar(30) NOT NULL DEFAULT '',
  `email` varchar(63) NOT NULL DEFAULT '',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` char(1) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='account info';

CREATE TABLE IF NOT EXISTS `user_config`(
  `user_id` int(11) NOT NULL,
  `timezone` tinyint(2) NOT NULL DEFAULT '8',
  `send_time` time NOT NULL DEFAULT '08:00:00',
  `include_entry` tinyint(1) NOT NULL DEFAULT '1',
  `frequency` char(1) NOT NULL DEFAULT 'd',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='user configuration';

CREATE TABLE IF NOT EXISTS `note`(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `content` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `author_entries` (`user_id`,`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='notes';

CREATE TABLE IF NOT EXISTS `user_regist`(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(63) NOT NULL DEFAULT '',
  `code` varchar(150) NOT NULL DEFAULT '',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='user regist info';



PlayerStats.csv is a dataset I created with every NBA player who has suffered an ACL, Achilles, or meniscus injury since the 2009-10 season, along with post-recovery performances and certain characteristics. Players were extracted from a larger dataset recording every injury in the NBA from the 2010-2020 seasons and added to this one with the following characteristics: 

 - Player is the last name, and sometimes first initial, of the player that was injured.

 - Injury type describes the injury with an integer: 0 for torn ACL, 1 for torn Achilles, and 2 for torn meniscus. If a player tore both their ACL and meniscus, they were given a 0, as the ACL is the more significant injury.

 - Season is the season that the injury occurred. For example, if a player was injured in the 2015-16 season, the year 2016 is written.
 
 - LEBRON diff is the difference in the average on the player's LEBRON score of the two seasons before injury and the two seasons post-recovery. If a player did not play two seasons before or after the injury, only one was used. Scores of -10 in this column indicate that the player did not return to play in the NBA after the injury. This usually meant that the player was never able to fully recover to compete at the NBA level again.

 - BPM diff is the difference in the average on the player's BPM score of the two seasons before injury and the two seasons post-recovery. If a player did not play two seasons before or after the injury, only one was used, and scores of -10 in this column indicate that the player did not return to play in the NBA after the injury.

 - Age indicates the age at which the athlete was injured.

 - Height indicates the height of the player in inches.

 - Weight indicates the weight of the player in pounds.

 - Previous injury describes the player's injury history with an integer: 0 if they have never suffered one of the three injuries at a previous moment in their careers, 1 if they have.

 - Change describes the impact of the injury on the player's performance with one of four integers, determined by looking at the LEBRON diff and BPM diff columns: 1 if their performance significantly decreased, 2 if their performance dropped a medium amount, 3 if there was minimal to no change, and 4 if they returned and improved.

 - O-LEBRON diff is the difference in the average on the player's O-LEBRON score of the two seasons before injury and the two seasons post-recovery. If a player did not play two seasons before or after the injury, only one was used. Scores of -5 in this column indicate that the player did not return to play in the NBA after the injury.

 - D-LEBRON diff is the difference in the average on the player's D-LEBRON score of the two seasons before injury and the two seasons post-recovery. If a player did not play two seasons before or after the injury, only one was used, and scores of -5 in this column indicate that the player did not return to play in the NBA after the injury.

 - Avg minutes indicates the average amount of minutes that player played per game in the season prior to injury.

 - O-change describes the impact of the injury on the player's offensive performance with one of four integers, determined by looking at the O-LEBRON diff column: 1 if their performance significantly decreased, 2 if their performance dropped a medium amount, 3 if there was minimal to no change, and 4 if they returned and improved.
 
 - D-change describes the impact of the injury on the player's defensive performance with one of four integers, determined by looking at the D-LEBRON diff column: 1 if their performance significantly decreased, 2 if their performance dropped a medium amount, 3 if there was minimal to no change, and 4 if they returned and improved.

 Source: https://github.com/derekgao2/NBA-Injuries 
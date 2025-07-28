
# NBA Serious Injury Analysis: Dataset Description

This document provides a detailed description of the `PlayerStats.csv` dataset, which is used for analyzing the impact of serious injuries (ACL, Achilles, and Meniscus tears) on NBA players' performance. The dataset includes information on players who suffered these injuries since the 2009-10 season, along with their pre-injury characteristics and post-recovery performance metrics. The data was compiled from a larger dataset tracking NBA injuries from 2010-2020.

## Dataset Features:

*   **Player**: The last name, and sometimes first initial, of the injured player.

*   **Injury type**: Categorizes the injury with an integer:
    *   `0`: Torn ACL
    *   `1`: Torn Achilles
    *   `2`: Torn Meniscus
    *   *Note*: If a player tore both their ACL and meniscus, `0` was assigned due to the ACL being the more significant injury.

*   **Season**: The NBA season in which the injury occurred (e.g., `2016` for the 2015-16 season).

*   **LEBRON diff**: The difference in the player's average **LEBRON** score between the two seasons *before* injury and the two seasons *post-recovery*. If two seasons were not available, only one was used. A score of `-10` indicates the player **did not return** to play in the NBA, often due to an inability to fully recover.

*   **BPM diff**: The difference in the player's average **BPM** score between the two seasons *before* injury and the two seasons *post-recovery*. Similar to LEBRON diff, only one season was used if two were unavailable. A score of `-10` also signifies that the player **did not return** to play in the NBA.

*   **Age**: The age of the athlete at the time of injury.

*   **Height**: The player's height in inches.

*   **Weight**: The player's weight in pounds.

*   **Previous injury**: Indicates the player's history with one of the three specified serious injuries:
    *   `0`: No previous occurrence of an ACL, Achilles, or meniscus tear.
    *   `1`: Has previously suffered one of these three injuries.

*   **Change**: Describes the overall impact of the injury on the player's performance, categorized by analyzing **LEBRON diff** and **BPM diff**:
    *   `1`: Performance significantly decreased.
    *   `2`: Performance dropped a medium amount.
    *   `3`: Minimal to no change in performance.
    *   `4`: Player returned and improved performance.

*   **O-LEBRON diff**: The difference in the player's average **Offensive LEBRON** score between the two seasons *before* injury and the two seasons *post-recovery*. A score of `-5` indicates the player **did not return** to play in the NBA.

*   **D-LEBRON diff**: The difference in the player's average **Defensive LEBRON** score between the two seasons *before* injury and the two seasons *post-recovery*. A score of `-5` indicates the player **did not return** to play in the NBA.

*   **Avg minutes**: The average minutes played per game in the season *prior* to injury.

*   **O-change**: Describes the impact of the injury on the player's **offensive performance**, based on **O-LEBRON diff**:
    *   `1`: Performance significantly decreased.
    *   `2`: Performance dropped a medium amount.
    *   `3`: Minimal to no change in performance.
    *   `4`: Player returned and improved performance.

*   **D-change**: Describes the impact of the injury on the player's **defensive performance**, based on **D-LEBRON diff**:
    *   `1`: Performance significantly decreased.
    *   `2`: Performance dropped a medium amount.
    *   `3`: Minimal to no change in performance.
    *   `4`: Player returned and improved performance.

## Conclusion:

This dataset provides a comprehensive basis for exploring various factors influencing NBA player recovery and performance after serious knee and Achilles injuries. The detailed features allow for in-depth analysis of correlations between player characteristics, injury types, and post-injury career trajectories.

---

## Source:

[NBA-Injuries GitHub Repository](https://github.com/derekgao2/NBA-Injuries) 
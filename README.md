# Working-with-IPL-Data
This file consist of solutions for certain Data problem stated with respect to IPL data.

Data Set Given : https://docs.google.com/spreadsheets/d/1ctWoqqDg2sA77qclZlHGSK-TvcuO-UYJYOEw4TQDSGk/edit#gid=672337210

Ask
Create a personal copy of the data to analyze the data to answer the following questions.
The choice of tool for analysis is not a restriction

•	Balls per Wicket, Balls per Six, and Runs per Wicket
•	The ratio of total balls to total dots for each batsman
•	Percentage of boundary runs to total runs for each batsman
•	Batsman responsible for the most wins
•	Best Death Over Bowler
•	Most Fifties by Batsmen


About the Dataset given:
	The data set given is the IPL Dataset which has records of IPL matches – Ball by ball with certain features like match_id, innings, batting_team, bowling_team, striker, non_striker etc..,
It has 179078 observations and 21 features.

Approach:
	The approach for the problem statement, is quite simple, since the data set is clean, as there is no any need for Data cleaning, and pre-processing.
Data Manipulation tasks plays significant role in the approach to the problem statement. It includes:
•	Filter
•	Group by
•	Sorting/order by
•	Concat/Join
•	Etc..,
The approach to the problem is, to prepare data for different requirements which has been asked as questions and that is done through creating sub sets for the given data.
I created subsets for data from the root data/ given data, and it includes:

![image](https://user-images.githubusercontent.com/80576855/211581481-ef95d85d-9fbb-48d4-a438-2675da9a9f80.png)

Tools Used:	
•	Python
•	Pandas
•	Numpy
•	Seaborn/Matplotlib


Information on the Subsets:
	Subsets have been created through Data manipulation and Feature Extraction, it includes, 
•	combing two features
•	applying functions on features
•	mapping values to features
•	calculations on the features etc..,

Batsmen Data set:
It consists of features like:
'Batsmen', 'Runs', 'Balls Faced', 'Strike Rate', 'Matches Played',
'Sixes', 'Fours', 'Triples', 'Doubles', 'Singles', 'Dismissals',
'Caught', 'Bowled', 'RunOut', 'LBW', '50s', '100s', '150s', '200s',
'Bp6', 'Bp4', 'Best', 'Wins', 'Wins Percentage', 'Dots', 'Dots Rate',
'Boundary_Runs', 'BR Percent'.

Bowlers Data set:
It consists of features like:
'Bowlers', 'Wickets', 'Balls Bowled', 'Overs Bowled', 'Strike Rate',
'Extras', 'Runs Conceded', 'Economy', 'Dots', 'Best'

Match Data set:
It consists of features like:
'match_id', 'First Innings', 'Second Innings', 'First Innings Score',
'Second Innings Score', 'Winner', 'Batting wins', 'Bowling wins'

Fielder Data set:
It consists of features like:
'Fielders', 'Catches', 'Run Outs'

Death & Power Play Overs Data set:
It consists of features like:
'Bowlers', 'Runs Conceded', 'Wickets', 'Economy', 'Balls', 'Overs', 'Dots'



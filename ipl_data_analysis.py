# -*- coding: utf-8 -*-
"""IPL_Data_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nWe2bVS38TtPnfV40ftUTHkMR8COpOhg

## **Data Analysis : Problem Statement**

###**Ask**

Create a personal copy of the data to analyze the data to answer the following questions.
The choice of tool for analysis is not a restriction

- Balls per Wicket, Balls per Six, and Runs per Wicket
- The ratio of total balls to total dots for each batsman
- Percentage of boundary runs to total runs for each batsman
- Batsman responsible for the most wins
- Best Death Over Bowler
- Most Fifties by Batsmen
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
sn.set_style('darkgrid')
import warnings
warnings.filterwarnings('ignore')

root_data = pd.read_csv('IPL_Data_IPL.csv')
Batsmen_data = pd.read_csv('Batsmen_data.csv')
Bowlers_data = pd.read_csv('Bowlers_data.csv')
Match_data = pd.read_csv('Match_data.csv')

root_data.shape

"""## **Analysis on Batsmen**"""

Batsmen_data.drop('Unnamed: 0', axis =1, inplace = True)

Batsmen_data.head()

print('There are', Batsmen_data.shape[0] , 'Batsmen')

"""## **Fields**"""

Batsmen_data.columns

"""### Balls per Six"""

Batsmen_data.sort_values(by = ['Bp6'],ascending = True)[(Batsmen_data['Sixes']!=0) & (Batsmen_data['Balls Faced'] > 100)].head()

sequential_colors = reversed(sn.color_palette("OrRd", 17))
plt.figure(figsize =(15,6))
sn.barplot(data =Batsmen_data.sort_values(by = ['Bp6'],ascending = True)[(Batsmen_data['Sixes']!=0) & (Batsmen_data['Balls Faced'] > 100)].head(15) ,y = 'Bp6',x = 'Batsmen', palette = sequential_colors)
plt.xticks(rotation = 80)
plt.title('Balls per Six')

"""These are the top 15 players who are highly skilled in hitting sixes who are having Balls per six rate within 15.0
- It shows that **AD Russell** a destructive Player who has the chances of hitting a six in every **7(6.75)** balls he face.

### The ratio of total balls to total dots for each batsman
"""

Dots = root_data['total_runs'][root_data['total_runs'] == 0].groupby(by = root_data['batsman']).count()
Dots = Dots.to_dict()
Batsmen_data['Dots'] = Batsmen_data['Batsmen'].map(Dots)
Batsmen_data['Dots'] = Batsmen_data['Dots'].fillna(0)
Batsmen_data['Dots Rate'] = Batsmen_data['Dots']/Batsmen_data['Balls Faced']*100
Batsmen_data['Dots Rate'] = Batsmen_data['Dots Rate'].apply(lambda x : round(x,2))
Batsmen_data.sort_values(by = ['Dots Rate'], ascending = False)[Batsmen_data['Balls Faced']>500].head()

"""The aim of this question is to see who are all the experienced players who have faced at least 500 Balls has highers **Dots Rate**(Total Dot Balls in Total Balls faced)

- Balls faced is an important factor in this, since the dot rate for inexperienced players who have faced minimum number of balls still can have higher Dots Rate.
"""

sequential_colors = reversed(sn.color_palette("YlOrRd", 15))
plt.figure(figsize =(15,6))
sn.barplot(data =Batsmen_data.sort_values(by = ['Dots Rate'], ascending = False)[Batsmen_data['Balls Faced']>500].head(15) ,y = 'Dots Rate',x = 'Batsmen', palette = sequential_colors)
plt.xticks(rotation = 80)
plt.title('Dots Rate')

"""We could see players like
- SC Ganguly
- MS Bisla
- NV Oijha
- M Vijay 
etc..


And also some big hitters like 
- DR Smith
- Ishan Kishan
- CH Gayle

also comes under the list, who made 35-40 % of Balls they faced as Dot Balls.

But on the other hand we cannot make any infereces on the performaces of these players based on their Dot Balls Rate, still there are players in this list who can go for a big chase and capable of scoring high scores with shorter balls.

###Percentage of boundary runs to total runs for each batsman
"""

Batsmen_data['Boundary_Runs'] = (Batsmen_data['Sixes']*6)+(Batsmen_data['Fours']*4)
Batsmen_data['BR Percent'] = Batsmen_data['Boundary_Runs']/Batsmen_data['Runs']*100
Batsmen_data['Boundary_Runs'] = Batsmen_data['Boundary_Runs'].apply(lambda x : round(x,2))
Batsmen_data.sort_values(by = ['Boundary_Runs'],ascending = False).head(10)

sequential_colors = reversed(sn.color_palette("Blues", 25))
sequential_colors2 = reversed(sn.color_palette("BuPu", 25))
plt.figure(figsize =(22,6))
plt.subplot(121)
sn.barplot(data =Batsmen_data.sort_values(by = ['Boundary_Runs'],ascending = False).head(10) ,y = 'Boundary_Runs',x = 'Batsmen', palette = sequential_colors)
plt.xticks(rotation = 80)
plt.title('Boundary Runs')
plt.subplot(122)
sn.barplot(data =Batsmen_data.sort_values(by = ['Boundary_Runs'],ascending = False).head(10) ,y = 'BR Percent',x = 'Batsmen', palette = sequential_colors2)
plt.xticks(rotation = 80)
plt.title('Boundary Percentage')

"""In this above figure we could see the top **10** players who scored higher runs through boundaries. Such a way, we have

- **CH Gayle** on the top who scored **3466** runs only through boundaries

following him

- **SK Raina** on the top 2 who scored **3150** runs only through boundaries.

following him we also have players like

- V Kohli
- DA Warner
- RG Sharma
- AB de Villiars
- S Dhawan
- RV Uthappa
- SR Watson
- MS Dhoni

Looking on the Boundary Percentage:

We have again 

- **CH Gayle** on the top, who has **76%** of the his runs scored only through boundaries.

following him, we have

- **SR Watson** on the top 2, who has **67%** of his runs scored only through boundaries


- DA Warner
- AD de Villiars
- RV Uthappa etc..,

are the players we have following the top 2

###Batsman responsible for the most wins

This question can be seen in many angles

- for example: Wins can be dependent on various factors not only on a good batting of Batsmen of a team.  And those various factors include:

    - Performance of bowlers
    - Pitch
    - Toss
    - Weather and so on...

There are also certain situation/matches where a certain batsman scores high but the team will not win the game and also, a certain batsman won't perform well on that day, or they are only required to score few runs (if the first inning score is very low), the team will win on the other hand..


So, we can solve this through mapping best runs of a batsmen scored in a match to the result of the particular match.

- We can frame condition like:

    if Batsmen run == max(ie., scores 50+ and 100+) and Result == 'Win'

But again we cannot look this as pattern for win since, winning a match is not only dependent on a good batting of a batsman.
"""

Batsmen_runs = pd.read_csv('Batsman_runs_with_results.csv')
Batsmen_runs.drop('Unnamed: 0', axis = 1, inplace = True)
Batsmen_runs.head()

Batsmen_runs.shape

Condition = Batsmen_runs[(Batsmen_runs['Runs']>49) & (Batsmen_runs['Result']==1)]

Condition.head()

tmp_dict = Condition['Batsman'].value_counts().to_dict()
Batsmen_responsible_for_most_wins = pd.DataFrame(columns = ['Batsmen','Wins'])
Batsmen_responsible_for_most_wins['Batsmen'] = tmp_dict.keys()
Batsmen_responsible_for_most_wins['Wins'] = tmp_dict.values()

Batsmen_responsible_for_most_wins.head(10)

sequential_colors2 = reversed(sn.color_palette("Greens", 13))
plt.figure(figsize =(15,6))
Data = Batsmen_responsible_for_most_wins.head(10)
sn.barplot(data = Data, x ='Batsmen',y = 'Wins', palette = sequential_colors2)
plt.xticks(rotation = 80)
plt.title('Batsman Best Runs and Wins')

"""In the above figure we could see the player names like

- DA Warner
- G Gambhir
- SK Raina etc..,

Where, they scored 50+ (more than 50 runs) and the number of wins they had by scoring so. Likewise

- **DA Warner** has **34** wins, when he score more than 50 runs

To prove the irony which I mentioned before, we can also see players who scored more than 50 runs has the match result as 'Lose'.
"""

Condition = Batsmen_runs[(Batsmen_runs['Runs']>49) & (Batsmen_runs['Result']==0)]
Condition.head(15)

"""See the consistency of AB de Villiars, who scores great in subsequent matches, but the results are disappointing."""

tmp_dict = Condition['Batsman'].value_counts().to_dict()
Batsmen_responsible_for_most_wins = pd.DataFrame(columns = ['Batsmen','Wins'])
Batsmen_responsible_for_most_wins['Batsmen'] = tmp_dict.keys()
Batsmen_responsible_for_most_wins['Wins'] = tmp_dict.values()
Batsmen_responsible_for_most_wins.head(10)

sequential_colors2 = reversed(sn.color_palette("Reds", 13))
plt.figure(figsize =(15,6))
Data = Batsmen_responsible_for_most_wins.head(10)
sn.barplot(data = Data, x ='Batsmen',y = 'Wins', palette = sequential_colors2)
plt.xticks(rotation = 80)
plt.title('Batsman Best Runs and Loses')

"""This could be seen as the number of times a player been unlucky!

- V Kohli had good scores in **23** matches but RCB doesn't made it, in the end!


####Therefore winning is not only dependent on a Batsman Performance.

###Most Fifties by Batsmen
"""

Batsmen_data[['Batsmen','50s']].sort_values(by = '50s', ascending = False).head(10)

sequential_colors2 = reversed(sn.color_palette("Purples", 13))
plt.figure(figsize =(15,6))
Data = Batsmen_data[['Batsmen','50s']].sort_values(by = '50s', ascending = False).head(10)
sn.barplot(data = Data, x ='Batsmen',y = '50s', palette = sequential_colors2)
plt.xticks(rotation = 80)
plt.title('Most Fifties by Batsmen')

"""Here are the top 10 batsmen who has maximum 50s in IPL league matches.

- **DA Warner** is on the top, who made **44** half-centuries
- **SK Raina** is on the top 2 who made **38** half-centuries

### Balls per Wicket (Bowling Strike Rate)
"""

Bowlers_data.drop('Unnamed: 0', axis = 1, inplace = True)

Bowlers_data.head()

Bowlers_data[Bowlers_data['Balls Bowled']>500].sort_values(by = 'Strike Rate')

Dataa =Bowlers_data[Bowlers_data['Balls Bowled']>500].sort_values(by = 'Strike Rate').head(15)

Dataa

sequential_colors2 = reversed(sn.color_palette("Greys", 19))
plt.figure(figsize =(15,6))
Data = Batsmen_data[['Batsmen','50s']].sort_values(by = '50s', ascending = False).head(10)
sn.barplot(data = Dataa, x ='Bowlers',y = 'Strike Rate', palette = sequential_colors2)
plt.xticks(rotation = 80)
plt.title('Balls per wicket')

"""DE Bollinger has good Bowling Strike Rate

###Best Death Over Bowler

This data has been extracted from the data manipulation process of this problem. It contains data of players who bowled only between 16-20 overs.
"""

D_over.columns

D_over = pd.read_csv('Death_over_data.csv')
D_over.drop('Unnamed: 0', axis = 1, inplace =True)

D_over.head()

D_over.sort_values(by = 'Wickets',ascending = False)

"""Undoubtedly, the best death over bowler is **SL Malinga**

He conceded **1540** runs which is less than other bowlers in his class in the death over.

He had taken **122** wickets in death overs.

His Death over economy is **7.87**, which is again a comparatively a decent figure.

### Runs per Wicket (Run quotient)
"""

Match_data.drop('Unnamed: 0', axis =1, inplace = True)

Match_data['First Innings'].unique()

Match_data['Second Innings'].unique()

Match_data['Second Innings'].unique() in Match_data['First Innings'].unique()

Teams = Match_data['First Innings'].unique()

runs_scored = root_data['total_runs'].groupby(by = root_data['batting_team']).sum().to_dict()

wickets_lost = root_data['player_dismissed'].groupby(by = root_data['batting_team']).count().to_dict()

runs_conceded = root_data['total_runs'].groupby(by = root_data['bowling_team']).sum().to_dict()

wickets_taken = root_data['player_dismissed'].groupby(by = root_data['bowling_team']).count().to_dict()

Run_qutient_table = pd.DataFrame(columns = ['Teams','Runs Scored','Wickets Lost','Runs Conceded','Wickets Taken'])
Run_qutient_table['Teams'] = runs_scored.keys()
Run_qutient_table['Runs Scored'] = runs_scored.values()
Run_qutient_table['Wickets Lost'] = wickets_lost.values()
Run_qutient_table['Runs Conceded'] = runs_conceded.values()
Run_qutient_table['Wickets Taken'] = wickets_taken.values()

Run_qutient_table

Run_qutient_table['RpW'] = (Run_qutient_table['Runs Scored']/Run_qutient_table['Wickets Lost']) / (Run_qutient_table['Runs Conceded']/Run_qutient_table['Wickets Taken'])

Run_qutient_table.sort_values(by = 'RpW', ascending = False)

"""Chennai Super Kings should be ranked 1st in Run Quotient table, Since they scored more runs than they conceded and they played more number of matches.

## Apart from the Questions

#### BB McCullum is the batsmen who has higher LBW dismissals.
"""

Batsmen_data[['Batsmen','LBW']].sort_values(by = 'LBW', ascending = False).head(10).plot(kind = 'bar', x = 'Batsmen', y='LBW')

"""#### MS Dhoni is the batsmen who has higher run out dismissals."""

Batsmen_data[['Batsmen','RunOut']].sort_values(by = 'RunOut', ascending = False).head(10).plot(kind = 'bar', x = 'Batsmen', y='RunOut')

"""#### V Kohli is the Highest run scorer in IPL"""

Batsmen_data[['Batsmen','Runs']].sort_values(by = 'Runs', ascending = False).head(10).plot(kind = 'bar', x = 'Batsmen', y='Runs')

"""#### V Kohli is the bastmen who made more singles running between the wicket"""

Batsmen_data[['Batsmen','Singles']].sort_values(by = 'Singles', ascending = False).head(10).plot(kind = 'bar', x = 'Batsmen', y='Singles')

"""#### SK Raina is the batsmen who played more number of matches"""

Batsmen_data[['Batsmen','Matches Played']].sort_values(by = 'Matches Played', ascending = False).head(10).plot(kind = 'bar', x = 'Batsmen', y='Matches Played')

"""#### SK Raina is the Batsman who have been dismissed more."""

Batsmen_data[['Batsmen','Dismissals']].sort_values(by = 'Dismissals', ascending = False).head(10).plot(kind = 'bar', x = 'Batsmen', y='Dismissals')

"""#### CH Gayle is the Batsman who have made more Centuries"""

Batsmen_data[['Batsmen','100s']].sort_values(by = '100s', ascending = False).head(10).plot(kind = 'bar', x = 'Batsmen', y='100s')

"""#### SL Malinga is the leading Wicket taker in IPL"""

Bowlers_data[['Bowlers','Wickets']].sort_values(by = 'Wickets', ascending = False).head(10).plot(kind = 'bar', x = 'Bowlers', y='Wickets')

"""#### SL Mallinga is the bowler who bowled more Extras"""

Bowlers_data[['Bowlers','Extras']].sort_values(by = 'Extras', ascending = False).head(10).plot(kind = 'bar', x = 'Bowlers', y='Extras')

"""#### A Kumble is the bowler who has lowest Economy"""

Bowlers_data[['Bowlers','Economy']][Bowlers_data['Overs Bowled']>100].sort_values(by = 'Economy', ascending = True).head(10).plot(kind = 'bar', x = 'Bowlers', y='Economy')

"""#### PP Chawla is the bowler who have conceded more runs in IPL as a Bowler"""

Bowlers_data[['Bowlers','Runs Conceded']].sort_values(by = 'Runs Conceded', ascending = False).head(10).plot(kind = 'bar', x = 'Bowlers', y='Runs Conceded')

Fielder_data = pd.read_csv('Fielders_data.csv')
Fielder_data.drop('Unnamed: 0', axis = 1, inplace = True)

"""#### KD Karthik is the player who caught more number of catches"""

Fielder_data[['Fielders','Catches']].sort_values(by = 'Catches', ascending = False).head(10).plot(kind = 'bar', x = 'Fielders', y='Catches')

"""#### MS Dhoni is the Player who made more run out dismissals"""

Fielder_data[['Fielders','Run Outs']].sort_values(by = 'Run Outs', ascending = False).head(10).plot(kind = 'bar', x = 'Fielders', y='Run Outs')

PP_data = pd.read_csv('PP_over_data.csv')
PP_data.drop('Unnamed: 0', axis = 1, inplace = True)

"""#### Z Khan is the highest wicket taker in Power Play"""

PP_data[['Bowlers','Wickets']].sort_values(by = 'Wickets', ascending = False).head(10).plot(kind = 'bar', x = 'Bowlers', y='Wickets')

"""#### P Kumar is the bowler who conceded more runs in Power Play"""

PP_data[['Bowlers','Runs Conceded']].sort_values(by = 'Runs Conceded', ascending = False).head(10).plot(kind = 'bar', x = 'Bowlers', y='Runs Conceded')

"""#### B Kumar is the bowler who has good economy in power play"""

PP_data[['Bowlers','Economy']][PP_data['Overs']>100].sort_values(by = 'Economy', ascending = True).head(10).plot(kind = 'bar', x = 'Bowlers', y='Economy')
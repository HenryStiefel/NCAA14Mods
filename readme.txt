The scripts in this repository modify csv files which generate data for players in the NCAA 14 game. 
They were created to modify the behavior of the game by affecting player attribute progression/regression, assigning new jersey numbers for players, and normalizing attributes. 
A simple GUI was created with tkinter.

Module 1 affects logic for existing players. First, it randomly chooses to progress or regress a player, then modifies that player's attributes according to their position 
(ex - QB throw power may increase/decrease, for defensive players tackle/pursuit rating is increased or decreased.) It uses a "dice" system to determine the outcome of progression or regression, 
as well as the degree to which attributes are modified. This module is also responsible for assigning new numbers for freshmen level players (ex - HBs can receive #1-45, rather than just #20-49), 
which helps keep the game feeling fresh. Also, there is an option to normalize QB awareness rating for "big" schools - QB awareness rating plays a big role in the simulation engine inside the game, 
so this helps to prevent the drop off that big schools usually face in their season W/L records.

Module 2 affects the csv file containing data of high school recruit players. Sometimes the game generates players named "Edward Edwards" or "Taylor Taylor" - this fixes that issue. Also, it 
allows suffixes to be added to names, for example "Mike Jones Jr." or "Billy Bob IV". Hyphenated last names also may be seen, such as "Maurice Jones-Drew". This helps keep the game fresh and varies 
players. Finally, it gives an awareness boost to certain highly rated recruits - as we have seen more and more recruits come straight out of high school and have a big impact at the college level, 
this increases the impact these players will have.

Module 3 finally provides better logic for draft declaration. In the base game, many players who are highly rated will not declare for the NFL draft, which is unrealistic. This expands the logic so 
that more RS SO, JR, and RS JR players will declare when their overall is high enough.

The ProgressionRegression.py file is the master file that implements the three modules and contains the GUI. 

cmdscript.bat is a batch file which runs a command to compact the modules into an executable file, ProgressionRegressionl.exe.
This allows users to run the scripts on any computer without needing the python source code available.

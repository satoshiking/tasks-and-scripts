Test task (WoWS Analyst)

Within the archive you can find a SQLite3 database with a slice of game logs from World of
Warships. Complete the tasks using any data analysis and visualization tools at your discretion.

Please send the results in form of a brief report in PDF. You should assume that the report
would be directed to your manager. Should any code would be used for the work, please submit it with your results.


Database description
There are 4 tables in the database:
1. arenas – data about battles: game mode, map used, battle duration, which team won
the battle and so on.
2. arena_members – data about battle participants: their ids, ids of ships used, various
battle statistics. Negative values of ‘account_db_id’ (ids of participants) mark
users controlled by AI (bots).
3. glossary_ships – ships description: their countries, classes, levels.
4. catalog_items – catalog of some in-game entities (maps, game modes, etc.).


Tasks
1. Analyze popularity of different game modes (‘team_build_type_id’ in arenas)
and visualize your findings. Explain your choices of methods of analysis and
visualization.
2. Analyze efficiency of ships in battle using methodology you find the most suitable for it.
Visualize the results and explain your choice of methods.
3. Observe the data provided and pick 1-2 insights you find the most interesting and useful
for the game development team. Explain your choice of insights and their possible
significance for the game.
4. Assuming you’d have more time for the tasks, what would you improve in your
answers? What additional information would you require for that?

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Analize popularity of different game modes
con = sqlite3.connect("Dataset.db")
df = pd.read_sql("SELECT team_build_type_id from arenas", con)

modes = {}
sum = 0
for mode in df['team_build_type_id'].unique():
    a = df.loc[df.loc[:, 'team_build_type_id'] == mode].count()
    modes[mode] = a[0]
    sum += a[0]

# Create a list of tuples sorted by value field
listofTuples = sorted(modes.items(),  key=lambda x: (x[1], x[0]), reverse=True)

print("Statistics for the past {} games:".format(sum))
for elem in listofTuples:
    print("Game mode {} represents {:.1%} of all games".format(elem[0], elem[1]/sum))


# Analize efficency of ships in battle
df = pd.read_sql("SELECT vehicle_type_id, account_db_id, team_build_type_id, " +
                 "item_class, item_desc2, item_level, duration_sec, " +
                 "ships_killed, planes_killed, damage, team_damage " +
                 "from arena_members as am, glossary_ships, arenas as ar " +
                 "where item_cd=vehicle_type_id and am.arena_id=ar.arena_id", con)

print("Check quality of the data, empty fields and duplicates")
print(df.isna().sum())
print('duplicated=', df.duplicated().sum())
print()


df['efficiency'] = ((df['damage'] - df['team_damage']) * (100 / df['damage'].median()) +
                    df['ships_killed']*100 + df['planes_killed']*25)
df = df.astype({'efficiency': int})
# to mark who controls ship human or AI
df['control'] = df.apply(lambda x: 1 if x['account_db_id'] > 0 else 0, axis=1)

# Number of unique players
users_human = df.loc[df.loc[:, 'control'] == 1]['account_db_id'].unique()
users_AI = df.loc[df.loc[:, 'control'] == 0]['account_db_id'].unique()
print('There {} unique players and {} unique AI players'.format(len(users_human), len(users_AI)))

# Efficiency, range and average/median
print()
print('Efficiency is in range: [{},{}]'.format(df['efficiency'].min(), df['efficiency'].max()))
print("Average/median efficiency = {:.2f} / {:.2f}".
      format(df['efficiency'].mean(), df['efficiency'].median()))


# Histogram of efficiency distribution
plt.hist(df['efficiency'], bins=50, density=True, alpha=0.6, color='g')
plt.show()


# Best and worst players
print()
print("top 3 best players:")
hero = df.sort_values(by='efficiency', ascending=False).head(3)
print(hero.loc[:, ['efficiency', 'damage', 'team_damage', 'ships_killed', 'planes_killed']])

print("top 3 worst players:")
loser = df.sort_values(by='efficiency', ascending=True).head(3)
print(loser.loc[:, ['efficiency', 'damage', 'team_damage', 'ships_killed', 'planes_killed']])


# Group by different attributes to answer some questions
print()
print(df.groupby('item_class')['efficiency'].median())
print()
print(df.groupby('item_desc2')['efficiency'].median())
print()
print(df.groupby('item_level')['efficiency'].median())
print()
print(df.groupby('control')['efficiency'].median())
print()
print(df.groupby('team_build_type_id')['efficiency'].median())

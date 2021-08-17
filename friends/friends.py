import sqlite3
conn = sqlite3.connect("my_friends.db")
#create cursor object
c = conn.cursor()
#execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends
# 					VALUES ('Merriwether', 'Lewis', 7)'''

# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
# Insert all at once
# c.execute(insert_query)

# people = [
# 	("Roald","Amundsen", 5),
# 	("Rosa", "Parks", 8),
# 	("Henry", "Hudson", 7),
# 	("Neil","Armstrong", 7),
# 	("Daniel", "Boone", 3)]

# for person in people:
# 	insert that one person
# average = 0
# for person in people:
# 	c.execute("INSERT INTO friends VALUES (?,?,?)", person)
# 	average += person[2]
# print(average/len(people))

c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
# for result in c:
# 	print(result)

print(c.fetchall())
# print(c.fetchone())

#commit changes
conn.commit()
conn.close()
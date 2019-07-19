"""
Created on Fri Jul 19 12:35:11 2019

@author: Valerie Langat
"""
###             SPRINT CHALLENGE PART ONE           ###
import sqlite3

conn = sqlite3.connect('demo_data.sqlite')
curs = conn.cursor()

curs.execute("DROP TABLE IF EXISTS demo")


create_demo_table = """
        CREATE TABLE demo (
                s PRIMARY KEY,
                x INT,
                y INT
                )
"""

curs.execute(create_demo_table)

row_tuples = [('g', 3, 9),
              ('v', 5, 7),
              ('f', 8, 7)]

for row in row_tuples:
        insert_row = "INSERT INTO demo VALUES" + str(row)
        curs.execute(insert_row)
      
conn.commit()

sprint_questions = ['1: Count how many rows you have - should get 3'
                    '2: How many rows are there where x and y are at least 5?'
                    '3: How many unique values of y?']

sprint_queries = ["SELECT COUNT(*) FROM demo;",
                  "SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5;",
                  "SELECT COUNT(DISTINCT y) FROM demo;"]

for i in range(len(sprint_questions)):
        print(sprint_questions[i])
        curs.execute(sprint_queries[i])
        print(curs.fetchall()[i][0])
        print('2\n')
        print('2\n')
     

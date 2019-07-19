"""
Created on Fri Jul 19 12:39:29 2019

@author: Valerie Langat
"""
###          SPRINT CHALLENGE PART TWO           ###


#import and connect to database files#
import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

#Questions from sprint and corresponding queries#
sprint_questions = ['1: What are the ten most expensive items (per unit price) in the database?',
                    '2: What is the average age of an employee at the time of their hiring?',
                    '3: How does the average age of employees at time of hire vary by cities?']

sprint_sql_queries = ["SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;",
                      "SELECT ROUND(AVG(HireDate - BirthDate),1) AS Avg_Age FROM Employee;",
                      "SELECT CITY, AVG(HireDate - BirthDate) AS Avg_Age FROM Employee GROUP BY CITY;"]

#Answers after running queries through DB Browser for SQLite
print('Answers from Part Two Questions:\n')
print('''Question One: Côte de Blaye, Thüringer Rostbratwurst, Mishi Kobe Niku, Sir Rodneys Marmalade, Carnarvon Tigers,
Raclette Courdavault, Manjimup Dried Apples, Tarte au sucre, Ipoh Coffee, Rössle Sauerkraut \n''')
print('''Question Two: 37.2 years old\n''')
print('''Question Three: Query returned with all 0s. I'm sure that's wrong--- Figured it out. Had a typo \n''')


#('''for i in range(len(sprint_questions)):
#    print(sprint_questions[i])
#    curs.execute(sprint_sql_queries[i])
#    results = curs.fetchall()
#    if len(results) == 1:
#            print(results)
#    else: 
#            for res in results:
#                    print(res)
#    print('\n')''')
    


    
###               SPRINT CHALLENGE PART THREE                ####
    
qtna = ['1: What are the 10 most expensive items (per unit price) in the database *and* their suppliers?',
        '2: What is the largest category (by number of unique products)?',
        '3: Who is the employee with most territories?']

qtna_answers = ["SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName AS Supplier FROM Product, Supplier WHERE Product.SupplierID = Supplier.ID ORDER BY UnitPrice DESC LIMIT 10;",
                "SELECT Category.CategoryName, COUNT(*) FROM Product, Category WHERE Product.CategoryID = Category.ID GROUP BY Product.CategoryID ORDER BY COUNT(*) DESC LIMIT 1;",
                "SELECT Employee.LastName, COUNT(*) FROM Employee, EmployeeTerritory WHERE EmployeeTerritory.EmployeeID = Employee.ID GROUP BY Employee.ID ORDER BY COUNT(*) DESC LIMIT 1;"]


#(not working well here either, i'll come back later)
#('''for i in range(len(qtna)):
#        print(qtna[i])
#       curs.execute(qtna_answers[i])
#      results = curs.fetchall()
#     if len(results) == 1
#        print(results)
#        else:
#            for res in results:
#                print(res)
#        print('\n')''')



#Anwers after querying in DB Browser for SQLite#
print('''Answers from Part Three Questions: \n''')
print('''Q1: Côte de Blaye
Thüringer Rostbratwurst
Mishi Kobe Niku
Sir Rodney's Marmalade
Carnarvon Tigers
Raclette Courdavault
Manjimup Dried Apples
Tarte au sucre
Ipoh Coffee
Rössle Sauerkraut \n''')
print('Q2: Confections with a count of 13 \n')
print('Q3: Robert King \n')



###                 PART FOUR RESPONSES           ###
print(''' Part Four: 1. The relationship between employee and territory is one-to-many.
2. A non-relational database like MongoDB is best used when dealing with large sets of data.
It's helpful because when companies need to find ways to scale, they can now worry less about a perfectly 
organized warehouse and more about functionality. In other uses where scalability is not a priority, it's 
preferable to use a relational database like SQL.
3. NewSQL is a newer database store that hopes to give the best of both worlds. It allows companies to scale
their data while still keeping up with functionality from relational databases. It is also ACID compliant.\n''')



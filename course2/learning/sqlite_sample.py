import sqlite3
from get_filename import get_filename

MyDb = sqlite3.connect(get_filename('prova').replace('txt', 'db'))

c = MyDb.cursor()

# c.execute(
#     '''
#     CREATE TABLE Student (
#         StudentID text,
#         Firstname text,
#         Surname text,
#         DOB date,
#         FormGroup text
#     )
#     '''
# )


c.execute(
    '''
    DELETE FROM STUDENT
    '''
)

values = [
    ('001', 'MARY', 'gianni', '11-11-11', '11W'),
    ('002', 'MARio', 'gianni', '11-11-11', '11w'),
    ('003', 'caròo', 'gianni', '11-11-11', '10w'),
    ('004', 'afsdfasf', 'gianni', '11-11-11', '10w'),
]

c.executemany(
    '''
    INSERT INTO Student
    VALUES (?,?,?,?,?)
    ''', values)

# c.execute(
#     '''
#     SELECT *
#     FROM Student
#     '''
# )

# for row in c.fetchall():
#     print(row)


# c.execute(
#     '''
#     SELECT Firstname, Surname
#     FROM Student
#     WHERE FormGroup = '10w'
#     '''
# )

# print(c.fetchone())

c.execute(
    '''
    SELECT MAX(Firstname)
    FROM Student
    GROUP BY FormGroup = '10w'
    '''
)

print(c.fetchall())


# MyDb.commit()
MyDb.close()

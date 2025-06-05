import sqlite3

con = sqlite3.connect("mydb.db")

# con.execute("create table reg(id int primary key, name varchar(30), email varchar(50))")

# con.execute("insert into reg values(1,'test','test@gmail.com')")
# con.execute("insert into reg(id,name) values(2,'Vishal')")
# con.execute("update reg set email='vishal@gmial.com' where id=2")

# con.execute("INSERT INTO reg (id, name, email) VALUES (3, 'Alice Johnson', 'alice.johnson@example.com'), (4, 'Bob Smith', 'bob.smith@example.com'),(5, 'Charlie Brown', 'charlie.brown@example.com'),(6, 'Diana Rose', 'diana.rose@example.com'),(7, 'Ethan Clark', 'ethan.clark@example.com'),(8, 'Fiona Davis', 'fiona.davis@example.com'),(9, 'George Miller', 'george.miller@example.com'),(10, 'Hannah Lee', 'hannah.lee@example.com'),(11, 'Ian Moore', 'ian.moore@example.com'),(12, 'Julia Adams', 'julia.adams@example.com')")


# con.commit()

# data = con.execute("select * from reg")

# for i in data.fetchall():
#     for k in i:
#         print(k,end="  ")
#     print()


con.execute("delete from reg where id=12")
con.commit()

import random
import sqlite3
def create_db():
    con=sqlite3.connect("dice.db")
    cur=con.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS rolls(
                id integer primary key autoincrement,
                value integer);
                """)
    con.commit()
    con.close()
   

def roll_dice():
    value=random.randint(1,6)
    con=sqlite3.connect("dice.db")
    cur=con.cursor()
    cur.execute("INSERT INTO rolls(value) VALUES (?);",(value,))
    con.commit()
    cur.close()
    print(f'You rolled:{value}')
def show_statistics():
    con=sqlite3.connect("dice.db")
    cur=con.cursor()
    cur.execute("SELECT COUNT(*) FROM rolls;")
    total=cur.fetchone()[0]

    if total==0:
        print('No dice rolls till now!')
        return 
    print(f"Total rolls:{total}")

    cur.execute('''SELECT value,count(*) as Count
                              from rolls
                              group by value
                              order by value asc;''')
    results=cur.fetchall()
    max_count=0
    max_frequent=None
    for value ,count in results:
        percent=(count/total)*100
        print(f'Number:{value}:Count {count} times {percent:.2f}')

        if count>max_count:
            max_count=count
            max_frequent=value
    print(f'Most frequent number is {max_frequent}')
    con.close()

def main():
    create_db()
    while True:
        print("1.Enter 1 to roll dice")
        print("2.Enter 2 to show statistics")
        print("3.Enter 3 to exit")
        choice=int(input('Enter input:'))
        if choice==1:
            roll_dice()
        elif choice==2:
            show_statistics()
        elif choice==3:
            print('GoodBye')
            break
        else:
            print('Invalid choice')
main()
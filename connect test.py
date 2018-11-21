import sqlite3
from sqlite3 import Error

def create_connection(db_NEA):
    """ creates a databse connection to sqlite database by specified db_file """
    try:
        conn = sqlite3.connect(db_NEA)
        return(conn)
    except Error as e:
        print(e)
    return None
        
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def main():
    database = "NEA.db"
 
    sql_create_Teacher_table = """ CREATE TABLE IF NOT EXISTS Teacher (
                                        id autonumber PRIMARY KEY
                                        REFERENCES Student (id),
                                        name text NOT NULL
                                        ); """
 
    sql_create_Student_table = """CREATE TABLE IF NOT EXISTS Student (
                                    id autonumber PRIMARY KEY,
                                    name text NOT NULL
                                    );"""
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_Teacher_table)
        # create tasks table
        create_table(conn, sql_create_Student_table)
    else:
        print("Error! cannot create the database connection.")
        
main()
        
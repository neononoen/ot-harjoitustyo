from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists yarns;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table yarns (
            name text,
            colour text,
            weight integer,
            meters integer,
            type text,
            id text primary key
        );
    ''')

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()

import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    '''
    Creates a connection to the studentdb. Also creates the sparkifydb,
    dropping it if it already exists.

    Returns
    -------
    cursor
        the cursor for the connection
    conn
        the connection to the session
    '''
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student \
                            password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' \
                 TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student \
                             password=student")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    '''
    Drops tables from the database.

    Parameters
    ----------
    cur : cursor
        The cursor to the session connection
    conn : connection
        The session connection
    '''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    '''
    Creates tables in the database.

    Parameters
    cur : cursor
        The cursor to the session connection
    conn : connection
        The session connection
    '''
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    '''
    The main program function.
    '''
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()

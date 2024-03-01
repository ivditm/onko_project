from commands import (table_pop_data_creat,
                      table_pop_data_creat_mort,
                      table_state_cancer_creat,
                      table_state_help_57,
                      table_06_cr,
                      table_57_cr,
                      table_07,
                      view)

import sqlite3


def do_first_migration(conn):
    cursor = conn.cursor()
    try:
        cursor.execute('BEGIN TRANSACTION')
        cursor.execute(table_pop_data_creat)
        cursor.execute(table_pop_data_creat_mort)
        cursor.execute(table_state_cancer_creat)
        cursor.execute(table_state_help_57)
        cursor.execute(table_06_cr)
        cursor.execute(table_57_cr)
        cursor.execute(table_07)
        cursor.execute(view)
        cursor.execute('COMMIT')
    except Exception as e:
        print(f"Error processing file: {e}")
        conn.rollback()
    finally:
        conn.close()


def main():
    connection = sqlite3.connect('data.db')
    do_first_migration(connection)
    print('done')

    connection = sqlite3.connect('data.db')
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    connection.close()


if __name__ == '__main__':
    main()

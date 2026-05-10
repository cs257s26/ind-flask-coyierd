"""psycopg2-sample.py

Sample code demonstrating how to use the psycopg2 Python library to
connect to a database and execute a query.
"""

import psycopg2 as ps

import psqlConfig as config


def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(
            database="coyierd",
            user="coyierd",
            password="plant222heart",
            host="localhost",
        )
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection


def get_sightings_at_stop_for_year(connection, bird, stop, year) -> list:
    """Returns the amount of birds at a given stop at a given year.

    Args:
        connection (psycopg2.connection) - the connection to the database
        temp (float) - the minimum high temperature

    Returns:
        list - a list of all dates where the high temperature is greater or equal to temp, or None if the query fails.
    """
    try:
        cursor = connection.cursor()

        query = 'SELECT * FROM "%s" WHERE bird_name=%s;'
        cursor.execute(query, (year, bird))
        return [cursor.fetchall()[0][stop]]

    except Exception as e:
        print("Something went wrong when executing the query: ", e)
        return None


def get_all_bird_sightings_for_year(connection, bird, year) -> list:
    """Returns the amount of birds at a given stop at a given year.

    Args:
        connection (psycopg2.connection) - the connection to the database
        temp (float) - the minimum high temperature

    Returns:
        list - a list of all dates where the high temperature is greater or equal to temp, or None if the query fails.
    """
    try:
        cursor = connection.cursor()

        query = 'SELECT COALESCE(stop_1, 0) + COALESCE(stop_2, 0) + COALESCE(stop_3, 0) + COALESCE(stop_4, 0) + COALESCE(stop_5, 0) + COALESCE(stop_6, 0) + COALESCE(stop_7, 0) + COALESCE(stop_8, 0) + COALESCE(stop_9, 0) + COALESCE(stop_10, 0) + COALESCE(stop_11, 0) + COALESCE(stop_12, 0) + COALESCE(stop_13, 0) + COALESCE(stop_14, 0) + COALESCE(stop_15, 0) + COALESCE(stop_16, 0) + COALESCE(stop_17, 0) AS total_sightings FROM "%s" WHERE bird_name=%s;'
        cursor.execute(query, (year, bird))
        return cursor.fetchall()

    except Exception as e:
        print("Something went wrong when executing the query: ", e)
        return None


def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_sightings_at_stop_for_year(
        connection, "American Crow (Corvus brachyrhynchos) ", 1, 2017
    )

    if results is not None:
        print(results, "***")
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

    ## Again, for second psql query

    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_all_bird_sightings_for_year(
        connection, "American Crow (Corvus brachyrhynchos) ", 2017
    )

    # print(results)
    # print("*****")
    if results is not None:
        print(results, "***")
        print("Query results: ")
        for item in results:
            print(item)

    # # Disconnect from database
    # connection.close()


main()


# SELECT column_name FROM information_schema.columns
# ORDER BY SUM(column_name) DESC
# LIMIT 1


# SELECT (stop_1 + stop_2 + stop_3 + stop_4 + stop_5 + stop_6 + stop_7 + stop_8 + stop_9 + stop_10 + stop_11 + stop_12 + stop_13 + stop_14 + stop_15 + stop_16 + stop_17) FROM "2017" WHERE bird_name='American Crow (Corvus brachyrhynchos) ';
# SELECT stop_1 + stop_1 FROM "2017" WHERE bird_name='American Crow (Corvus brachyrhynchos) ';

# SELECT COALESCE(stop_1, 0) + COALESCE(stop_2, 0) + COALESCE(stop_3, 0) + COALESCE(stop_4, 0) + COALESCE(stop_5, 0) + COALESCE(stop_6, 0) + COALESCE(stop_7, 0) + COALESCE(stop_8, 0) + COALESCE(stop_9, 0) + COALESCE(stop_10, 0) + COALESCE(stop_11, 0) + COALESCE(stop_12, 0) + COALESCE(stop_13, 0) + COALESCE(stop_14, 0) + COALESCE(stop_15, 0) + COALESCE(stop_16, 0) + COALESCE(stop_17, 0) AS total_sightings FROM "2017" WHERE bird_name='American Crow (Corvus brachyrhynchos) ';
# 'SELECT COALESCE(stop_1, 0) + COALESCE(stop_2, 0) + COALESCE(stop_3, 0) + COALESCE(stop_4, 0) + COALESCE(stop_5, 0) + COALESCE(stop_6, 0) + COALESCE(stop_7, 0) + COALESCE(stop_8, 0) + COALESCE(stop_9, 0) + COALESCE(stop_10, 0) + COALESCE(stop_11, 0) + COALESCE(stop_12, 0) + COALESCE(stop_13, 0) + COALESCE(stop_14, 0) + COALESCE(stop_15, 0) + COALESCE(stop_16, 0) + COALESCE(stop_17, 0) FROM "%s" WHERE bird_name=%s;'

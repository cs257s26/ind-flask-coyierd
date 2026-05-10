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


def get_sightings_at_stop_for_year(connection, bird, stop, year) -> int:
    """Returns the amount of birds at a given stop at a given year.

    Args:
        connection (psycopg2.connection) - the connection to the database
        temp (float) - the minimum high temperature

    Returns:
        list - a list of all dates where the high temperature is greater or equal to temp, or None if the query fails.
    """
    try:
        cursor = connection.cursor()
        stop_var = "stop_" + str(stop)
        year = str(year)

        # query = """SELECT stop_var FROM year;"""
        # cursor.execute(query, (stop_var, year, bird))
        query = "RAISE NOTICE year;"
        cursor.execute(query, (year,))
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
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()


main()

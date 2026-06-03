import psycopg2 as ps

import psqlConfig as config


def connect():
    """Establishes a connection to the database with the following credentials:

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


def get_sightings_at_stop_for_year(connection, bird: str, stop: int, year: int) -> list:
    """Returns the amount of birds at a given stop at a given year.

    Args:
        connection (psycopg2.connection) - the connection to the database
        bird (str) - the bird in consideration
        stop (int) - the stop on the route
        year (int) - the year to find the sightings for

    Returns:
        list - a list with one item, the number of sightings at a single stop
    """
    try:
        cursor = connection.cursor()

        query = 'SELECT * FROM "year_%s" WHERE bird_name=%s;'
        cursor.execute(query, (year, bird))
        return [cursor.fetchall()[0][stop]]

    except Exception as e:
        print("Something went wrong when executing the query: ", e)
        return None


def get_all_bird_sightings_for_year(connection, bird: str, year: int) -> list:
    """Returns the amount of bird sightings for a given year across all stops.

    Args:
        connection (psycopg2.connection) - the connection to the database
        bird (str) - the bird in consideration
        year (int) - the year to find the sightings for

    Returns:
        list - a list with one item, the number of sightings across all stops
    """
    try:
        cursor = connection.cursor()

        query = 'SELECT COALESCE(stop_1, 0) + COALESCE(stop_2, 0) + COALESCE(stop_3, 0) + COALESCE(stop_4, 0) + COALESCE(stop_5, 0) + COALESCE(stop_6, 0) + COALESCE(stop_7, 0) + COALESCE(stop_8, 0) + COALESCE(stop_9, 0) + COALESCE(stop_10, 0) + COALESCE(stop_11, 0) + COALESCE(stop_12, 0) + COALESCE(stop_13, 0) + COALESCE(stop_14, 0) + COALESCE(stop_15, 0) + COALESCE(stop_16, 0) + COALESCE(stop_17, 0) AS total_sightings FROM "year_%s" WHERE bird_name=%s;'
        cursor.execute(query, (year, bird))
        return cursor.fetchall()[0]

    except Exception as e:
        print("Something went wrong when executing the query: ", e)
        return None


def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_sightings_at_stop_for_year(connection, "Blue Jay", 1, 2013)

    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # And for the second psql query

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_all_bird_sightings_for_year(connection, "Blue Jay", 2013)

    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # # Disconnect from database
    connection.close()


main()

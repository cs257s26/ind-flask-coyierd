DO $$
DECLARE
    a INT;
    b INT;
    c INT;
BEGIN
    FOR a IN 2020..2025 LOOP
        DROP TABLE IF EXISTS CAST(a AS TEXT);
        CREATE TABLE CAST(a AS TEXT) (
        bird_name text,
        stop_1 INT,
        stop_2 INT,
        stop_3 INT,
        stop_4 INT,
        stop_5 INT,
        stop_6 INT,
        stop_7 INT,
        stop_8 INT,
        stop_9 INT,
        stop_10 INT,
        stop_11 INT,
        stop_12 INT,
        stop_13 INT,
        stop_14 INT,
        stop_15 INT,
        stop_16 INT,
        stop_17 INT
        );
    END LOOP;

    FOR b IN 2008..2018 LOOP
        DROP TABLE IF EXISTS CAST(b AS TEXT);
        CREATE TABLE CAST(b AS TEXT) (
        bird_name text,
        stop_1 INT,
        stop_2 INT,
        stop_3 INT,
        stop_4 INT,
        stop_5 INT,
        stop_6 INT,
        stop_7 INT,
        stop_8 INT,
        stop_9 INT,
        stop_10 INT,
        stop_11 INT,
        stop_12 INT,
        stop_13 INT,
        stop_14 INT,
        stop_15 INT,
        stop_16 INT,
        stop_17 INT
        );
    END LOOP;

    FOR c IN 2000..2004 LOOP
        DROP TABLE IF EXISTS CAST(c AS TEXT);
        CREATE TABLE CAST(c AS TEXT) (
        bird_name text,
        stop_1 INT,
        stop_2 INT,
        stop_3 INT,
        stop_4 INT,
        stop_5 INT,
        stop_6 INT,
        stop_7 INT,
        stop_8 INT,
        stop_9 INT,
        stop_10 INT,
        stop_11 INT,
        stop_12 INT,
        stop_13 INT,
        stop_14 INT,
        stop_15 INT,
        stop_16 INT,
        stop_17 INT
        );
    END LOOP;
END
$$

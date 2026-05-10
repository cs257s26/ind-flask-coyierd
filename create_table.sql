DO $$
DECLARE
    i int;
    table_name text;
BEGIN
    FOR a IN 2020..2025 LOOP
        DROP TABLE IF EXISTS a;
        CREATE TABLE a (
        bird_name text,
        stop_1 numeric,
        stop_2 numeric,
        stop_3 numeric,
        stop_4 numeric,
        stop_5 numeric,
        stop_6 numeric,
        stop_7 numeric,
        stop_8 numeric,
        stop_9 numeric,
        stop_10 numeric,
        stop_11 numeric,
        stop_12 numeric,
        stop_13 numeric,
        stop_14 numeric,
        stop_15 numeric,
        stop_16 numeric,
        stop_17 numeric
        );
    END LOOP;
END

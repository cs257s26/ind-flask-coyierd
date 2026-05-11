# Collaboration

## Flask
I referenced the flask reading during the process.
I briefly checked in with Dongyu about this assignment, just making sure I had the right files.
Ported in project files but modified command_line.py in numerous places.

## Database

Used ChatGPT for a command to split the cleaned xslx into csv files.
Output:
  I’ll give you a copy-pasteable command that converts each worksheet in one .xlsx file into its own .csv, using sheet names for filenames.Thought for 12sRun this in Terminal, replacing workbook.xlsx with your file name:
  python3 -m pip install --quiet --user xlsx2csv && mkdir -p csv_sheets && python3 -m xlsx2csv -a "workbook.xlsx" csv_sheets/
  It will create a csv_sheets folder and export each worksheet as a separate CSV.



I also had a thread with ChatGPT for how to use a for loop in sql with a variable as the table name. The thread is below.

User: What is the proper syntax for a for loop with create table within the loop in a .sql file for psql


Assistant: I’ll verify against the PostgreSQL docs and then give you a copy-pasteable .sql pattern for psql, including the common dynamic-table-name case.

Thought for 20s

In a .sql file run by psql, use a PL/pgSQL anonymous block with DO $$ ... $$. A plain SQL script does not have a top-level FOR loop; the loop has to live inside PL/pgSQL. PostgreSQL’s DO command executes an anonymous code block, and plpgsql is the default language.

DO $$
DECLARE
    i int;
    table_name text;
BEGIN
    FOR i IN 1..5 LOOP
        table_name := format('my_table_%s', i);

        EXECUTE format(
            'CREATE TABLE IF NOT EXISTS %I (
                id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name text,
                created_at timestamptz DEFAULT now()
            )',
            table_name
        );
    END LOOP;
END
$$ LANGUAGE plpgsql;

Run it with:

psql -d your_database -f your_file.sql

The key point is: if the table name changes inside the loop, you must use dynamic SQL with EXECUTE. PostgreSQL documents that normal variable substitution does not work for changing table or column names, and recommends using format() with %I for identifiers such as table names.

The integer FOR loop syntax is:

FOR i IN 1..10 LOOP
    -- statements
END LOOP;

PostgreSQL also supports query-result loops like:

FOR r IN SELECT ... LOOP
    -- statements
END LOOP;

Both forms are PL/pgSQL loop syntax.

Example looping over rows to create tables:

DO $$
DECLARE
    r record;
BEGIN
    FOR r IN
        SELECT schema_name, table_name
        FROM tables_to_create
    LOOP
        EXECUTE format(
            'CREATE TABLE IF NOT EXISTS %I.%I (
                id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                data text
            )',
            r.schema_name,
            r.table_name
        );
    END LOOP;
END
$$ LANGUAGE plpgsql;

Use %I for identifiers like schema, table, and column names; use %L for literal values when you must interpolate values into dynamic SQL.



User: This loop is causing an error. Any obvious syntax issue? FOR a IN 2020..2025 LOOP DROP TABLE IF EXISTS CAST(a AS TEXT); CREATE TABLE CAST(a AS TEXT) ( What is the simplest fix for this code?



Assistant:
Yes: CAST(a AS TEXT) cannot be used as a table name in normal SQL. Table names are identifiers, not expressions. Use dynamic SQL with EXECUTE.

Simplest fix:

FOR a IN 2020..2025 LOOP
    EXECUTE format('DROP TABLE IF EXISTS %I', a::text);

    EXECUTE format(
        'CREATE TABLE %I (
            -- columns here
            id int
        )',
        a::text
    );
END LOOP;

But table names like "2020" require quoting because they start with a number. format('%I', a::text) handles that automatically.

A cleaner version is to prefix the table name:

FOR a IN 2020..2025 LOOP
    EXECUTE format('DROP TABLE IF EXISTS %I', 'table_' || a);

    EXECUTE format(
        'CREATE TABLE %I (
            id int
        )',
        'table_' || a
    );
END LOOP;

So your direct replacement is: use EXECUTE format(...), not CREATE TABLE CAST(...).



User: Explain all of this 'CREATE TABLE %I ( -- columns here id int )',



Assistant:
That part is a SQL string template passed to format().

'CREATE TABLE %I (
    -- columns here
    id int
)'

It means: “build a CREATE TABLE statement, but leave a placeholder for the table name.”

In context:

EXECUTE format(
    'CREATE TABLE %I (
        -- columns here
        id int
    )',
    a::text
);

Here is what each piece does:

'CREATE TABLE %I (

This starts a string containing SQL. %I is a placeholder used by PostgreSQL’s format() function. It means: “insert this value as a SQL identifier.”

An identifier is something like a table name, column name, or schema name.

So if a = 2020, this:

format('CREATE TABLE %I (id int)', a::text)

becomes roughly:

CREATE TABLE "2020" (
    id int
)

The quotes around "2020" matter because a table name starting with a number is not valid unless quoted.

This part:

-- columns here

is just a SQL comment. It does nothing. It is a reminder to replace it with your real column definitions.

This part:

id int

creates one column named id with type int.

This part:

)'

closes the CREATE TABLE statement string.

The comma after the string:

),
a::text

means: “use a::text as the value for the %I placeholder.”

So this whole command:

EXECUTE format(
    'CREATE TABLE %I (
        id int
    )',
    a::text
);

means:

Dynamically create a table whose name is the current value of a, and give it one integer column called id.

For example, the loop would generate:

CREATE TABLE "2020" (
    id int
);

CREATE TABLE "2021" (
    id int
);

CREATE TABLE "2022" (
    id int
);

and so on.



I used the information about separating the sql command into EXECUTE blocks in my submission. I had already tried using the ::text command.



I also searched up the COALESCE command to factor in null values when summing the sightings across stops for a single year in the second sql query.

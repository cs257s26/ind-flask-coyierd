# README

## Individual Flask 

Two features in the flask app:
1. To see the amount of birds seen across all stops for a certain year, enter http://127.0.0.1:PORT/year_count/<bird>/<year>
  - The <bird> must be exactly as it appears in the csv for that year
2. To see the most popular stop (by birds seen) for a certain year, enter http://127.0.0.1:PORT/popular_stop/<year>

I was running python3 app.py to start the app (need to add port in app.run(host="0.0.0.0", port=####) as needed)
Tests were: python3 -m unittest Tests/test_app.py


## Individual DB

Copy commands (one for each table):
\copy "2000" FROM 'data/csv/2000.csv' DELIMITER ',' CSV
\copy "2001" FROM 'data/csv/2001.csv' DELIMITER ',' CSV
\copy "2002" FROM 'data/csv/2002.csv' DELIMITER ',' CSV
\copy "2004" FROM 'data/csv/2004.csv' DELIMITER ',' CSV
\copy "2008" FROM 'data/csv/2008.csv' DELIMITER ',' CSV
\copy "2010" FROM 'data/csv/2010.csv' DELIMITER ',' CSV
\copy "2012" FROM 'data/csv/2012.csv' DELIMITER ',' CSV
\copy "2013" FROM 'data/csv/2013.csv' DELIMITER ',' CSV
\copy "2014" FROM 'data/csv/2014.csv' DELIMITER ',' CSV
\copy "2016" FROM 'data/csv/2016.csv' DELIMITER ',' CSV
\copy "2017" FROM 'data/csv/2017.csv' DELIMITER ',' CSV
\copy "2018" FROM 'data/csv/2018.csv' DELIMITER ',' CSV
\copy "2020" FROM 'data/csv/2020.csv' DELIMITER ',' CSV
\copy "2021" FROM 'data/csv/2021.csv' DELIMITER ',' CSV
\copy "2022" FROM 'data/csv/2022.csv' DELIMITER ',' CSV
\copy "2023" FROM 'data/csv/2023.csv' DELIMITER ',' CSV
\copy "2024" FROM 'data/csv/2024.csv' DELIMITER ',' CSV
\copy "2025" FROM 'data/csv/2024.csv' DELIMITER ',' CSV

### Questions

Describe the process by which you decided how to represent your data in your database. Include why you selected the number of tables you did, how you decided what data to include and exclude, why you selected the datatypes you did, and what the primary keys are.



Explain how each of your queries represents a user story. What does the query do, and how does this match all or part of a user story?

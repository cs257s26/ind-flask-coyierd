# README

Individual Flask project.

Two features in the flask app:
1. To see the amount of birds seen across all stops for a certain year, enter http://127.0.0.1:PORT/year_count/<bird>/<year>
  - The <bird> must be exactly as it appears in the csv for that year
2. To see the most popular stop (by birds seen) for a certain year, enter http://127.0.0.1:PORT/popular_stop/<year>

I was running python3 app.py to start the app (need to add port in app.run(host="0.0.0.0", port=####) as needed)
Tests were: python3 -m unittest Tests/test_app.py

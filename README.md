# mini-hackathon-1

Task 1 for a Mini Hackathon that I took part in over the summer of 2024 (specifications: https://minihackathon.de/gdge/)

## Sources

Icons Used: https://www.flaticon.com/packs/weather-550?word=weather

# Running the project with Docker

Run `docker compose up` in the root of the project.

You should now be able to access the site from `localhost:8000`.

# Running the project manually

Incase Docker isn't working for some reason, here's how to manually set up and run the project.

Ensure that you have Python 3.10 (or a later version) installed.

Create a virtual environment with `python3 -m venv MYENVNAME` and activate with `. /env/bin/activate` (activating it will depend on your operating system).

Then, run `pip install -r requirements.txt`. Ensure that there are no errors.

Finally, run `python3 manage.py runserver`. You should now be able access the site from `localhost:8000`.

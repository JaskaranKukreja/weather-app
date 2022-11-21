# NOTE: Make sure before performing the below steps python & pip are installed in the system, if not install them from internet.

Open terminal and enter the following commands:-<br/>
    a. Install dependencies `pip install -r requirements.txt`<br/>
    b. Initializing db, run command `python weather_service/sql_db.py`<br/>
    c. Start python job to collect data by command: `python weather_data_collector.py`<br/>
    d. [Optional] To run python backend service in debug mode run command, `export FLASK_DEBUG=1`<br/>
    e. Run command, `export FLASK_APP=weather_service/application.py`<br/>
    e. Run the flask service, by command: `flask run --host=localhost --port=8080`<br/>

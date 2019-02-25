## World emissions tool

#### Intro
https://www.reaktor.com/ennakkotehtava-ohjelmistokehittaja/

#### Requirements and installation
Requirements are located in requirements.txt file, and can be installed with `pip install -r requirements.txt` command.
After installing requirements, the server can be started with `python manage.py runserver`.

#### Heroku
app is running
https://mysterious-mountain-53443.herokuapp.com/app/

#### Walktrough
First open the app page. Here you should see single select input. To use, simply fill all the select boxes which open up one after another. When all the required select inputs are filled, a graph is displayed with the emission data of the selected options. 

To update the emission data, superuser rights are required. Login at <server_url>/accounts/login, and youre redirected to <server_url>/admin_tools. Here it is possible to update either emission data or population data.
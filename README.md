## Capstone Team2 
---
Details of clone project:

* [Project Link](https://github.com/aashishshrestha5532/ecommersesample)
* Tech Stack:
  1. HTML5
  2. CSS3
  3. JavaScript
  4. React JS
---
### e-Commerce Project
#### Team Members
* [Jatin Gharat](https://gitlab.com/jatin_gharat)
* [Rakshit Sarkheliya](https://gitlab.com/sarkheliyarakshit)
* [Vijay Yarramsetty](https://gitlab.com/vijaykumaryv94)
#### Context of the Project:
* This Project is about building a backend for an existing React JS based frontend ready e-commerce application. We have also build some pages from scratch in Javascript and React/Redux, which were not available in original project.

### Requirements

* python version > 3.0.0
* A stable internet connection and an up-to-date browser.
* PostgreSQL server installed in local machine.
* Install additional javascript modules by using the following command in terminal `npm install`.
* Additional python packages required for this project are listed in *requirements.txt*.
* Create a new virtual environment using the command: `python -m virtualenv my_env`.
* Download and install the additional packages by using the command: `pip3 install -r requirements.txt`.
* Download [Docker](https://docs.docker.com/engine/install/ubuntu/) and [Docker Compose](https://docs.docker.com/compose/install/) from the official website.
---

### Working (in docker)

1. Clone this repository.

2. Install `docker` and `docker-compose` and run the following command: `docker-compose up -d --build`. This will create three docker containers for backend, frontend and postgreSQL.

3. After build is done successfully, check the status of containers by using the following command: `docker ps`.

4. Populate the database by using the following command: `docker exec -i docker-container-id psql -U capstone -v -d capstone < backend/capstone_data`, where `docker-container-id` is the container id for postgresql container.

5. Apply the migrations on backend container by using the following command: `docker exec -t -i docker-container-id python manage.py migrate`, where `docker-container-id` is the container id of backend container image.

6. Open browser and go to **`localhost:3000`** to view and interact with the application. The **apis** and **admin** panel can be viewed on **`https://127.0.0.1:8000`** address.

7. To close the session and containers, use the following command: `docker-compose down -v`. 

---

### Working (without docker)


1. To run this application, first clone this repository.

2. Create a virtual environment, activate it, and install the required packages.

3. Create Role and Database in PostgreSQL using the command: `psql -f scripts/CREATE_ROLE_N_DB.sql`.

4. To run frontend, cd to front directory, install frontend packages and use the following command: `npm start`.

5. To run backend, Change directory to `backend` directory using the following command: `cd ../backend`.

6. Dump the data using the following data:`psql -h 127.0.0.1 -U capstone capstone < capstone_data`. 

7. Apply database migrations using the following command: `python manage.py migrate`.

8.  Start the Django development server by executing the following command in the terminal: `python manage.py runserver`.

9.  Then it will start an HTTP Server at the localhost address **http://127.0.0.1:8000**.

10. The frontend server will start at address **localhost:3000**.

11. You can browse through the pages and use functionality similar to any e-commerce website.

12. To stop the both the servers, use `Ctrl + C`.

13. To Delete the Role and Database in PostgreSQL, use the command: `psql -f SQL_SCRIPTS/DELETE_ROLE_N_DB.sql`.

---

#### ADMIN CREDENTIALS (USE IT CAREFULLY)
    email: admin@admin.com
    password: admin
---
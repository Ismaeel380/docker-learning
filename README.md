# Docker Learning

This repository contains the projects and exercises I've completed while learning Docker as part of my DevOps journey.

## CoderCo Docker Challenge

For this challenge, I built a simple web application using Python Flask and Redis.

The application uses two containers. One runs Flask and the other runs Redis. I used Docker Compose to manage both containers and allow them to communicate.

### How it works

The application has two routes:

- `/` displays a welcome message.
- `/count` increases a visit counter stored in Redis.

Each time the counter page is refreshed, Redis updates the number and Flask displays the new value.

### Project files

- `app.py`: Contains the Flask application.
- `requirements.txt`: Lists the Python dependencies.
- `Dockerfile`: Builds the Flask image.
- `Dockerfile.redis`: Uses the Redis image.
- `docker-compose.yml`: Configures both services.

### Running the application

Open a terminal inside the project folder and run:

`docker compose up --build`

Once both containers are running, open:

- `http://localhost:5001`
- `http://localhost:5001/count`

### Problems I encountered

I initially had issues with the indentation in my Docker Compose file. I used `docker compose config` to identify and fix the YAML errors.

I also encountered a Flask import error and an indentation issue in my Python code that caused the container to stop.

Another issue was accessing the application through port 5000. I changed the host port to 5001, which resolved the problem.

After fixing these issues, I managed to get both containers running and confirmed that the Redis counter worked.

### What I learned

This challenge helped me understand how Docker Compose manages multiple containers and how services communicate through Docker networking.

I also gained more practice with Dockerfiles, building images, port mapping and troubleshooting errors using terminal logs.
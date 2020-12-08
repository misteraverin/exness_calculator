## Tom's calculator


### Run application
```shell script
docker-compose up --build -d
open https://127.0.0.1:8000/calculate/ for frontend
open https://127.0.0.1:8000/docs for docs
```

### Technical details
Application was built on:

* FastAPI for backend, jinja2 templates for frontend and sakura.css for beautiful view
* Docker and docker-compose for containers
* black and flake8 as code formatters and linters

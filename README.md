# mapmycrop app

This repository contains two microservices implemented using FastAPI - `map_service` and `auth_service`. 

## Getting Started

To get started, follow the instructions below:

### Clone the Repository

```bash
git clone https://github.com/LarflleezeGonzo/mapmycrop_api
cd mapmycrop_api
```


### Run with Docker Compose
```bash
docker-compose up
```
Once the containers are up and running, the services can be accessed as follows:

map_service runs on [http://127.0.0.1:8000](http://127.0.0.1:8000)
API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
Note: Access to the `map_service` API requires OAuth2-based Bearer JWT. See below on how to obtain an access token.

auth_service runs on [http://127.0.0.1:8001](http://127.0.0.1:8001)
API documentation: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)

### OAuth2-based Bearer JWT

The map_service API requires OAuth2-based Bearer JWT for authentication. Follow the steps below to obtain an access token:
```bash
# Use the following command to obtain an access token:
curl --location 'http://localhost:8001/api/v1/login/access-token' \
--form 'username="admin@test.com"' \
--form 'password="Testing@123"'
# Copy the access token from the response.

# Use the obtained access token in the authorization header for map_service API requests. For example:
curl --location 'http://localhost:8000/api/v1/mapmycrop/historic-weather?longitude=11.0&latitude=11.0&number_of_days=1' \
--header 'Authorization: Bearer <your_access_token>'
```

### Why Two Separate Apps?

The decision to separate the map_service and auth_service follows microservices architecture principles. Separating authentication into its own service allows for reusability across multiple services. This promotes better maintainability, scalability, and flexibility in the long run.

### Why FastAPI?

FastAPI was chosen for its several advantages:

- **Fast:** FastAPI is one of the fastest web frameworks available, thanks to its use of Starlette and Pydantic.
  
- **Interactive API Documentation:** With FastAPI, you get automatic interactive documentation (Swagger UI and ReDoc) for your APIs.
  
- **Type Safety:** Leverages Python type hints for runtime type checking, providing better code reliability.
  
- **Asynchronous Support:** Fully supports asynchronous programming for handling high concurrency with ease.
  
- **Easy Integration with Docker:** Easy to containerize applications using Docker.

Feel free to explore and modify the codebase as needed!



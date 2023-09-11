# CRUD REST API 
This is a CRUD Rest API built with the FastAPI framework. It's a simple crud api that creates, reads, updates , and deletes a person'
name. 

It uses a relational database, specifically SQLite. 

It returns data and accepts in the `application/json` content-type. 

## API Url

    https://hngxtask1api.onrender.com/api
    
## API Endpoints

### GET/READ requests

`GET` - /api/ 
Gets all persons in the databasase. The endpoint receives a get request and returns all the persons in the database.
For example

```python
[
    {
        "id" : 1,
        "name": "Kinlani"
    },
    {
        "id" : 2,
        "name" : "Tijani"
    }

]

```
### GET a specific person resource by name

`GET` - /api/{name} -  
  Returns a specific person to the client. The endpoint receives a get request and returns the specific. 
  A path parameter is used to specify the specific person's details to return. 
`NOTE` : If a wrong path parameter value is sent, then a 404 response stating that the 'User can't be found will be returned'


For example. This the result for calling the endpoint `/api/Tijani`
```python
 {
        "id" : 2,
        "name" : "Tijani"
  }

```

### POST/CREATE - create a specific person resource.

`POST` - /api/
A POST request that creates a person instance. The details/parameters to be sent as `application/json` should include `name` as      the json key and it's value. For example 

```python
  {
    "name" : "Kinlani
  }
```
`NOTE`: If an existing data is used in the data sent, then a 400 response would be returned stating that a 'User already has that     name'    

### UPDATE - Update a specific person resource 

`PUT` - /api/{name} - UPDATE an existing Person resource. 
A PUT request that updates an existing Person resource. A path parameter is required to as it specifies the name of the existing 
resource. 

The update data is sent through the request body in the `application/json` format is used to update the existing resource. 
In all, path parameter is used for identifying the existing resource. 

`NOTE`: 
If a wrong name is inserted or one that doesn't exist, a 404 response
will be returned. 

### DELETE - A specific person resource

`DELETE` - /api/{name} Delete an existing person instance. 



  

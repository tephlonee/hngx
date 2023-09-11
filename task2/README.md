# CRUD REST API 
This is a CRUD Rest API built with the FastAPI framework. It's a simple crud api that creates, reads, updates , and deletes a person'
name. 

It uses a relational database, specifically SQLite. 

It returns data and accepts in the `application/json` content-type. 

## Setup

The API can be set up locally by cloning this repository and running the 
```python
pip install .task2/requirements.txt
```
 to install all the dependencies. 

 In order to run the FastApi app locally. Run the following command

 ```python
    uvicorn task2.main:app --port 8000 --reload
```

## API Url

    https://hngxtask1api.onrender.com/api
## How to use the CRUD API

  - GET A PERSON'S DETAILS. Use the GET request to the `api/{name}` endpoint specified in the DOCUMENTATION.md file.
  - CREATE A PERSON's DETAILS.  Send a POST request to the `api`. Send the data in a json format as the body of the post request      with "name" as an attribute and
    value accompaning it .
  - UPDATE A PERSON's details. Send a PUT request to the `api/{name}` with an old name specified in the path paramter. Send the new
    name as the body of the request. The body should be in json format with the same attribute name as the POST request.
  - DELETE A PERSON's details. Send a delete request to the `api\{name}` with an existing specified in the path parameter. 

## Example Usage

```python

    import requests

    url = "https://hngxtask1api.onrender.com/api"
    headers = {"content-type" : "application/json"}

    req = requests.Session() # Create a Session

    # Create a Person

    params = {"name" : "Kinlani"}

    post_req = req.post(url , json =  params , headers = headers}
    res = post_req.json()

    # Getting a Person

    get_req = req.get(url+f"/{params.values()[0]/")
    res = get_req.json()

    # Updating a Person

    put_req = req.put(url + f"/Kinlani/" , json = {"name" : "Tunde"})
    res = put_req.json()


    # Deleting a Person
    del_req = req.delete(url + f"/Tunde/")
    res = del_req.json()

```


  

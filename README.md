# graphql-idors-sast

## Installation

- ```git clone https://github.com/grishxnder/graphql-idors-sast.git```
- ```cd graphql-idors-sast```
- ```You can make the venv (this is optional).```
- ```pip install -r requirements.txt```
- ```export FLASK_APP=app.py```

## Database
- Install the docker container with Postgres image or run it in your localhost.

## Usage

You can now test the simple web app: ```flask run```, go to the http://127.0.0.1:5000/ by the default.
If you go to the http://127.0.0.1:5000 you will see the DB Version test message.
  
Make the venv:
- ```python3 -m venv myapp```
- ```source myapp/bin/activate```

## Business flow

- You can set the cookie value in ```/setcookie?id={int_value}``` and check in ```/getcookie```
- Next, go to the graphql frontend in ```/graphql``` go to the settings tab and set ```"request.credentials": "include"``` 
- Try to do some queries.
- For ex. for create person with name = "name":
```
mutation mutation{
  createPerson(name: "name"){
      success
      errors
      person {
        id
        name
      }
  }
}
```
- In the response you can find your id - ```"id": "333",```
- Go to the ```/setcookie?id=333``` (check it in the ```/getcookie```)
- Then try to execute:
```
mutation mutation{
	createAccount(currency:USD balance: 123456, person_id: "333") {
    success
    errors
    account {
      id
      currency
      balance
      person_id
    }
  }
}
```
- Get the answer. Try to do the same query after /setcookie?id={int_value_not_equal_333} and get the Forbidden status
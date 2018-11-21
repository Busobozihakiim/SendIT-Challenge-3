# SendIT-Challenge-3
SendIT is an application that is used to create parcel delivery orders and this is its api.

## Installing
Clone or download this repository and move into the folder 
```
git clone https://github.com/Busobozihakiim/SendIT-Challenge-3/tree/develop
cd SendIT-Challenge-3
```
Then create a virtual environment and start it
```
virtualenv venv
source/venv/bin/activate
```

And finally install all the necessary dependencies
```
pip install -r requirements.txt
```

## Running
At the terminal type in
```
python run.py
```

Use the api endpoints with an app like [Postman](https://www.getpostman.com/apps) 

## Features
- `Register a user` Anybody should be able to create an account
- `Login to the api` Anyone with an account should be able to login
- `Create a parcel delivery order` User should be able to create a parcel delivery order
- `Get all parcel delivery orders` Admin should be able to fetch all delivery orders
- `Change Destination of a delivery order` User should be able to change a parcels destination
- `Change status of a delivery order` Admin should be able to change status to delivered
- `Change location of a delivery order` Admin should be able to change the location of a delivery order
- `Get a specific parcel delivery order` User should be able to fetch a delivery order by its id
- `Cancel a parcel delivery order` User should be able to cancel a delivery order by its id 
- `Get all parcel delivers by userid` User should be able to fetch all delivery orders by a userid

## Available API Endpoints
|  EndPoint  |  Functionality  | Accessible to | 
| ------------- | ------------- | -------------|
| POST /auth/signup | Register a new user | All |
| POST /auth/login | Logs in a user | All |
| POST /parcels | Create a parcel delivery order | Users  |
| GET /parcels  | Fetch all parcel delivery orders | Admin | 
| PUT /parcels/\<parcelId\>/destination | Change Destination of a delivery order | User |
| PUT /parcels/\<parcelId\>/status | Change the status of a delivery order | Admin | 
| PUT /parcels/\<parcelId\>/presentLocation | change the current location of a parcel delivery order | Admin |
| GET /parcels/\<parcel_id\>  | Fetch a specific parcel delivery order | Admin/User |
| GET /users/\<user_id\>/parcels | Fetch all parcel delivery orders by a specific user | User |
| PUT /parcels/\<parcel_id\>/cancel | Cancel the specific parcel delivery order | User
  
## Contributers
- Busobozihakiim


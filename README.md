# To use the code, you can follow these steps:

1.Install the required dependencies:
pip install flask
pip install flask-sqlalchemy


2.Download the code 

3.open xampp control panel or mysql workbrench

4.run the code 

5.export the task.sql database file in your mysql database

6.Run the app.py file
python app.py

7.The API should now be available at http://localhost:5000/. You can test the endpoints using a tool like curl or a REST client like Postman.

Here are some example curl commands that you can use to test the API:

To get all users:
curl http://localhost:5000/users

To get a specific user by ID:
curl http://localhost:5000/users

To get a specific user by ID:
curl http://localhost:5000/users/1

To get all orders:
curl http://localhost:5000/orders

To get a specific order by ID:
curl http://localhost:5000/orders/1

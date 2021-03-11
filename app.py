from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
import sqlalchemy as DB
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text

app = Flask(__name__)
app_1 = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost:5432/employees"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

engine = DB.create_engine(
    "mysql+pymysql://root:@localhost:3308/opsdashboard"
)
connection = engine.connect()
metadata = DB.MetaData()
census = DB.Table('employees', metadata, autoload=True, autoload_with=engine,
#    Column('mobile', String(10), primary_key=True),
#    Column('first_name', String(50)),
#    Column('last_name', String(50)),
#    Column('manager_name', String(50)),
#    Column('department', String(50))
   )

class EmployeeModel(db.Model):
    __tablename__ = 'employees'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    department = db.Column(db.String())

def __init__(self, first_name, last_name, department, email, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email
        self.user_id = user_id

def __repr__(self):
        return f"<Employee {self.first_name}>"


@app.route('/PostgreSQL', methods=['GET', 'POST'])
def employees():
    if request.method == 'GET':
        employee = EmployeeModel.query.all()
        results = [
            {
                "first_name": e.first_name,
                "last_name": e.last_name,
                "email": e.email,   
                "department": e.department
            } for e in employee]

        return {"employees": results}
    else:
        return {"error": "The request payload is not in JSON format"}

@app.route('/MySQL', methods=['GET'])
def MySqlemployees():
    if request.method == 'GET':
        # query = DB.select([employees])
        Results = connection.execute(text('SELECT * FROM employees'))
        FinalSet = Results.fetchall()
        results = [
            {
                "first_name": e.first_name,
                "last_name": e.last_name,
                "manager_name": e.manager_name,   
                "department": e.department,
                "mobile": e.mobile
            } for e in FinalSet]

        return {"employees": results}
    else:
        return {"error": "The request payload is not in JSON format"}
if __name__ == '__main__':
    app.run(debug=True)
import mysql.connector
import datetime


class con_db:
    def get_connect(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Priyan@07",
                database="hospital_db"
            )
            return self.con
        except Exception as e:
            return None


class PatientManager(con_db):

    def get(self):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()

            query = "select * from patient"

            self.cursor.execute(query)

            r = self.cursor.fetchall()

            print(r)

        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()

            query = """insert into patient
            (name, age, gender, mobile, email, disease, doctor, admission_date)
            values(%s,%s,%s,%s,%s,%s,%s,%s)"""

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)

            self.connect.commit()

            print("patient added successfully")

        except Exception as e:
            print(e)

    def get_one(self, id=None):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()

            query = "select * from patient where id=%s"

            values = (id,)

            self.cursor.execute(query, values)

            r = self.cursor.fetchone()

            return r

        except Exception as e:
            return None

    def dele(self, id=None):
        try:
            r = self.get_one(id=id)

            if r != None:

                self.connect = super().get_connect()
                self.cursor = self.connect.cursor()

                query = "delete from patient where id=%s"

                values = (id,)

                self.cursor.execute(query, values)

                self.connect.commit()

                print("patient deleted successfully")

            else:
                print("404")

        except Exception as e:
            print(e)

    def update(self, id=None, **kwargs):
        try:
            r = self.get_one(id=id)

            if r != None:

                self.connect = super().get_connect()
                self.cursor = self.connect.cursor()

                placeholder = ""

                for k in kwargs:
                    placeholder += k + "=%s, "

                placeholder = placeholder.rstrip(", ")

                query = f"update patient set {placeholder} where id=%s"

                values = [v for v in kwargs.values()]

                values.append(id)

                self.cursor.execute(query, values)

                self.connect.commit()

                print("patient updated successfully")

            else:
                print("404")

        except Exception as e:
            print(e)


patient = PatientManager()

# READ
# patient.get()

# CREATE
# patient.post(
#     name="Rahul",
#     age=25,
#     gender="Male",
#     mobile="9876543210",
#     email="rahul@gmail.com",
#     disease="Fever",
#     doctor="Dr. Anil",
#     admission_date=datetime.date.today()
# )

# READ ONE
# print(patient.get_one(id=1))

# UPDATE
# patient.update(
#     id=1,
#     disease="Viral Fever",
#     doctor="Dr. Arun"
# )

# DELETE
# patient.dele(id=1)
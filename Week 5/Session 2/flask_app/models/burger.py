from flask_app.config.mysqlconnection import connectToMySQL, DB

class Burger:
    def __init__(self , data):
        self.id = data["id"]
        self.name = data["name"]
        self.bun = data["bun"]
        self.meat = data["meat"]
        self.calories = data["calories"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Method that will get all rows of the table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        results = connectToMySQL(DB).query_db(query)
        burgers = []
        #  results = [
        # {'id': 1, 'name': 'Burger 1', 'bun': 'Bun 1', 'meat': 'Meat 1', 'calories': 5000, 'created_at': datetime.datetime(2023, 11, 21, 19, 48, 14), 'updated_at': datetime.datetime(2023, 11, 21, 19, 48, 14)}
        # , {'id': 2, 'name': 'Burger 2', 'bun': 'Bun 2', 'meat': 'Meat 2', 'calories': 3000, 'created_at': datetime.datetime(2023, 11, 21, 19, 51, 7), 'updated_at': datetime.datetime(2023, 11, 21, 19, 51, 7)}
        # ]
        for row in results:
            burger = cls(row)
            burgers.append(burger)
        # Burgers = [instance_1 , instance_2]
        return burgers


    # Method that will get one row by id
    @classmethod
    def get_by_id(cls , data):

        """
            data = {'id': x}
        """

        query = "SELECT * FROM burgers WHERE id = %(id)s"
        results = connectToMySQL(DB).query_db(query , data)
        # results = []
        # results = [{...}]
        burger = None
        if results != []:
            burger = cls(results[0])
        return burger


    # Method that will insert a row to the table
    @classmethod
    def create(cls, data):
        query = "INSERT INTO burgers (name , bun , meat , calories) VALUES (%(name)s , %(bun)s , %(meat)s , %(calories)s);"
        results = connectToMySQL(DB).query_db(query , data)
        return results



    # Method that will update a certain row by id
    @classmethod
    def update(cls , data):
        query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)


    # Method that will delete a certain row by id
    @classmethod
    def delete(cls , data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return results
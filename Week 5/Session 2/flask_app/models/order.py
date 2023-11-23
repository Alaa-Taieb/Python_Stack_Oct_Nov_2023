from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models.burger import Burger

class Order:
    def __init__(self , data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.quantity = data['quantity']
        self.order_date = data['order_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.burger = None

    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM orders JOIN burgers ON orders.burger_id = burger_id WHERE orders.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        print("*"*50)
        print(result)
        order = None
        if result != []:
            order = cls(result[0])
            # Create an instance of the burger that was passed in result
            burger_data = {
                'id': result[0]['burgers.id'],
                'name': result[0]['name'],
                'bun': result[0]['bun'],
                'meat': result[0]['meat'],
                'calories': result[0]['calories'],
                'created_at': result[0]['burgers.created_at'],
                'updated_at': result[0]['burgers.updated_at'],
            }
            order.burger = Burger(burger_data)
        return order
    
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders JOIN burgers ON orders.burger_id = burger_id;"
        results = connectToMySQL(DB).query_db(query)

        orders = []
        if results != []:
            for row in results:
                order = cls(row)

                burger_data = {
                    'id': row['burgers.id'],
                    'name': row['name'],
                    'bun': row['bun'],
                    'meat': row['meat'],
                    'calories': row['calories'],
                    'created_at': row['burgers.created_at'],
                    'updated_at': row['burgers.updated_at'],
                }

                order.burger = Burger(burger_data)
                orders.append(order)
        return orders
    
    @classmethod 
    def create(cls , data):
        query = "INSERT INTO orders (customer_name, quantity, order_date, burger_id) values(%(customer_name)s , %(quantity)s, %(order_date)s ,%(burger_id)s);"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def delete(cls , data):
        query = "DELETE FROM orders WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def update(cls , data):
        query = "UPDATE orders SET customer_name = %(customer_name)s , quantity = %(quantity)s , order_date = %(order_date)s , burger_id = %(burger_id)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)

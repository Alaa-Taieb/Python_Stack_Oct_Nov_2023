from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Event:
    db_name = "ajax_demo"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM events"

        results = connectToMySQL(cls.db_name).query_db(query)
        all_posts = []
        for result in results:
            all_posts.append(cls(result))
        return all_posts

    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM events WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query , data)

        event = None
        if results:
            event = cls(results[0])
        return event

    @classmethod
    def add(cls, data):
        query=  "INSERT INTO events(title) "\
                "VALUES(%(title)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def reset(cls):
        query = "DELETE FROM events"
        return connectToMySQL(cls.db_name).query_db(query)
    
    def __iter__(self):
        # {'id': self.id , 'title': self.title , 'created_at': self.created_at , 'updated_at': self.updated_at}
        # In Python, yield is used to create generators, which are functions that return values one at a time instead of all at once. This makes them memory-efficient for iterating over large sequences. When a generator function encounters yield, it temporarily pauses execution, sends the yielded value back to the caller, and remembers its state. The next time the generator is called, it resumes execution from the point where it left off. This allows generators to be used in loops like any other iterable, but without needing to store the entire sequence in memory at once.
        yield 'id', self.id
        yield 'title', self.title
        yield 'created_at', self.created_at
        yield 'updated_at', self.updated_at

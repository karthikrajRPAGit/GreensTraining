Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Importing flask module in the project is mandatory
... # An object of Flask class is our WSGI application.
... from flask import Flask
...  
... # Flask constructor takes the name of 
... # current module (__name__) as argument.
... app = Flask(__name__)
...  
... # The route() function of the Flask class is a decorator, 
... # which tells the application which URL should call 
... # the associated function.
... @app.route('/')
... # ‘/’ URL is bound with hello_world() function.
... def hello_world():
...     return 'Hello World'
...  
... # main driver function
... if __name__ == '__main__':
...  
...     # run() method of Flask class runs the application 
...     # on the local development server.

### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Javascript is mostly used for client side scripting.	Python is generally used for server side scripting.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  1.)get(key,def_val)
  2.)setdefault(key, def_value)

- What is a unit test?
A unit test is a way of testing a unit - the smallest piece of code that can be logically isolated in a system

- What is an integration test?
Integration testing is the testing of multiple components of the application to check that they work together. 

- What is the role of web application framework, like Flask?
 To provide you with tools, libraries and technologies that allow you to build a web application.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  use the route for the object itself

  use query string parameters if you are describing the object you are on 

- How do you collect data from a URL placeholder parameter using Flask?
You can specify the variable in the app.route and then use that variable as a paramater in the routing function

- How do you collect data from the query string using Flask?
With a query string the data can be found in the request.args dictionary

- How do you collect data from the body of the request using Flask?You can get the data form a post request in the body using the request.form dictionary

- What is a cookie and what kinds of things are they commonly used for?
Cookies are text files with small pieces of data
Cookies are most commonly used to track website activity

- What is the session object in Flask?
In the flask, a session object is used to track the session data

- What does Flask's `jsonify()` do?
jsonify turns a python object into a Werkzeug/Flask response object. You can use this with plan Flask to return a JSON response.
**Django User Activity Logger**

A simple Django project that demonstrates how to use middleware to log user activity. The project logs each incoming HTTP request, including the IP address, URL accessed, and timestamp of the request.


**Features**
* Logs user IP addresses and the URLs they visit.
* Middleware intercepts each request and logs details into the database.
* View the logged activity in the Django admin panel.
* Simple pages like Home, About, and Contact for testing middleware.


**Project Functionality**
Middleware: The custom middleware logs user requests, including their IP address, visited URL, and the time of access.
Admin Panel: View the logs through the Django admin interface.
Simple Views: The project includes basic pages such as Home, About, and Contact to test the logging functionality.


**Architecture**
Custom Middleware (LogMiddleware): Captures request data and stores it in the ActivityLog model.
ActivityLog Model: A simple model designed to store user activity, including the following fields:
ip_address: Stores the user's IP address.
url: Stores the full URL that was accessed.


**Middleware Functionality**
**Logging Process**
The custom middleware LogMiddleware is added to the MIDDLEWARE setting in settings.py. It intercepts each request, logs the request metadata (IP address, URL, and timestamp), and stores it in the ActivityLog model.


**Here’s how it works**
Request Interception: Each time a request is made to the server (e.g., visiting a page), the middleware captures the request before passing it to the corresponding view.


**Logging Information**
* The IP address is obtained from request.META.get('REMOTE_ADDR').
* The URL is obtained from request.build_absolute_uri().
* The timestamp is automatically recorded when the entry is saved in the database.
* Database Storage: The captured data is stored in the ActivityLog model, where each request is logged as a separate entry.
* timestamp: Automatically records the time the request was made.
* Simple Views: Three basic views (Home, About, Contact) to simulate user activity across different pages.


**Requirements**
To run this project, you'll need:
* Python,
* Django,


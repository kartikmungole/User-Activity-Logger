**Django User Activity Logger**
A simple Django project that demonstrates how to use middleware to log user activity. The project logs each incoming HTTP request, including the IP address, URL accessed, and timestamp of the request.

**Features**
Logs user IP addresses and the URLs they visit.
Middleware intercepts each request and logs details into the database.
View the logged activity in the Django admin panel.
Simple pages like Home, About, and Contact for testing middleware.

**Project Functionality**
Middleware: The custom middleware logs user requests, including their IP address, visited URL, and the time of access.
Admin Panel: View the logs through the Django admin interface.
Simple Views: The project includes basic pages such as Home, About, and Contact to test the logging functionality.

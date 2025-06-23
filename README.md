# stock-analyses-py
stock analyses python and tensorflow with PyQt5
First page
either login page or sign up page
when user click on sign up, it will direct user to the sign up page. where user can enter their first name, last name, password, age and email. if user is less 18, it will prompt an error message and won't continue to save the data entered. However if the user is more than or equal to 18, it will stored the data in users.txt file as username = firstname+lastname, password and email
when user want to login. The system will check the users.txt file, for username as index 0 and for password as index 1. if matched it will allow the user to sign in else the username can't be able to sign in.
in homepage, user can choose either to search or logout. Logout will close the windown using self.close(). When user choose searchpage it will direct user to the search page.
in search page user can search the companies value using the search bar above. Here it will load the data in yfinance which also known as yahoo finance. If data is found it will continue with the analyses. However, if data is not found it will prompt an error message. 
When predictions is made, it will release the RMSE value. this value is very important in stocks analyses as it check whether the result is accurate or not. and also the latest prediction closing price. 

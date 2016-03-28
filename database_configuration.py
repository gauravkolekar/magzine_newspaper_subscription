import MySQLdb
database_configuration = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="password", db="subscriptiondb")
#creating a configuration file which can be changed as per the user of the program and their paramters

import csv
#import MySQLdb
import pymysql as sql

def getDBConnCursor():
    mydb=sql.connect(host='localhost',user='root',password='vedula', db='loans')
    cursor=mydb.cursor()
    cursor.execute("Select * from cust_loans")
    store_result = cursor.fetchall()
#myConnection.close()

# Print the result of the query
    print(store_result)
def LoadLoanMDdata():
    pass



def ChangeLoanMDdata():
    pass


def ActivateLoanMDData():
    pass


def DeactivateLoanMDdata():
    pass


def GetAllLoanMDdata():
    pass


def GetloanMDbyCreditScore():
    pass


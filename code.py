from datetime import date,timedelta
import datetime

a={'cust1':[(2019,5,12),(2019,6,24),(2018,2,11),(2018,8,13)],
   'cust2':[(2018,8,13),(2020,8,25),(2019,10,21)],
   'cust3':[(2017,7,25),(2018,8,25),(2019,1,5)],
   'cust4':[(2018,6,4),(2019,12,12),(2020,5,14),(2020,8,7)]}

b={'cust1':[(2017,12,12),(2019,1,24),(2020,8,25)],
   'cust2':[(2018,9,24),(2017,8,15)],
   'cust3':[(2019,11,7)],
   'cust4':[(2021,1,12),(2020,4,24)]}

def print_data():
    for i in a.keys():
        print("Customer name:",i,"\n","Purchased date:",(a[i]))
    


def find(name):
    if name in a:
        year = int(input("\nEnter the year:"))
        month = int(input("Enter the month:"))
        day = int(input("Enter the day:"))
        l=(year,month,day)
        date2=date(year,month,day)
        for i in a[name]:
            if i==l:
                mini=1000
                newdate=i
                for j in b[name]:
                    d=str(j)
                    e=d.split(",")
                    ss=e[0].replace("(","")
                    dd=e[2].replace(")","")
                    year1=int(ss)
                    month1=int(e[1])
                    day1=int(dd)
                    date1=date(year1,month1,day1)
                    if(date2>date1):
                        new_date=(date2-date1).days
                        if new_date<mini:
                            mini=new_date
                print(mini,"days")
           
    else:
        print("Invalid customer name")
        
                  


print_data()
name= str(input("\nEnter name:"))
find(name)
           

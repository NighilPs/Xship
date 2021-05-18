from datetime import datetime

purchased_list = [
{'Cust1':'12/5/2019'},
{'Cust1':'24/6/2019'},
{'Cust1':'11/2/2018'},
{'Cust1':'13/8/2018'},
{'Cust2':'13/8/2018'},
{'Cust2':'25/08/2020'},
{'Cust2':'21/10/2019'},
{'Cust3':'25/07/2017'},
{'Cust3':'25/08/2018'},
{'Cust3':'05/01/2019'},
{'Cust4':'04/06/2018'},
{'Cust4':'12/12/2019'},
{'Cust4':'14/05/2020'},
{'Cust4':'07/08/2020'},
]


key_list = [
{'Cust1':'12/12/2017'},
{'Cust1':'24/01/2019'},
{'Cust1':'25/08/2020'},
{'Cust2':'24/09/2018'},
{'Cust2':'15/08/2017'},
{'Cust3':'07/11/2019'},
{'Cust4':'24/04/2020'},
{'Cust4':'12/01/2021'},
]

for list1 in purchased_list:
    for data1 in list1:
        purchase_date=datetime.strptime(list1[data1],'%d/%m/%Y').date()
        c=[]
        for list2 in key_list:
           for data2 in list2:
                if data2==data1:
                    
                    
                    key_date=datetime.strptime(list2[data2],'%d/%m/%Y').date()
                    if purchase_date>key_date:
                        c.append(key_date)
        if not c :
            print("Null")
        else:
            nearest_date=min(c, key=lambda sub:abs(sub-key_date))
            print((purchase_date-nearest_date).days)

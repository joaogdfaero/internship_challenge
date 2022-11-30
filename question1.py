def find_underpaid(list): # -> function to find and print employes with more than 3 years with a salary below the average
    # calculates average
    sum = 0
    for i in range(0,len(list1)):
        sum = sum + list1[i][1]
    average = sum/len(list1)
    
    # iterate to print employees with more than 3 years with a salary below the average
    for i in range(0,len(list1)):
        if(list1[i][1] < average and list1[i][2]>3 ): #if salary is below average AND employee is with the company for more than 3 years than:
            print(list1[i][0]) # print employer's name
    

# input
list1 = [["Bruno", 1700.00, 3], ["Leonardo", 1400.23, 1], ["Juan", 1561.12, 2], ["Juliana", 1660.07,3], ["Wagner", 1841.92, 5], ["Micaela", 2000.00, 1], ["Bento", 1750.87, 4], ["Lucia", 1600.55,1], ["Pedro", 1690.00, 4], ["Carla", 1580.00, 6]]

# calling function
find_underpaid(list1)
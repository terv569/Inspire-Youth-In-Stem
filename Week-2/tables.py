#import module
from tabulate import tabulate

# assign data
mydata = [                                                             


    ["Yves", "Jean"] ,
    ["Claude", "Fabian"] ,
    ["Christophe", "Laurent"] ,
    ["Alexandre", "Pierre"] ,
]

#create header
head = ["Name" , "City"]


# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))































pip-installer.Enable:





l1=[
    {
        'name':"asif",
        'f_name':"azam",
        "subjects" : [ 
            "Eng", "Math"
         ],
        "classes":[
            "1st", "2nd"
        ],
        "contacts":{ 
            "personal" : "23223",
            "official" : "34234234" 
        }
    },
    {
        'name':"abubakar",
        'f_name':"ATA",
        "subjects" : [ 
            "Sci", "Urd"
        ],
        "classes":[
            "1st", "2nd"
        ],
        "contacts":{ 
            "personal" : "23223",
            "official" : "34234234" 
        }
    }
    ]


# print(d1['a'])
# print(type(l1[0]))
for i in l1:
    print(i['contacts']['personal'],'\n')
    break
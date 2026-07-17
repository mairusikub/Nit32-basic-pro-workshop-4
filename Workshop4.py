gang_members = []
def add_members(name,age,gang,list):
    member ={
            "name":name,
            "age":age,
            "gang":gang,
        }
    
    return list.append(member)


while True :
    memberr = (input("1เพิ่มสมาชิก,2ดูสมาชิกทั้งหมด,3อย่างอื่น(ออก)"))
    if  memberr == 1 :
        name = (input("กรอกชื่อนะ"))
        age  =(int(input("อายุเท่าไหร่")))
        gangname = (input("ชื่อเเก๊ง"))
        add_members(name,age,gangname,gang_members)
    elif memberr == 2:
        print(gang_members)
    else :
        print ("ออกจากระบบ")
        break




        
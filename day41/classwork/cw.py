# 1
# 1)შექმენით სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიის ბოლოში დაამატე სიტყვა --> "ianvari" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა
lst = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]
lst.append("ianvari")
print(lst)


# 2
# 2)შექმენი სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიაში მეორე ინდექსზე დაამატე სიტყვა ---> "bati" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა
lst = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]
lst.insert(2, "bati")
print(lst)

# 3

# 3)შექმენი სია ---->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე მე 5 ინდექსზე მდგომი ელემენტი და დაპრინტე საბოლოო სია ნახე ამოიშალა თუ არა
lst = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]
lst.pop(5)
print(lst)

# 4
# 4)შექმენი სია --->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე True და ასევე ამოშალე "kote" და დაპრინტე საბოლოო სია და ნახე ამოიშალა თუ არა
lst = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]
lst.remove(True)
lst.remove("kote")
print(lst)
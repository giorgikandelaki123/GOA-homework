x=int(input())
y=int(input())
print(x>y)
print(x<y)
print(x==y)



a="4"
b="5"
c="6"
e=2
d=1
a=int(a)
b=int(b)
c=int(c)
print((a*b*c*e*d)/5)


x=input()
y=input()
z=input()
e=int(input())
d=x+y+z
print(e*d)

# ჩვენ ვისწავლეთ and და or. and-ს ვიყენებთ როცა ორივე პირობა შესრულებულია 
# და or-ს ვიყენებთ როცა ერთი მაინც არის შესრულებული

         #and                                                                                #or
# True and  True    True    რადგან ორივე შედეგი არის true                          True or True    True   რადგან ორივე პირობა არის true       
# True and  False   False   რადგან ერთი პირობა არ არის შესრულებული               True or False   True   რადგან ორივე პირობა არის შესრულებული
# False and True  False     რადგან ერთი პირობა არ არის შესრულებული               False or True   True   რადგან ორივე პირობა არის შესრულებული
# False and False  False    რადგან ორივე პირობა არის false                         False or False  False   რადგან ორივე პირობა არის false



x=30
print(x>10 and x>2)

y=20
print(y>10 or y<19)


a="giorgi"
b=20
c=30.7
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


s=input("gamarjoba giorgi")
c=int(input("enter your age"))
l=float(input("enter your height"))
print(s)
print(c)
print(l)
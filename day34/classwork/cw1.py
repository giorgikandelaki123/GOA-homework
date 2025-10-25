#1
text = input("შეიყვანე სიტყვა ან ტექსტი: ")


length = len(text)
print("ტექსტის სიგრძე:", length)

print("სიმბოლოები ინდექსებით:")
for i in range(length):
    print(i, ":", text[i])



#2
words = ["sun", "moon", "earth", "sky", "tree"]
for word in words:
    length = len(word)
    print("სიტყვა:", word, "შედგება", length, "სიმბოლოსაგან")

    if length % 2 == 0:
        print("ლუწია")
    else:
        print("კენტია")
    
    print()
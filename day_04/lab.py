user = {
"name": input("what is your name?"),
"age": int(input("what is your age?")),
"multilingual": input("do you speak more than one language? (yes/no)")
    }
print(f"Hello, {user['name']}!")
if user['age']<=18:
    print("You can't vote!")
elif user['age']<=25:
     print("You can't rent a car!")
elif user['age']>=35:
        print("You are old sry")
if user['multilingual']=="yes":
    num_languages=int(input("how many languages do you speak?"))
    for i in range(num_languages):
        language=input("what is one of the languages you speak?")
        print(language)
else:
    language=input("what language do you want to learn?")
    print(language+" is a great language to learn!")
more_info=input("do you want to input more information?")
if more_info=="yes":
    hobby=input("what is your favorite hobby?")
    print(hobby+" sounds fun!")
    location=input("where do you live?")
    print(location+" is a nice place.")
    user.update({"hobby": hobby, "location": location})
print("Here is the information you provided:")
print(user)
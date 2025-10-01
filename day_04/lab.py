userinfo=[]
while True:
    username=input("Enter a username. Enter 'q' to quit: ")
    if username != 'q':
        user = {
        "name": username,
        "age": int(input("what is your age?")),
        "multilingual": [input("are you multilingual? (yes/no)")],
            }
        userinfo.append(user)
        print(f"Hello, {user['name']}!")
        if user['age']<=13:
            print("you can't sit in the passenger seat")
        if user['age']<=18:
            print("You can't vote")
        if user['age']<=25:
            print("You can't rent a car")
        if user['age']>=35:
                print("You are old sry")
        if "yes" in user['multilingual']:
            user['multilingual']=["Yes, they know: "]
            num_languages=int(input("how many languages do you speak?"))
            for i in range(num_languages):
                language=input("what is one of the languages you speak?")
                print(language)
                user['multilingual'].append(language)
        else:
            language=input("what language do you want to learn?")
            print(language+" is a great language to learn!")
            user['multilingual']=[]
            user['multilingual'].append(f"No, but they want to learn {language}")
        more_info=input("do you want to input more information?")
        if more_info=="yes":
            hobby=input("what is your favorite hobby?")
            print(hobby+" sounds fun!")
            location=input("where do you live?")
            print(location+" is a nice place.")
            user.update({"hobby": hobby, "location": location})
    else:
        break
print("Here is the information you provided for all users:")
print(userinfo)
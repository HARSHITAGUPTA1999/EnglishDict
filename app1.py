
#interactive english dictionary 
# to clear terminal : ctrl + shift + P --> terminal : clear
# press ctrl+c to stop an infinte loop
# we are going to use a json file
import json

# to check for similar closely related words and suggest it to the user we use the following library
from difflib import get_close_matches

# we import pyttsx3 --> module for text-->speech conversion
import pyttsx3 as tts
# we create an instance to initialsie the package
engine = tts.init()
#first thing is to load the json fille 
#data is a file object : type = dict --> means key and value pairs
data = json.load(open(r"data_app1.json"))


def eng_definition(w):
    
    # lower() converts any type of string to all lowercase
    w = w.lower()
    if w in data:
        return data[w]
    # title() coverts the first char of string to captial eg: "silly me" ---> "Silly Me"
    elif w.title() in data:
        return data[w.title()]
    # capitalize() coverts the first char of string to captial eg: "silly me" ---> "Silly me"
    elif w.capitalize() in data:
        return data[w.capitalize()]
    # upper() converts str to all uppercase
    elif w.upper() in data:
        return data[w.upper()]
    # check if the user meant some other similiar word 
    # if list is not empty means we got a similar word
    elif len(get_close_matches(w,data.keys(),3,0.8)) > 0:
        input_mssg = "Did you mean %s instead?.Press Y for yes .Press N for no." % get_close_matches(w,data.keys(),3,0.8)[0]
        engine.say(input_mssg)
        engine.runAndWait()
        yn=input(input_mssg)
        
        if yn=="Y":
            # we return the definition of the correct word if user enters Y
             return data[get_close_matches(w,data.keys(),3,0.8)[0]]
        
        elif yn =="N":
            # word does not exist if user enters N
            return "Please double check the word.It does not exist in our dictionary."
        
        else:
            # if user enters anything random except for Y or N
            return "We did not understand your query!"
        
    else:
        return "Such word does not exist in our dictionary, Please double check the word."

#user enters a word
while True:
    engine.say("Welcome,PLease enter a word")
    engine.runAndWait()
    word =(input("Enter a word:"))
    word_inputed = "You have entered %s"% word
    engine.say(word_inputed)
    engine.runAndWait()
    engine.say("Press Y if you want to continue,Press N to enter another word")
    engine.runAndWait()
    yn_for_input = input("Press Y if you want to continue,Press N to enter another word")
    if(yn_for_input == 'Y'):
    #print the definition of the word entered by the user
    #print(eng_definition(word))  --> we dont want the square bracket to show up . so we optimise 
    # how we print the output
        ans = eng_definition(word)
        
    elif(yn_for_input == 'N'):
        continue
    else:
        print("Please check your input again")
        engine.say("Please check your input again")
        engine.runAndWait()



    #we traverse the list to print the output
    i = 1
    if type(ans) == list:
        for item in ans:
        
            order = "Definition number %s is," % i
            engine.say(order)
            engine.runAndWait()
            print(item)
            engine.say(item)
            engine.runAndWait()
            i +=1
    else:
        # type(output) is a string
        print(ans)
        engine.say(ans)
        engine.runAndWait()



# write a function called SPEAK that accepts a single parameter, animal


def speak (animal="dog"):
    noise = {
        "dog" : "woof", 
        "pig" : "oink", 
        "duck" : "quack",
        "cat" : "meow"
    }
    if animal in noise: 
        return noise[animal]
    return "?"

# print(speak ())
# print (speak("pig"))
# print (speak("banana")) 
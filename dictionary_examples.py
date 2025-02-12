d = {} # empty dictionary
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
eng_to_spa["i"] = "yo"
eng_to_spa["am"] = "soy"
eng_to_spa["spanish"] = "espanol"
print(eng_to_spa)
sentence = "i am spanish"
words = sentence.split()
for word in words:
    print(eng_to_spa[word])
eng_to_spa.update({"yes": "si", "no": "no"}) #updating a dict with a new dict
print(eng_to_spa)
del eng_to_spa["no"] #how to delete a key/value from dict
print(eng_to_spa)

eng_to_spa.popitem() #how to delete the last item in a dict
print(eng_to_spa.pop("two")) #deleting a specific item in the dict

if "tree" in eng_to_spa:
    print(eng_to_spa["tree"])
else:
    print("i dont know that word")


print(eng_to_spa.get("tree", "unknown word"))#does the if else short function above

for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")

for key, value in eng_to_spa.items(): #same as above but simpler
    print(f"{value} means {key}")
#Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
# import random


# Subject = ["I", "You"]
# Verb = ["Play", "Love"] 
# Object = ["Hockey","Football"]

# print(random.choice(Subject) + random.choice(Verb)+ random.choice(Object))


subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[k], verbs[j], objects[i])
            print(sentence)
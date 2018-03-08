a = [12, "I", 18, "am", 2, "a", 10, "ninja"]
question = "Who are you?"
x = 0
for i in range(len(a)):
    if isinstance(a[i], str):
        question += " " + a[i]
    elif isinstance(a[i], int):
        x += a[i]

print question + "."
print x

if type(a) == list and str and int:
    print "mixed"
elif type(a) == list and str:
    print "strings"
else:
    print "integers"


        



#! /usr/bin/env python

# DB: I couldn't figure out why I was having trouble with the inputs for your scripts, but
#     it was because you used /usr/bin/python in your shebang line. For me, that calls 
#     version 2, while /usr/bin/env python calls version 3. Maybe stick with the latter
#     because it should be more robust across different systems.

mystring = input("Enter Your DNA Sequence: ")
#converts to lowercase
mystring = mystring.lower()
#makes complimentary strand
mystring = mystring.replace("c", "G")
mystring = mystring.replace("g", "C")
mystring = mystring.replace("a", "T")
mystring = mystring.replace("t", "A")
#print reverse order
print("Your reverse complimentary DNA Sequence is: ")
print(mystring[::-1])

# DB: Overall, good! In general, for aesthetics, I'd suggest adding spaces between lines.
s = "Monty Python"
print(s[0:4]) #s sub 0 sub 4
#goes up to and not including 4
print(s[6:7])
print(s[6:20]) #no traceback even though there's not 20 characters

s = "Margie Blair"
print(s[: 2])
print(s[8:])
print(s[:])

if 'gie' in s:
    print('Found it!') 

legalname = s.replace('Margie', "Marguerite")
print(legalname)

#lstrip takes whitepsace off the left, rstrip() takes whitespace off the right
#strip takes whitespace off the beginning and end

#line.startwith('P') returns a Boolean

data = 'sent from marguerite.blair@gmail.com '
atpos = data.find('@') #returns the index where the @ sign starts
sppos = data.find(' ', atpos)
host = data[atpos+1:sppos]
print(host)
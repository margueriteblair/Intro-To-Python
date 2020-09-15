#in elifs there's multiple ways to get this shit done!
x = 20
if x < 2:
    print('small')
elif x < 10:
    print('medium')
else: 
    print('LARGE')
print('All done')

#the else statement is left as a catch all for those that weren't matched
#try/except structure
#you surround a dangerous section of the code with try and except
#if the try works then the except is skipped
#if the try fails, it jumps to the except section

astr = "Hello Bob"
try:
    istr = int(astr)
except: 
    istr = -1
print('First', istr)

astr = '123'
try: 
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

#Python try-catch is a try-except
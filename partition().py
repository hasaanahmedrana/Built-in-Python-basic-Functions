# PARTITION()
'''
Divides the given string into a three-element tuple by locating the specified string (from the left by default).

SYNTAX: string.partition('stringpart')
'''

s = ' hey how you doing cutie?'
result = s.partition('you')
print(result)
print(result[1])
print(list(result))
print('-'*50)

result = s.partition('cutie?')
print(result)
print('-'*50)
# r-PARTITION()
'''
Divides the given string into a three-element tuple by locating the specified string from the right.

SYNTAX: string.rpartition('stringpart')
'''

s = ' hey how you doing you cutie?'
result = s.rpartition('you')
print(result)
print(result[1])
print(list(result))
print('-'*50)

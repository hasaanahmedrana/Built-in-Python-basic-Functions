'''
-----: REPLACE FUNCTION :------
This function is used to replace the specific part of the string(substring)
withthe new part*(substring).


SYNTAX : string.replace(old, new, count)
    Here,
    old:   The substring you want to replace.
    new:   The substring that will replace occurrences of the old substring.
    count: number of substrings you want to replace
           and it is optional, by default it means all'''


#EXAMPLE-1
s = 'hello world'
print(s.replace('o','M',1))

#EXAMPLE-2
name = 'hasaaaan'
name = name.replace('aaa','a')
print(name)

#EXAMPLE-3
greet = 'hey how you doin?'
greet = greet.replace('hey','Hello!')
print(greet)


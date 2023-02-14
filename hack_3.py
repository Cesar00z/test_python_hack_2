"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(str):
    result = str
    #...
    change = {"a":"@", "e":"3", "i":"¡", "o":"0", "u":"v"}
    length = len(result)
    
    if len(result) >= 3:
        for old, new in change.items():
            length = len(result) - 1
            last_letter_upper = result[-1].upper()
            result = result[0].upper() + result[1:length].replace(old,new) + last_letter_upper
    
    elif len(result) < 3:
        first_letter = result[0].upper()
        for old, new in change.items():
            for letter in result:
                if letter in change.values() or letter == "u":
                    result = first_letter + letter.lower().replace(old,new)
   
                else:
                    result = first_letter + letter.upper().replace(old,new)

    return result

print(fn_hack_3("3q"))
"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(str):
    result = str
    #...

    new_str = ""

    if len(result) % 2 == 0 and len(result) > 2:
        for n in range(0, len(result)):
            if n == 1:
                new_str = new_str + result[n].upper()
            elif n == 2:
                new_str = new_str + result[n].lower()
            
            elif result[n] == "i":
                new_str = new_str + result[n].upper()
            else:
                new_str += result[n]
            
    elif len(result) % 2 == 1:
        for n in range(0, len(result)):
            if result[n] == "u":
                new_str = new_str + result[n].upper()
            else:
                new_str += result[n]
    
    elif len(result) % 2 == 0 and len(result) >= 2:
        for n in result:
            new_str = new_str + n.lower()
            
    return new_str
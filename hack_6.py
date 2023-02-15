"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(str):
    result = str
    #...

    dash = "-"
    if result:
        for i in range(len(result)):
            if "a" in result:
                
                result[i] = "1"
            
            elif "b" in result:
                result[i] = dash
            
            elif "c" in result:
                result[i] = "3"

            elif "d" in result:
                result[i] = dash
            
            elif "e" in result:
                result[i] = "5"
    else:
        result.append("0")
    return result

print(fn_hack_6(["a","b","c","d","e"]))
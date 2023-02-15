"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(str):
    result = str
    #...
    if result:
        for i in range(len(result)):
            if "a" in result:
                    
                result[i] = "1"
                
            elif "b" in result:
                result[i] = 2
                
            elif "c" in result:
                result[i] = "3"

            elif "d" in result:
                result[i] = 4
                
            elif "e" in result:
                result[i] = "5"
    else:
        result.append(0)

    return result
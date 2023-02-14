"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(str):
    result = str
    #...
    if len(result) > 3:
        result = result[1:len(result) - 1]

    return result

print(fn_hack_4("qux"))
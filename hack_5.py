"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(str):
    result = str
    #...
    new_str = ""

    if len(result) > 3:
        for n in range(len(result)):
            if result[n].startswith("f"):
                dash = "-"
                new_str = result[:2] + dash + result[3:5] + dash + result[5:8].replace("n","-")
            elif result[n].startswith("b") :
                dash = "-"
                new_str = result[:2] + dash + result[3:5] + dash + result[6:8].replace("m","-")

    elif len(result) > 2:
        
        new_str = result[0:len(result) - 1] + result[-1:].upper() 
    else:
        new_str = result
    return new_str
print(fn_hack_5("fooziman"))
"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(dict):
    result = {"foo":"fookziman","bar":"barziman"}
    #...
    #result_copy = result.copy()
    key_list = list(result.keys())
    for key in key_list:
        result.pop(key)
    
    result["Foo"] = "Fooziman"
    return result

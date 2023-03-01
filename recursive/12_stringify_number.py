# stringify number

def stringify_number(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            # print(newObj[key])
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringify_number(newObj[key])
    return newObj


obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

print(stringify_number(obj))

# result
# {'num': '1',
#  'test': [],
#  'data': {'val': '4',
#           'info': {'isRight': True, 'random': '66'}
#           }
#  }

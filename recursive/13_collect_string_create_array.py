# collect string solution


def collect_string_to_object_make_it_array(obj):
    result_array = []
    for key in obj:
        if type(obj[key]) is str:
            result_array.append(obj[key])
        if type(obj[key]) is dict:
            result_array += collect_string_to_object_make_it_array(obj[key])
    return result_array



obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(collect_string_to_object_make_it_array(obj)) # ['foo', 'bar', 'baz'])

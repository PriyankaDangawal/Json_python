import json
def complex_number(objects):
    if "complex" in objects:
        return complex(objects['real'],objects['img'])
    return objects
complex_object=json.loads('{"real":4,"img":5}')
print(complex_number(complex_object))
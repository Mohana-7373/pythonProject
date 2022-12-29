import json
cars= {
    "manufacturers":[
        "Cadillac","chevrolet", "BMW"
    ]
}
print(json.dumps(cars,indent=4))
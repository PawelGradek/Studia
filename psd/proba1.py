import json

f = open("C:\\Users\\Lenovo\\PycharmProjects\\psd\\customer_transaction.json", "r")
data = json.load(f)
f.close()
data['myszka'].append(789)


g = open("C:\\Users\\Lenovo\\PycharmProjects\\psd\\customer_transaction.json", "w")
json.dump(data, g)
g.close()

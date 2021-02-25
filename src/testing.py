from json import loads

with open("C:\Projects\lgbtq_final\lgbtqp_banned_places\src\hate.json", "r") as f:
    j = loads(f.read())

keys = j.keys()

print(len(keys))
def tickets(people):
    pocket = {"25":0, "50":0 }
    for num in people:
        if num == 25:
            pocket["25"] += 1
        elif num == 50 and pocket["25"]:
            pocket["50"] +=1
            pocket["25"] -= 1
        elif num == 100 and pocket["50"] and pocket["25"]:
            pocket["50"] -= 1
            pocket["25"] -= 1
        elif num == 100 and pocket["25"] > 2:
            pocket["25"] -= 3
        else:
            return "NO"
    return "YES"

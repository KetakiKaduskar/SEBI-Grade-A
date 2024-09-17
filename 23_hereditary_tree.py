def getOrderOfSuccession(famTree, currMember):
    order = [currMember]
    sons = famTree.get(currMember, [])

    for son in sons:
        order.extend(getOrderOfSuccession(famTree, son))

    return order

inpList = []
broList = []
while True:
    inp = input()
    if inp == "":
        break
    inpList.append(inp)

famTree = {}
for elem in inpList:
    if "'s sons: " in elem:
        par, child = elem.split("'s sons: ")
        childList = child.split(",")
        famTree[par] = childList
    elif "'s son: " in elem:
        par, child = elem.split("'s son: ")
        childList = child.split(",")
        famTree[par] = childList
    elif "'s brothers: " in elem: 
        mem, bro = elem.split("'s brothers: ") 
        broList.extend(bro.split(","))
    else: 
        broList.append(elem)

king = broList[0]
successionOrder = getOrderOfSuccession(famTree, king)

for bro in broList:
    if bro != king:
        successionOrder.extend(getOrderOfSuccession(famTree, bro))

print(successionOrder)
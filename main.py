import json
import argparse
arg_parser = argparse.ArgumentParser( description = "Configuration file" )
arg_parser.add_argument("config_file")
arguments = arg_parser.parse_args()
config_file = arguments.config_file

f = open(config_file)
config = json.load(f)
print(config[0]["gameIntro"])


def findSceneIndex(config, sceneId):
    for ind,scene in enumerate(config):
        if config[ind]['sceneId'] == sceneId:
            return ind
    return -1

def getAction(userInput):
    newInput = userInput.split(' ')
    return newInput[0]

def getObject(userInput):
    newInput = userInput.split(' ')
    return newInput[1]

def findActionIndex(actions,action):
    for ind,act in enumerate(actions):
        if act['name'] == action:
            return ind
    return -1

def getObjectIndex(objects,object):
    for ind,obj in enumerate(objects):
        if obj['name'] == object:
            return ind
    return -1

def getCombos(combos,itemHolder,equipments):
    for combo in combos:
        if combo["ingredients"][0] in itemHolder and combo["ingredients"][1] in itemHolder:
            equipments.append(combo["name"])
            itemHolder.append(combo["name"])
            print(combo["print"])
            itemHolder.remove(combo["ingredients"][0])
            itemHolder.remove(combo["ingredients"][1])
    return (itemHolder,equipments)

def perform(object, curr_sceneID,itemHolder):
    outcome = object['outcome']
    print(object['print'])
    if outcome == "Success" or outcome == 'Game Over':
        return -1
    elif outcome == 'item':
        if object["weapon"] not in itemHolder:
            itemHolder.append(object["weapon"])
            return curr_sceneID
    elif outcome == "stay":
        return curr_sceneID
    elif outcome == "move":
        return object["gotoSceneId"]
    return curr_sceneID

if __name__ == '__main__':
    curr_sceneID = 1
    itemHolder = []
    equipments = []
    healthBar = 100
    print("You health is: ", healthBar)

    while True:
        sceneInd = findSceneIndex(config, curr_sceneID)
        scene_description = config[sceneInd]['description']
        print(scene_description)
        print("Backpack: ", itemHolder)
        if "precautions" in scene_description:
            if "mask" not in equipments:
                healthBar-=10
                if healthBar == 0:
                    print("You lost all your health, Game Over")
                    break
                print("Hurry!!!!!!!! Your are losing health: ", healthBar)

        itemHolder,equipments = getCombos(config[0]["combos"],itemHolder,equipments)
        userInput = str(input("Enter your move: ")).lower()
        action = getAction(userInput)
        actions = config[sceneInd]['actions']
        actionInd = findActionIndex(actions, action)

        if actionInd == -1:
            print("Invalid Option, retry")
            continue

        elif action == "hint":
            print(actions[actionInd]["print"])
            continue
        else:
            objects = actions[actionInd]["objects"]
            object = getObject(userInput)
            objectIndex = getObjectIndex(objects, object)
            if objectIndex == -1:
                print("You performed the action correctly, but the execution is wrong ! Invalid Option, retry")
                continue
            else:
                curr_sceneID = perform(objects[objectIndex], curr_sceneID,itemHolder)
        if curr_sceneID == -1:
            print("Thank you for playing with us!")
            break











































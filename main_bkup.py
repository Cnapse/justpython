import json

f = open('/Users/crameshb/Documents/neural_nets/typeR/config_large.json')
config = json.load(f)
print(config)

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

def perform(object, curr_sceneID):
    outcome = object['outcome']
    print(object['print'])
    if outcome == "Success":
        return -1
    elif outcome == 'Game over':
        return -1
    elif outcome == "stay":
        return curr_sceneID
    elif outcome == "move":
        return object["gotoSceneId"]
    return curr_sceneID

if __name__ == '__main__':
    curr_sceneID = 1
    print("Game intro")
    while True:
        sceneInd = findSceneIndex(config, curr_sceneID)
        print(config[sceneInd]['description'])

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
                # actionObject = getObject(userInput)
                curr_sceneID = perform(objects[objectIndex], curr_sceneID)
        if curr_sceneID == -1:
            print("Thank you for playing with us!")
            break









































    """
        self.directions = ['left','right','straight']
        self.equipments = ['cloth','strings']

    def right(self):
        print("You moved right!")
    def left(self):
        print("You moved left!")
    def straight(self):
        print("You moved straight!")
    def cloth(self):
        print('you picked cloth')
    def strings(self):
        print('you picked strings')

    def move(self,choice):
        try:
            eval('self.'+choice+'()')
        except:
            print('Invalid choice, Try again!')


    def pick(self,choice):
        try:
            eval('self.'+choice+'()')
        except:
            print('Invalid choice, Try again!')
    choice = input('Enter you choice')

    if choice in self.directions:
        self.move(choice)
    elif choice in self.equipments:
        self.pick(choice)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        try:
            Game()

        except:
            print('try again')
    """


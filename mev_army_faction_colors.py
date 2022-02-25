import json
from PIL import Image, ImageDraw
 
# Opening JSON file
f = open('mev_army_array.json')
data = json.load(f)
 
def getHexColorsForFaction(factionArray, filename):

    incrementor = 0
    binary = []
    for item in factionArray:

        binaryValue = item["metadata"]["attributes"][5]["value"]
        binary.append(binaryValue)
        incrementor+=1
        if incrementor == 4:
            binary.append("#")
            incrementor = 0
    
    listToStr = ''.join(map(str, binary))
    binaryValues = listToStr.split("#")

    hexArray = []
    hexIncrementor = 0

    for binary_string in binaryValues:

        if hexIncrementor == 0:
            hexArray.append("$#")

        hexs = f'{int(binary_string, 2):X}'

        hexArray.append(hexs)
        hexIncrementor+=1
        if hexIncrementor == 6:
            hexIncrementor = 0

    hexToStr = ''.join(map(str, hexArray))
    hexx = hexToStr.split("$")

    # remove first time in array because empty
    hexx.pop(0)

    generateImageFromFractionColors(hexx, filename)


def generateImageFromFractionColors(arrayOfAllColors, filename):
    print(len(arrayOfAllColors))

    sizeOfImage = len(arrayOfAllColors)*20
    height = sizeOfImage
    width = sizeOfImage
    image = Image.new("RGB", (width, height), color="white")

    for index, hex in enumerate(arrayOfAllColors):
        x = index * 20
        shape = [(x, 0), (x+20,height)]

        img1 = ImageDraw.Draw(image)  
        img1.rectangle(shape, fill = hex)   
        del img1

    image.save(filename)

all = []
searcher = []
generalized_frontrunner = []
liquidator = []
sandwicher = []
backrunner = []
time_bandit = []

for item in data:

    all.append(item)
    legionType = item["metadata"]["attributes"][6]["value"]
    if legionType == "searcher":
        searcher.append(item)
    elif legionType == "generalized frontrunner":
        generalized_frontrunner.append(item)
    elif legionType == "liquidator":
        liquidator.append(item)
    elif legionType == "sandwicher":
        sandwicher.append(item)
    elif legionType == "backrunner":
        backrunner.append(item)
    elif legionType == "time bandit":
        time_bandit.append(item)

    
# # Closing file
f.close()

getHexColorsForFaction(all,"all.png")
getHexColorsForFaction(searcher,"searcher_faction.png")
getHexColorsForFaction(generalized_frontrunner,"generalized_frontrunner.png")
getHexColorsForFaction(liquidator,"liquidator.png")
getHexColorsForFaction(sandwicher,"sandwicher.png")
getHexColorsForFaction(backrunner,"backrunner.png")
getHexColorsForFaction(time_bandit,"time_bandit.png")
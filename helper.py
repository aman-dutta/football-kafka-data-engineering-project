def jsonWrite(json,keyword):
    fileName = keyword + ".json"
    with open(fileName, "w") as outfile:
        try:
            outfile.write(json)
        except:
            print("An exception occured")
        else:
            print("Successfully created file named: " + fileName + " in the current directory")

def csvWrite(csv,keyword):
    fileName = keyword + ".csv"
    with open(fileName, "w") as outfile:
        try:
            outfile.write(csv)
        except:
            print("An exception occured")
        else:
            print("Successfully created file named: " + fileName + " in the current directory")

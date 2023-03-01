def jsonWrite(json,keyword):
    fileName = keyword + ".json"
    with open(fileName, "w") as outfile:
        try:
            outfile.write(json)
        except:
            print("An exception occured")
        else:
            print("Successfully created file named: " + fileName + " in the current directory")

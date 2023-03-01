from search import *
from helper import *

def main():
    jsonData = searchKeyword("ManchesterUnited")
    jsonWrite(jsonData,"ManchesterUnited")
    jsonFootballData = searchKeywordWithTimeRange("Football", "2023-02-01","2023-02-02")  # For keyword with Time Range
    jsonWrite(jsonFootballData,"Football")
    

if __name__ == "__main__":
    main()
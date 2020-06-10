import pandas as pd
import re
import io
from io import StringIO


class decoder:
    """
    Reads a file as stream and tries to extract the users from the data inside.
    Dataframe expects 3 columns:
    -encryptedName
    -loginName
    -realName

    A given encrypted Name will be searched and the related real name will be provided.
    The underlying file in the example is in a readable format.
    However, in production this file is encrypted, of course.
    """

    def __init__(self):
        self.users = []
        self.fout = io.StringIO()
    

    def readFile(self, file):
        fin = open(file, mode="r", encoding="utf-8")
        for line in fin:
            separatedLine = line.split("  ")
            codedStringPart = re.sub(r'\d+ for ', "", separatedLine[0])
            codedStringPartCleaned = codedStringPart.replace("alias ", "")
            codedStringPartCleaned = codedStringPartCleaned.replace(" ", ";")
            self.fout.write(codedStringPartCleaned + ";" + separatedLine[1])
        fin.close()

        content = self.fout.getvalue()
        self.fout.close()
        return content


    def createDataFrame(self, text):
        data = pd.read_csv(StringIO(text), sep=";", header=None)
        result = self.checkDataFrame(data)
        return result
    

    def checkDataFrame(self, df):
        if df is None:
            print("No data!")
            raise TypeError

        if df.empty:
            print("DataFrame with no data inside!")
            return None
        
        if not len(df.columns) == 3:
            print("Incorrect amount of columns!")
            return None
        
        df.columns = ["encryptedName", "loginName", "realName"]
        return df

    def getRealName(self, df, encryptedName):
        if df is None:
            raise TypeError

        data = self.checkDataFrame(df)
        row = data.loc[data['encryptedName'] == encryptedName]
        if row.empty:
            print("No matching real name for: %s" %encryptedName)
            return None
        print("Found real name for: %s is --> %s" %(encryptedName, row.realName.values[0]))
        return row.realName.values[0]

# Workflow
decode = decoder()
content = decode.readFile("/Volumes/path-to-your-encrypted-file/user.txt")
df = decode.createDataFrame(content)
name1 = decode.getRealName(df, "user0082")
name2 = decode.getRealName(df, "user43a4")
name3 = decode.getRealName(df, "user0068")
name4 = decode.getRealName(df, "badhacker")
print(name1)
print(name2)
print(name3)
print(name4)


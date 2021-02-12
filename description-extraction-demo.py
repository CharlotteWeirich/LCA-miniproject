import glob
import pandas as pd
import re

if __name__ == "__main__":
    path = '/Users/emma/Documents/University/Linguistic Corpus Annotation/Project/Subtitles/HTML/*'
    files = glob.glob(path)

    result = str()

    for name in files:
        print(name)

        with open(name, encoding = "UTF-8") as f:
        # opens the source file

            dfcol = pd.read_html(f)
            for df in dfcol:
                listoflists = df.values.tolist()
                for line in listoflists:
                    if str(line[0]).strip() == "nan":
                        result += "\n\n<scene>\n"
                        result += line[1]
                        result += "\n</scene>"
            
            nameList = name.split("HTML/")
            newName = nameList[0] + "scenes.txt"

    with open(newName, 'w', encoding = "UTF-8") as f2:
        f2.write(result)
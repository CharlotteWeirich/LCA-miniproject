import glob
import pandas as pd
import re

if __name__ == "__main__":
    path = '/Users/emma/Documents/University/Linguistic Corpus Annotation/Project/Subtitles/HTML/*'
    files = glob.glob(path)

    result = str()
    dict = {}

    for name in files:
        print(name)

        with open(name, encoding = "UTF-8") as f:
        # opens the source file

            dfcol = pd.read_html(f)
            result += "<scene>\n"
            for df in dfcol:
                listoflists = df.values.tolist()
                for line in listoflists:
                    if str(line[0]).strip() == "nan":
                        if (re.match(r'(.*)?[Ss]cene(.*)?', line[1]) or re.match(r'(.*)?[Cc]amera(.*)?', line[1]) or re.match(r'(.*)?[Cc]ut(s)? (back )?to(.*)?', line[1])):
                            result += "</scene>\n"
                            result += "\n<scene>\n"
                            #result += line[1]
                        else:
                            result += "\n"
                            #result += line[1]
                    else:
                        if len(line[0]) <= 30:
                            line[1] = re.sub(r'\[[^\]]*\]', "", line[1])
                            if line[0] not in dict.keys():
                                dict[line[0]] = 0
                            dict[line[0]] += len(line[1].strip().split(" "))
                        else:
                            listoflists.remove(line)
                        result += line[0] + " says: " + line[1] + "\n"
            
            nameList = name.split("HTML/")
            newName = nameList[0] + "scenes.txt"

    with open(newName, 'w', encoding = "UTF-8") as f2:
        f2.write(result)
import glob
import pandas as pd
import re

if __name__ == "__main__":
    path = '/Users/emma/Documents/University/Linguistic Corpus Annotation/Project/Subtitles/HTML/*'
    files = glob.glob(path)

    result = ""
    filenumber = 0

    for name in files:
        print(name)

        nameList = name.split("Subtitles/HTML/")
        indexname = nameList[0] + "LCA-miniproject/scenes/index.txt"

        with open(name, encoding = "UTF-8") as f:
        # opens the source file

            dfcol = pd.read_html(f)
            for df in dfcol:
                listoflists = df.values.tolist()
                for line in listoflists:
                    if str(line[0]).strip() == "nan":
                        if (re.match(r'(.*)?[Ss]cene(.*)?', line[1]) or re.match(r'(.*)?[Cc]amera(.*)?', line[1]) or re.match(r'(.*)?[Cc]ut(s)? (back )?to(.*)?', line[1])):
                            newName = nameList[0] + "LCA-miniproject/scenes/scene" + str(filenumber) + ".txt"
                            indexes = "scene" + str(filenumber) + ".txt\n"
                            with open(newName, 'w', encoding = "UTF-8") as f2:
                                f2.write(result)
                            with open(indexname, 'a', encoding = "UTF-8") as f3:
                                f3.write(indexes)
                            result = ""
                            filenumber += 1
                    else:
                        if len(line[0]) <= 30:
                            line[1] = re.sub(r'\[[^\]]*\]', "", line[1])
                        else:
                            listoflists.remove(line)
                        result += line[0] + " says: \"" + line[1].strip() + "\"\n"
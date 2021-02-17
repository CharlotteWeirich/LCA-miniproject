import glob
import pandas as pd
import re

if __name__ == "__main__":
    path_base = "/Users/emma/Documents/University/Linguistic Corpus Annotation/Project/LCA-miniproject/"
    path_korra = path_base + "html_source/korra/*"
    path_atla = path_base + "html_source/atla/*"
    files_korra = glob.glob(path_korra)
    files_atla = glob.glob(path_atla)
    show_paths = dict()
    show_paths["korra"] = files_korra
    show_paths["atla"] = files_atla

    for show_name in show_paths:

        result = ""
        filenumber = 0
        indexes = ""
        path_base_show = path_base + "scenes/" + show_name + "/"
        index_path = path_base_show + "index.txt"

        for name in show_paths[show_name]:
            print(name)

            with open(name, encoding = "UTF-8") as f:
            # opens the source file

                dfcol = pd.read_html(f)
                for df in dfcol:
                    listoflists = df.values.tolist()
                    for line in listoflists:
                        if str(line[0]).strip() == "nan":
                            if (re.match(r'(.*)?([Ss]cene)|([Cc]amera)|([Cc]ut(s)? (back )?to)(.*)?', line[1])):
                                if (result != ""):
                                    newName = path_base_show + "scene" + str(filenumber) + ".txt"
                                    indexes += "scene" + str(filenumber) + ".txt\n"
                                    with open(newName, 'w', encoding = "UTF-8") as f2:
                                        f2.write(result)
                                    result = ""
                                    filenumber += 1
                        else:
                            if len(line[0]) <= 30:
                                line[1] = re.sub(r'\[[^\]]*\]', "", line[1])
                            else:
                                listoflists.remove(line)
                            if len(line) == 2:
                                result += line[0] + " says: \"" + line[1].strip() + "\"\n"
        
        with open(index_path, 'w', encoding = "UTF-8") as f3:
            f3.write(indexes)
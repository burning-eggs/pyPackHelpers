import os

sources_path = "./"
exclusions = [""]

sources = os.listdir(sources_path)
sources_to_format = []
sus = []

for root, dirs, files in os.walk(".", topdown=False):
    for file in files:
        if file.endswith(".py"):
            if file not in exclusions:
                print("Found file '%s'" % file)

                sources_to_format.append(os.path.join(root, file))
                sus.append(file)
            else:
                print("Found excluded file '%s'" % file)

files_to_format = " ".join(sources_to_format)

print("Formatting file(s) '%s'" % " ".join(sus))

os.system("black %s" % files_to_format)

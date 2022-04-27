import os

path='./'
filesNames = []
pathRreadme='./README.md'


# Leemos este directorio y guardamos en el array los nombres de los archivos .py
for file in os.listdir(path):
    if file.endswith(".py") and file != "main.py":
        filesNames.append(file)


# Queremos crear una tabla en markdown con los nombres de los archivos .py
# y guardarla en README.md
filesNames.sort()

# Si existe README.md lo borramos
if os.path.exists(pathRreadme):
    os.remove(pathRreadme)



# Creamos la tabla

table = '''
| Nombre del archivo | URL |
|:-----------------  |:------------------|
'''


table += "|"
for file in filesNames:
  filename = file.replace(".py", "")
  if file == filesNames[-1]:
    table += f"{filename}| [Solución](https://github.com/mrgold92/leetcode/blob/master/{file})"
  else:
    table += f"{filename}| [Solución](https://github.com/mrgold92/leetcode/blob/master/{file})\n"
  table += "|"


# Creamos el archivo README.md
with open(pathRreadme, 'a') as f:
    f.write("# LeetCode\n")
    f.write(table)


# Subimos los archivos a GitHub
os.system("git add .")
os.system("git config user.name mrgold92")
os.system("git config user.email davids1_4@hotmail.com")
os.system("git commit -m '[bot] Actualizado README.md'")
os.system("git push")







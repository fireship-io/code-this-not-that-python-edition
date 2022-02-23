# Managing files - using open and f.close() ❌
f = open("file.txt", "w")
f.write("Hi mom!") # If an exception is raised, the file won't be closed
f.close()

# Pythonic way 🐍 -  Use a context manager ✅
with open("file.txt", "w") as f:
    f.write("Hi mom!") # If an exception is raised, the file will be closed
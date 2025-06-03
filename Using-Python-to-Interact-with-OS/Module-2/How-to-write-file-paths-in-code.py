# The structure of a file path depends on the OS:
# 1. Windows = Starts with drive name
# 2. Mac/Linux = Starts with a forward slash / (the root)

# Windows file directory
# C:\my-directory\target-file.txt
# However, Windows file directory written in Python:
# C:/my-directory/target-file.txt <- Recommended way to write file paths in Python, if not, C:\\my-directory\\target-file.txt

# CurrentWorkingDirectory CWD command:
# os.getcwd()

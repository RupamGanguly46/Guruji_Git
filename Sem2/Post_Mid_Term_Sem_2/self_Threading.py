import subprocess
import time

# Define the path to the Python file with spaces in the path
file_path1 = r"C:\Users\HP\Desktop\Computer Programming\Sem2\Post_Mid_Term_Sem_2\1_Matrix.py"
file_path2 = r"C:\Users\HP\Desktop\Computer Programming\Sem2\Post_Mid_Term_Sem_2\3_Array.py"

# Run the command as a subprocess and open a separate console window
process1 = subprocess.Popen(["start", "cmd", "/k", "python", file_path1], shell=True)
process2 = subprocess.Popen(["start", "cmd", "/k", "python", file_path2], shell=True)

time.sleep(3)

# Terminate the process (close the console)

process1.terminate()
process2.terminate()


i=1
while True:
    i+=1
    print(i)
    time.sleep(1)
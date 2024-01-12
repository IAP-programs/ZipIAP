import argparse
import os 
import json 
parser = argparse.ArgumentParser(description='Example of argparse in Python')
parser.add_argument('--build',help='For Building the apk',action='store_true')
parser.add_argument('--file', help='Input file path')
parser.add_argument('--number', help='enter the files to zip')
args = parser.parse_args()
file_a = args.file
zip_files = args.number
ishan = file_a
data = '"temp" : "temp"'
c    = 0
x = b''
if args.build :
 zip_files = int(zip_files)
 if ishan.endswith(".ishan") :
  for i in range(zip_files) :
      c = int(c)
      c = c + 1
      file = input("Enter the path of the file  : ")
      f = open(file, "rb")
      x = x + f.read()
      f.close()
 
      size = os.path.getsize(file)
      name = os.path.basename(file)
      name = str(name)
      c = str(c)
      n = "file_name" + c
 
      s = "file_size" + c
      data = data + f' , "{n}":"{name}", "{s}":"{size}"'
 
  data = '{' + data + '}[#+eewjsjd$ww+$(2(2+$e+wwr#+$+r#3e+djjsjsjz#+33]'
  data = data.encode('utf-8')
 
 
  data = data + x
 
  with open(ishan, "wb") as file :
      file.write(data)
  print("")
  print("successfully completed! ")
 else :
  print("sorry the file must ends with .ishan")
 
else :
 path = file_a
 file = open(path, "rb")
 opt = file.read()
 opt = str(opt)
 space = "[#+eewjsjd$ww+$(2(2+$e+wwr#+$+r#3e+djjsjsjz#+33]"
 
 opt = opt.replace(space, "\n")
 opt = opt.splitlines()
 opt = opt[0]
 opt = opt.replace("b'", "")
 temp =  opt 
 opt = json.loads(opt)
 
 c  = 0
 for i in temp :
     c = c + 1
 file.close()
 
 
 
 c1 =   0
 file = open(path, "rb")
 c = c + 48
 tmp = file.read(c)
 print("$%$")
 print(tmp)
 while True :
 
 
  
     c1 = c1 + 1
     file_name = f"file_name{c1}"
     file_size = f"file_size{c1}"
     
     try :
         name = opt[file_name]
         size = opt[file_size]
         print(f"Extracting {name}")
     except :
         print("successfully completed!  ")
         break 
     
     size = opt[file_size]
     size = int(size)
     print(size)
 
     data = file.read(size)
     #print(data)
     with open(name, "wb") as hello :
         hello.write(data)

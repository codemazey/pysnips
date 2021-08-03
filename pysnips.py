
x = 9
x += 1

skip = True

if not skip :
  # simple print
  print("Hello world")
  
  # stdin kbd input
  #val = input("Please enter a string:\n")
  #username = input("Enter username:") # <-- input with prompt
  #print("Username is: " + username)

  # String/num print formats
  n = 567
  f = 6789.98
  s = "boo"
  
  print("1. Num is", n, "float is", f, "string is '", s, "'")
  print("2. Num is ", n, "float is ", f, " string is '", s, "'", sep="")
  print(f'3. Num is {n}, float {f} and string "{s}"')
  
  cash = 123.45
  mystr = "The price is {:.2f} quid"
  print(mystr.format( cash ) )
  
  # for loop
  print ()
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
    print(x)
  
  # Iterate through a string char by char
  for x in "cat":
    print(x)
  
  # break out of a loop
  print
  tuple_eg = ("a","fixed", "tuple" ) # can't change
  set_eg = {"unique", "items", "only", "only" } # unordered and apparently not only unique
  cats = ["siamese", "blue", "tabby", "wild"] # this is a list. It can change
  for x in cats:
    print(x)
    if x == "tabby":
      print(f"Stopped at {x}")
      break # abandon the loop
      # continue # go no further but jump to the nect loop iteration
    else:
      print ("nope not stopping")
  
  # multiline comment as multiline string
  """
  This is 
  a multi-line
  comment, not assigned
  """
  
  # Multi-line string
  print ()
  mls = """
  the
  cat
  sat
  on
  the mat
  """
  
  print( mls )
  
  # function call
  print ()
  def do_stuff( num1, num2, opt_arg = "if you want to" ):
    return num1 + num2
  
  the_answer = do_stuff(1,2)
  print("fn call: ", the_answer )
  
  # Lambdas - alternate function syntax
  print ()
  import math
  add_two_nums = lambda a, b: a+b
  
  print("lambda ", add_two_nums(2,3) )
  
  sqrt_this = 64
  ans = lambda my_sqrt : math.sqrt(my_sqrt)
  print ("lambda II sqr root of 64 is ... ", ans(sqrt_this) )
  
  print ()
  # Define a list use as an array
  ten_nums = [ 0 ] * 10
  ten_nums = [0 for i in range(10)]
  
  print (ten_nums)
  print ()
  
  # List is this long
  listlen = len(ten_nums)
  print ("list length " + str(listlen))

  ten_nums[5] = 123
  print (f"elt 5 is: {ten_nums[5]}")
  print (f"elt 6 is: {ten_nums[6]}")
  ten_nums.append(42)
  print (f"elt 10 is: {ten_nums[10]}")
  wot = ten_nums.pop(5) # remove element
  print("popped", wot)
  # can also  sort, get index of value x 
  
  # List sort (array)
  A=[1,3,4,2,7,6,0,22]
  A.sort()
  A.sort(reverse=True)
  print (A)

  # Dictionaries
  print ()
  lotr_dict = {
    "frodo"    : "hobbit"
    ,"gandalf" : "wizard"
    ,"smaug"   : "dragon"
    ,"gimli"   : "dwarf"
  }
  
  lotr_dict2 = {
    "frodo"   : "hobbit" ,
    "gandalf" : "wizard" ,
    "smaug"   : "dragon" ,
    "gimli"   : "dwarf"
  }
  
  dude="frodo"
  print (dude, " is a ", lotr_dict[dude], sep="")
  
  dude="smaug"
  print (dude, " is a ", lotr_dict[dude], sep="")
  
  # Python class example
  print ()

  class LLnode:
    def __init__(self,prev, nxt):
      self.prev = prev
      self.next = nxt

  class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
  
    def method_eg(self, a_str) :
      return self.name + " is a " + a_str
   
  p1 = Person("John", 36)
  LLnode.prev = 0

  print("person object name:", p1.name)
  print("person object age:", p1.age)
  del p1 # delete object
    
  # modules - files made of functions that you can import
  # Save the following code in a file named mymodule.py
  
  def greeting(name):
    print("Hello, " + name)
  
  # Now we can use the module we just created, by using the import statement:
  #import mymodule # <-- commented out because not built but usually not commented out obvs
  # mymodule.greeting("Jonathan") # <--- example module call
  
  # Using pip the package manager
  print ()
  # at terminal, say:  pip install camelcase 
  # thereafter you can use it as an import
  
  import camelcase
  my_cc_obj = camelcase.CamelCase()
  txt = "hello world originally all lowercase"
  print(my_cc_obj.hump(txt))
  
  # text file write
  print ()
  print("creating test file")
  f = open("demofile.txt", "a")
  file_lines="""This is a sample text file.
  This is line two
  and more \r and another 
  and more text
  and the last line.
  """
  f.write(file_lines)
  f.close()
  print("test file created")
  
  # file input
  f = open("demofile.txt", "r")
  
  print("first 10 chars: '" + f.read(10) + "'") # Read first n characters only.
  f.seek(0) # back to start
  
  whole_file = f.read() # read whole file
  print("Here comes the whole file\n" + whole_file)
  print("\n End of the whole file\n")
  
  f.seek(0) # back to start
  line1 = f.readline() # read next line
  print ("line1 is: ", line1 )
  line2 = f.readline() # read next line
  print ("line2 is: ", line2 )
  
  # Read line by line from file
  print ()
  f.seek(0) # back to start
  print ("files lines by for loop:\n")
  for x in f:
    print(x)
  print ("\nend of files lines by for loop:\n")
  f.close() # <--- close the file
  
  # File exists?
  print ()
  from pathlib import Path
  my_file = Path("demofile.txt")
  if my_file.is_file():
    # file exists
    print ("yes file exists")
  else:
    print ("nope, file does not exist")    
  
  # another way with try .. except
  my_file = Path("demofile.txt")
  try:
      my_abs_path = my_file.resolve(strict=True)
  except FileNotFoundError:
      print("this file doesn't exist")
  else:
      print("this file does exist")
  
  # Dir exists
  print()
  import os 
  a_dir = "\\etc"
  if os.path.isdir(a_dir):
      print("yep the directory exists")
  
  # Get absolute path and filename
  import os 
  currr_file = str(__file__) 
  print("full path and filename:" + currr_file)
  
  cur_path = str(os.path.abspath(os.path.dirname(__file__))) 
  print("current path to working dir/ working dir: '" + cur_path + "'")
  
  # Seems simplest for current path / dir
  cur_path = str(os.path.dirname(__file__))
  print ("alternate current path to working dir/ working dir: '" + cur_path + "'")
  
  # Seems a bit too complex this way
  the_dir_path = os.path.dirname(os.path.realpath(__file__))
  print ("dir path is: " + the_dir_path)
  
  # Best current path
  print ("Current working dir is " + os.path.relpath(the_dir_path) )
  
  # relative paths in python
  print()
  
  # get the parent directory of wherever you are
  import sys, os
  
  # add a path to the system path
  #parent_dir = str(sys.path.append(os.path.realpath('..')))
  
  # get parent directory of current path
  print()
  from pathlib import Path
  cur_path_obj = Path(str(os.path.dirname(__file__)))
  parent_dir = str(cur_path_obj.parent)
  print("Parent dir: " + parent_dir)
  
  # Search and replace
  # Read in the whole file
  with open('demofile.txt', 'r') as file :
    whole_file = file.read()
  
  # Replace all occurrences of a string in a string and a file
  whole_file = whole_file.replace('more', 'mare')
  
  # Write the same file out again
  with open('demofile.txt', 'w') as file:
    file.write(whole_file)
  
  
  # String substrings search etc
  # last character of a string
  my_str = "abcwoof"
  
  print("test str : " + my_str)
  print("last char is: " + my_str[-1])
  print("chars 0 to 2 are: " + my_str[0:2])
  print("chars 0 on but skip the last 3: " + my_str[0:-3])
  print("every 2nd char starting at 0: " + my_str[::2])
  print("every 3nd char: " + my_str[::3])
  
# Test if a string contains a substring
print ()
if "dog" not in "doggone": 
    print ("dog is not in doggone")
else:
    print ("dog is in doggone")

if "cat" in "magnificat": 
  print ("cat found")

# Stop running now
import sys
sys.exit(0)

#  exec bash/yum external OS command(s)
print()
import os
ret_cd = os.system("terraform --version")
print("ext command return code: " + str(ret_cd)) 

print()
import subprocess
run_this = "terraform --version"
res_out = subprocess.check_output(run_this, shell=True)
print("about to run the command: " + str(run_this))
print("output from running the command, is: " + str(res_out))

print()
import subprocess
#print ( commands.getstatusoutput('terraform --version') )
print("Running silently in a subprocess")
subprocess.run("terraform --version") 

# try .. except
print()
try:
  print("no_such_var")
except ValueError:
  print("bad value")
except:
  print("An exception occurred")
else:
  print("no wait, I do know that variable after all")
finally:
  print("but doing the final block as always")

# Raising an exception
print()
import sys
who = "dotty"
if who != "dot":
  dummy = 0
  # raise Exception("Sorry, don't know you")
  print("Unexpected error:", sys.exc_info()[0])

# sample webserver code
# see https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/ 


# The end  :-)
print ()
print("Made it to the end without crashing :-)")
print ()

# w3schools python reference here: https://www.w3schools.com/python/python_inheritance.asp
 

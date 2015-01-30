#Run VFB2UFO in Batch: UFO > VFB
import os

# small function to collect all files with (a) particular extension(s) in a directory
def getFiles(root, ext):
   files = []
   allfiles = os.listdir(root)
   for myfile in allfiles:
      if os.path.splitext(myfile)[1] in ext:
         files.append(os.path.join(root, myfile))
   return files

root = '/Users/ramiromacpro/Desktop/02-VFB2UFO'   # ! define your own directory here
settings = " "    # ! define your settings for VFB2UFO

new_root = "mkdir " + root +"/VFBs"
os.system(new_root) 

if not os.path.exists(root):
   print 'Not a valid directory'
else:
   ext = ['.ufo']
   filenames = getFiles(root, ext)

for n in filenames:
	run_VBFB2UFO = "vfb2ufo "+ settings + n 
	move_files = "mv " + root + "/*.vfb" +" "+ new_root+"/"
	os.system(run_VBFB2UFO),os.system(move_files) 
	

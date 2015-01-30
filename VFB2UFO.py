#Run VFB2UFO in Batch: VFB > UFO
import os

# small function to collect all files with (a) particular extension(s) in a directory
def getFiles(root, ext):
   files = []
   allfiles = os.listdir(root)
   for myfile in allfiles:
      if os.path.splitext(myfile)[1] in ext:
         files.append(os.path.join(root, myfile))
   return files

root = '/Users/you/Desktop/VFB2UFO_folder'   # ! define your own directory here
settings = "-64 "    # ! define your settings for VFB2UFO

new_root = "mkdir " + root +"/UFOs"
os.system(new_root) 

if not os.path.exists(root):
   print 'Not a valid directory'
else:
   ext = ['.vfb']
   filenames = getFiles(root, ext)

for n in filenames:
	run_VBFB2UFO = "vfb2ufo "+ settings + n 
	move_files = "mv " + root + "/*.ufo" +" "+ new_root+"/"
	os.system(run_VBFB2UFO),os.system(move_files) 
	

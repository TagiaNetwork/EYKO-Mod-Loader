import os, tempfile, json, shutil, functools, distutils

"""
    Election Year Knockout
    Resource Modification Loader
"""

path = os.getcwd()
mod_dir = path + "\\Mods"

def directory_checker():
    if os.path.split(os.getcwd())[1] == "Election Year Knockout":
        return True
    else:
        return False

# Create file structure + example mod
def generate_structure():
    if os.path.isdir(mod_dir) == False:
        os.makedirs(mod_dir + "\examplemod\music-hd")
        open(mod_dir + "\\examplemod\\modinfo.json", 'w').write("{\n    \"mod\": {\n        \"name\": \"Example Mod\",\n        \"description\": \"Example description\"\n    }\n}")
        print("File Structure Created")
    else:
        print("File Structure Loaded")

# Backup resource files
def create_backup():
    if os.path.isdir(path + "\\Backup") == False:
        destination = shutil.copytree(path + "\\Resources", path + "\\Backup")
        print("Backup Created:", destination)
    else:
        print("Backup Location Found:", path + "\\Backup")

# Read modinfo JSON file
def modinfo_reader(path):
    with open(path + '\\modinfo.json') as f:
      data = json.load(f)
    return data # returns dictionary of json data

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = functools.reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir


# Generates dicts for the file struct
def resources_structure():
    colors = get_directory_structure(path + "\\Resources")['Resources']['colors']
    fonts = get_directory_structure(path + "\\Resources")['Resources']['fonts']
    images = get_directory_structure(path + "\\Resources")['Resources']['images']
    music = get_directory_structure(path + "\\Resources")['Resources']['music']
    musichd = get_directory_structure(path + "\\Resources")['Resources']['music-hd']
    particles = get_directory_structure(path + "\\Resources")['Resources']['particles']
    sounds = get_directory_structure(path + "\\Resources")['Resources']['sounds']
    soundshd = get_directory_structure(path + "\\Resources")['Resources']['sounds-hd']
    spines = get_directory_structure(path + "\\Resources")['Resources']['spines']
    strings = get_directory_structure(path + "\\Resources")['Resources']['strings']

def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f), 
                                    os.path.join(dest, f), 
                                    ignore)
    else:
        shutil.copyfile(src, dest)

# Load mods
def mod_loader():
    mods = os.listdir("Mods")
    print(mods)
    
    # Load first mod. Will be made recursive later once the system is completely set up
    cd = mod_dir + "\\" + mods[0] # Set working directory to the first mod found.
    if os.path.isfile(cd + "\\modinfo.json"):
        mod_name = modinfo_reader(cd)["mod"]["name"]
        mod_desc = modinfo_reader(cd)["mod"]["description"]
        
        artifacts = os.listdir(cd)
        if 'modinfo.json' in artifacts: artifacts.remove('modinfo.json')
        
        for item in artifacts: # Remove empty directories
            working = cd + "\\" + item
            if not os.listdir(working):
                artifacts.remove(item)
        for single in artifacts:
            recursive_overwrite(cd + "\\" + single, path + "\\Resources\\" + single)
            
        print(artifacts)
    else:
        print("mod not found")

    """for i,j,y in os.walk('Mods'):
        print(i)"""

# Clean up afterwards and restore backup
def cleanup():
    shutil.rmtree(path + "\\Resources")
    destination = shutil.copytree(path + "\\Backup", path + "\\Resources")

if directory_checker() == True:
    create_backup()
    generate_structure()
    #resources_structure()
    mod_loader()

else:
    print("Please move " + os.path.basename(__file__) + " to your Election Year Knockout game folder.")
    

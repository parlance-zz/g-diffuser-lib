"""
MIT License

Copyright (c) 2022 Christopher Friesen
https://github.com/parlance-zz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


g_diffuser_cli.py - command line interface for g-diffuser-lib with interactive mode

"""

import ntpath # these lines are inexplicably required for python to use long file paths on Windows -_-
ntpath.realpath = ntpath.abspath

import g_diffuser_lib as gdl
from g_diffuser_config import DEFAULT_PATHS

import os, sys
os.chdir(DEFAULT_PATHS.root)

import datetime
import argparse
import code
import importlib
import time
import glob
import shutil

import numpy as np
import cv2

VERSION_STRING = "g-diffuser-cli v0.95b"
INTERACTIVE_MODE_BANNER_STRING = """
Interactive mode:
    call sample() with keyword arguments and use the up/down arrow-keys to browse command history:

sample("pillars of creation", n=3, scale=15)                         # batch of 3 samples with scale 15
sample("greg rutkowski", init_img="my_image.png", n=0)               # setting n <=0 repeats until stopped
sample("something's wrong with the g-diffuser", sampler="k_euler")   # uses the k_euler sampler

sample() # arguments can be omitted to use your last args instead
s()      # some commands have shortcuts / aliases

reset_args() # reset your arguments back to defaults
show_args()  # shows your *basic* input arguments
show_args(0) # shows *all* your input arguments
load_args()  # use your last args (from auto-saved json file in inputs/json)
save_args("my_fav_args") # you can save your args; these are saved as json files in the inputs path
load_args("my_fav_args") # you can load saved args by name; these are json files in the inputs path

compare("path1", "path2", "path3") # make a grid from all images in specified output paths
compare("a", "b", mode="rows")     # arrange each output path's images into rows instead
compare("a", "b", file="my_compare.png") # the comparison image will be saved in ./outputs/compare.png
                                         # use file to specify the output filename instead

list()             # show list of files / folders in ./outputs
list("my_path")    # show list of files / folders in specified output path
remove("my_path")  # moves the specified output path from ./outputs to ./backups
restore("my_path") # moves the specified output path from ./backups to ./outputs
save("my_path")    # copies the specified output path from ./outputs to ./saved
clear()            # clear the command window if things get cluttered
help()             # display this message
exit()             # exit interactive mode
"""

LAST_ARGS_PATH = DEFAULT_PATHS.inputs+"/json/last_args.json"
        
def main():
    global VERSION_STRING, INTERACTIVE_MODE_BANNER_STRING, LAST_ARGS_PATH
    global INTERACTIVE_CLI_ARGS, INTERACTIVE_CLI_STARTING_ARGS, INTERACTIVE_CLI_INTERPRETER
    
    INTERACTIVE_CLI_ARGS = argparse.Namespace()
    
    parser = gdl.get_args_parser()
    args = parser.parse_args()
    if (args.prompt == "") and (args.interactive == False) and (args.load_args == ""):
        parser.print_help()
        exit(1)

    print("")
    if args.debug: print(VERSION_STRING + ": --debug enabled (verbose output on, writing debug files...)")
    else: print(VERSION_STRING + ": use --debug to enable verbose output and writing debug files...")
    if args.load_args:
        print("")
        cli_load_args(args.load_args)
        INTERACTIVE_CLI_ARGS.load_args = args.load_args
        args = INTERACTIVE_CLI_ARGS
    else:
        INTERACTIVE_CLI_ARGS = args
    
    gdl.start_grpc_server(args)
    INTERACTIVE_CLI_STARTING_ARGS = argparse.Namespace(**vars(args)) # copy for reset function
    
    if args.interactive:
        cli_locals = argparse.Namespace()
        cli_locals.sample = cli_get_samples
        cli_locals.s = cli_get_samples
        cli_locals.show_args = cli_show_args
        cli_locals.sha = cli_show_args
        cli_locals.load_args = cli_load_args
        cli_locals.la = cli_load_args
        cli_locals.save_args = cli_save_args
        cli_locals.sa = cli_save_args
        cli_locals.reset_args = cli_reset_args
        cli_locals.ra = cli_reset_args
        cli_locals.list = cli_dir
        cli_locals.ls = cli_dir
        cli_locals.dir = cli_dir
        cli_locals.remove = cli_remove
        cli_locals.rm = cli_remove
        cli_locals.restore = cli_restore
        cli_locals.save = cli_save
        cli_locals.clear = cli_clear
        cli_locals.cls = cli_clear
        cli_locals.help = cli_help
        cli_locals.exit = cli_exit
        cli_locals.compare = cli_save_comparison_grid
        
        INTERACTIVE_CLI_INTERPRETER = code.InteractiveConsole(locals=dict(globals(), **vars(cli_locals)))
        INTERACTIVE_CLI_INTERPRETER.interact(banner=INTERACTIVE_MODE_BANNER_STRING, exitmsg="")
        exit(0)
    else:
        if not args.load_args: gdl.print_namespace(args, debug=args.debug, verbosity_level=1)
        
        args.init_time = str(datetime.datetime.now()) # time the command was created / queued
        samples = gdl.get_samples(args)

        try: # try to save the used args in a last_args json file for convenience
            gdl.save_json(vars(gdl.strip_args(args)), LAST_ARGS_PATH)
        except Exception as e:
            if args.debug: print("Error saving sample args - " + str(e))

    return
    
def cli_get_samples(prompt=None, **kwargs):
    global INTERACTIVE_CLI_ARGS, LAST_ARGS_PATH
    args = argparse.Namespace(**(vars(INTERACTIVE_CLI_ARGS) | kwargs)) # merge with keyword args
    if prompt: args.prompt = prompt
    if args.n <= 0: print("Repeating sample, press ctrl+c to stop...")
    
    args.init_time = str(datetime.datetime.now()) # time the command was created / queued
    args_copy = argparse.Namespace(**vars(args)) # preserve args, if sampling is aborted part way through
    try:                                         # anything could happen to the data
        samples = gdl.get_samples(args)
    except KeyboardInterrupt:             # if sampling is aborted with ctrl+c or an error, restore the args we started with
        INTERACTIVE_CLI_ARGS = args_copy
    except Exception as e:
        print("Error in gdl.get_samples '" + str(e) + "'")
        INTERACTIVE_CLI_ARGS = args_copy
    else:
        INTERACTIVE_CLI_ARGS = args        # preserve args for next call to sample() if everything went ok
        try:                               # try to save the used args in a json tmp file for convenience
            gdl.save_json(vars(gdl.strip_args(args)), LAST_ARGS_PATH)
        except Exception as e:
            if args.debug: print("Error saving sample args - " + str(e))

    if args.debug: gdl.print_namespace(args, debug=0, verbosity_level=1)
    return
    
def cli_show_args(level=None):
    global INTERACTIVE_CLI_ARGS
    if level != None: verbosity_level = level
    else: verbosity_level = 1
    gdl.print_namespace(INTERACTIVE_CLI_ARGS, debug=INTERACTIVE_CLI_ARGS.debug, verbosity_level=verbosity_level)
    return
    
def cli_load_args(name=""):
    global DEFAULT_PATHS, LAST_ARGS_PATH
    global INTERACTIVE_CLI_ARGS
    try:
        if not name: json_path = LAST_ARGS_PATH
        else: json_path = DEFAULT_PATHS.inputs+"/json/"+name+".json"
        saved_args_dict = gdl.load_json(json_path)
        INTERACTIVE_CLI_ARGS = argparse.Namespace(**(vars(INTERACTIVE_CLI_ARGS) | saved_args_dict)) # merge with keyword args
        gdl.print_namespace(INTERACTIVE_CLI_ARGS, debug=INTERACTIVE_CLI_ARGS.debug, verbosity_level=1)
    except Exception as e:
        print("Error loading last args from file - " + str(e))
    return
    
def cli_save_args(name):
    global INTERACTIVE_CLI_ARGS
    global DEFAULT_PATHS
    try:
        json_path = DEFAULT_PATHS.inputs+"/json/"+name+".json"
        saved_path = gdl.save_json(vars(gdl.strip_args(INTERACTIVE_CLI_ARGS)), json_path)
        print("Saved " + saved_path)
    except Exception as e:
        if INTERACTIVE_CLI_ARGS.debug: print("Error saving args - " + str(e))
    return

def cli_reset_args():
    global INTERACTIVE_CLI_ARGS, INTERACTIVE_CLI_STARTING_ARGS
    INTERACTIVE_CLI_ARGS = argparse.Namespace(**vars(INTERACTIVE_CLI_STARTING_ARGS))
    cli_show_args()
    return

def cli_dir(output_path=""):
    global DEFAULT_PATHS
    target_path = DEFAULT_PATHS.outputs
    if output_path: target_path += "/"+output_path
    os.system('dir "'+target_path+'"')
    return   

def cli_remove(output_path):
    assert(output_path)
    global DEFAULT_PATHS
    old_path = DEFAULT_PATHS.outputs+"/"+output_path
    new_path = DEFAULT_PATHS.backups+"/"+output_path
    shutil.move(old_path, new_path)
    print("Removed '"+output_path+"' to "+DEFAULT_PATHS.backups)
    return   

def cli_restore(output_path):
    assert(output_path)
    global DEFAULT_PATHS
    old_path = DEFAULT_PATHS.backups+"/"+output_path
    new_path = DEFAULT_PATHS.outputs+"/"+output_path
    shutil.move(old_path, new_path)
    print("Restored '"+output_path+"' to "+DEFAULT_PATHS.outputs)
    return   

def cli_save(output_path):
    assert(output_path)
    global DEFAULT_PATHS
    old_path = DEFAULT_PATHS.outputs+"/"+output_path
    new_path = DEFAULT_PATHS.saved+"/"+output_path
    shutil.copytree(old_path, new_path)
    print("Saved copy of '"+output_path+"' to "+DEFAULT_PATHS.saved)
    return   

def cli_clear():
    os.system("cls")
    return   
    
def cli_help():
    global VERSION_STRING, INTERACTIVE_MODE_BANNER_STRING
    print(VERSION_STRING+INTERACTIVE_MODE_BANNER_STRING+"\n")
    return
    
def cli_exit():
    global INTERACTIVE_CLI_ARGS
    gdl._p_kill(INTERACTIVE_CLI_ARGS.grpc_server_process.pid)
    exit(0)
    
def cli_save_comparison_grid(*paths, **kwargs):
    global DEFAULT_PATHS
    args = argparse.Namespace(**kwargs)
    if not "mode" in args: args.mode="columns"
    else: args.mode = args.mode.lower()
    if not "file" in args: grid_filename = "compare.png"
    else: grid_filename = args.file
    grid_filename = DEFAULT_PATHS.outputs+"/"+grid_filename

    num_paths = len(paths)
    assert(num_paths > 1)
    path_samples = []

    max_sample_width = 0  # keep track of the largest image in all the folders to make everything fit in the event of non-uniform size
    max_sample_height = 0
    for path in paths:
        path_files = glob.glob(DEFAULT_PATHS.outputs+"/"+path+"/*.png")
        for file in path_files:
            if os.path.basename(file).startswith("grid_"): path_files.remove(file) # exclude grid images from comparison grids
        path_files = sorted(path_files)

        samples = []
        for file in path_files:
            img = cv2.imread(file)
            max_sample_width = np.maximum(max_sample_width, img.shape[0])
            max_sample_height = np.maximum(max_sample_height, img.shape[1])
            samples.append(img)
        path_samples.append(samples)

    max_path_samples = 0
    for path_sample_list in path_samples:
        if len(path_sample_list) > max_path_samples: max_path_samples = len(path_sample_list)

    if args.mode != "rows": layout = (max_path_samples, num_paths)
    else: layout = (num_paths, max_path_samples)
    np_grid = np.zeros((layout[0] * max_sample_width, layout[1] * max_sample_height, 3), dtype="uint8")

    for x in range(len(path_samples)):
        for y in range(len(path_samples[x])):
            sample = path_samples[x][y]
            paste_x = x * max_sample_width
            paste_y = y * max_sample_height
            if args.mode != "rows":
                paste_x = y * max_sample_width
                paste_y = x * max_sample_height
            np_grid[paste_x:paste_x+max_sample_width, paste_y:paste_y+max_sample_height, :] = sample[:]
    
    cv2.imwrite(grid_filename, np_grid)
    print("Saved " + grid_filename)
    return

if __name__ == "__main__":
    main()
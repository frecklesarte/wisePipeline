# Create a function that allows folders and sub-folders to be listed, and read here
import os
import pathlib as Path
from directory_generation.home_directory_validator import validUserDirectory


# Creates lists of all the folders required by pre-production
# Allow lists to be used for generating  preset folder-structures
class list_pre_production_folders():
    
    def valid_directory():
        #define the valid home dir to gen from
        

    def list_top_folders():
# Lists the top-level-parent folder 'pre-production'.
        parent_folder = ['pre-production']
        if parent_folder == True:
            os.mkdir(parent_folder)
            if False:
                return 0

    # Lists  folders within  pre-production.
#def list_subfolders():
    def list_sub_folders():
        subfolders = ['parent_folder', ['Research-Development'], ['Design'], ['Writing']]
        if subfolders == True:
            os.mkdir(subfolders)
            if False:
                return 0
# List the subfolders and any sub-subfolders for pre-production.
#def list_subsubfolders():

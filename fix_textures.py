import os.path
import re

import maya.cmds as cmds

NEW_ROOT_PATH = "C:/project_path"
NEW_SUBDIRECTORY = ""
pattern = re.compile(r'([^\r]+)(\/sourceimages\/)(\S+\/)*(\S+\.\S+)')


def fixTexturePath():
    texture_list = cmds.ls(type = 'file')
    if (texture_list != None):
        for texture in texture_list:
            # save on db
            texture_path = ""
            texture_path = cmds.getAttr(texture + '.ftn', x = True)
            print texture_path
            i = texture_path.rfind("sourceimages")
            if (i > -1):

                if not os.path.isfile(texture_path):
                    path_match = pattern.match(texture_path)
                    new_path = ''.join([NEW_ROOT_PATH, path_match.group(2), NEW_SUBDIRECTORY, path_match.group(4)])
                    print texture_path, " ---> ", new_path
                    cmds.setAttr(texture + '.ftn', new_path, type = "string")
            else:
                print "texture outside sourceimages"
            
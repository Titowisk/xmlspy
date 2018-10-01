# This module itends to group xml files by type (CTE or NFE) and version (1.04, 2.00, 3.10)

# user inputs the directory path where relies all xmls files inside folders named by year
# xmlspy reads all and copy those files into directories grouped by type an version

#example:
# ALESA_XMLS/XML 2013/ have xmls files with types/versions CTE_1.04, NFE_2 and NFE_3.1
# the result will create inside /ALESAT_XMLS/:
#   /XML_2013_CTE_104/ containing only CTE_1.04 files;
#   /XML_2013_NFE_200/ containing only NFE_2.00 files;
#   /XML_2013_NFE_310/ containing only NFE_310 files;

import argparse
import xml.etree.ElementTree as ET
import os
import re
import shutil

"""
Definition of parse

The actual definition of "parse" in Wiktionary is "To split a file or other input into 
pieces of data that can be easily stored or manipulated." 
So we are splitting a string into parts then recognizing the parts to convert it into 
something simpler than a string.
"""

# step 1
# Receive an input of the directory that contains the xmls files
# checks if there are xml files

# step 2
# iterate over the files to use the xml.etree.ElementTree module to parse
# files according to its type (CTE_1.04, NFE_2 or NFE_3.1)


# step 3
# create a directory called <dir-name_type> for each type found and copy the files
# with matching types inside these directories

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path of the directory containing xmls files")
    parser.add_argument("-d", "--delete", 
        help="deletes all the directories created by the xml parser and its files",
        action="store_true"
    )
    parser.add_argument("-l", "--log", 
        help="shows quantity information about the execution of the algorithm",
        action="store_true"
    )
    args = parser.parse_args()

    xml_dir_path = args.path

    if args.delete:
        #deletes all xmls files https://docs.python.org/3/library/shutil.html#shutil.rmtree
        for root, dirs, files in os.walk(xml_dir_path):
            if any( t in os.path.basename(root) for t in ('cteProc', 'nfeProc')):
                shutil.rmtree(root)
                print("{0} directory and its whole tree delete successfully".format(os.path.basename(root))) 
    else:
        for root, dirs, files in os.walk(xml_dir_path):
            quantity_verifier = {} # each directory will have a verifier
            list_of_xml_files = xml_path_handler(root)
            xml_version_parser(list_of_xml_files, root, quantity_verifier)
            # quantity verification
            if (args.log): verifier_format(quantity_verifier, root)
            
            
        
    
    # print(os.getcwd())

# step 1

def xml_path_handler(xml_dir_path):
    # This function takes a path, check if there are xmls files, and return a iterator containing only xml files

    # https://docs.python.org/3/library/os.html#os.scandir
    # https://docs.python.org/3/library/os.html#os.DirEntry

    xml_quantity = 0
    dir_name = os.path.basename(xml_dir_path)
    list_of_xml_files = []
    for entry in os.scandir(xml_dir_path):
        if entry.name.endswith('.xml'):
            list_of_xml_files.append(entry)
            xml_quantity += 1
    if xml_quantity > 0:    
        print("There are {0} xml files in {1}".format(xml_quantity, dir_name))
    else:
        print("There aren't xml files in {0}".format(dir_name))
    return list_of_xml_files

# step 2 and 3

def xml_version_parser(list_of_xml_files, xml_dir_path, quantity_verifier):
    # this function takes a list of xml files and iterate over them to parse each file 
    # into different types inside the corresponding folder
    
    type_regex = re.compile(r'cteProc|nfeProc', re.IGNORECASE) # re.compile(r'\w*Proc')

    for xf in list_of_xml_files:
        xml_file_path = os.path.join(xml_dir_path, xf.name) # leticia_xml_2/XMLs 2016/'xf.name'
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        type_version = root.get('versao')
        mo = type_regex.search(root.tag)

        if (mo and type_version):
            dir_name = "xmlspy_{0}_{1}".format(mo.group(), type_version)
            new_dir_path = os.path.join(xml_dir_path, dir_name)

            # prevents walking into created directory if this algorithm is ran twice or more times
            if dir_name == os.path.basename(xml_dir_path):
                print("{0} already exists, breaking loop.".format(dir_name))
                break
            # create dir
            if not (os.path.isdir(new_dir_path)):
                os.mkdir(new_dir_path)
            # copy file into dir https://docs.python.org/3.6/library/shutil.html#shutil.copy
            shutil.copy(xml_file_path, new_dir_path)

            # count +1 for each (type, type_version)
            verifier = '{type}_{type_version}'.format(type=mo.group(), type_version=type_version)
            quantity_verifier.setdefault(verifier, 0)
            quantity_verifier[verifier] += 1


def verifier_format(quantity_verifier, root):
    # Friendly format for log output
    log_format = ''
    log_format += 'Directory: {0}\n'.format(os.path.basename(root))
    quant_sum = 0
    for k, v in quantity_verifier.items():
        quant_sum += v
        log_format += '{name}: {quantity}\n'.format(name=k, quantity=v) 
    log_format += 'Total: {0}\n'.format(quant_sum)
    log_format += ('=-='*10)
    print(log_format)

main()
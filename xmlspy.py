# This module itends to group xml files by type (CTE or NFE) and version (1.04, 2.00, 3.10)

# user inputs the directory path where relies all xmls files inside folders named by year
# xmlspy reads all and copy those files into directories grouped by type an version

#example:
# ALESA_XMLS/XML 2013/ have xmls files CTE_1.04, NFE_2 and NFE_3.1
# the result will create inside /ALESAT_XMLS/:
#   /XML_2013_CTE_104/ containing only CTE_1.04 files;
#   /XML_2013_NFE_200/ containing only NFE_2.00 files;
#   /XML_2013_NFE_310/ containing only NFE_310 files;

import argparse
import xml.etree.ElementTree as ET
import os




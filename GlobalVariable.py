#!/usr/bin/env python
import json

class env:
    """ Global variables created in this class by use of add function"""
    def add(self,key,value):
        """ Add attribute of key value pair to class
        Attributes:
            key -- string for env class
            value -- value of attribute (can be of any type)
        """
        setattr(self,key,value)
    def dir(self):
        """Returns list of all the attributes of the class"""
        return dir(self)
    def vars(self):
        """return vars(self)"""
        return vars(self)
    def delete(self,key):
        """ delete specified attribute"""
        delattr(self,key)
    def has(self,key):
        """ return True if key is in class, False if key is not in class"""
        return hasattr(self,key)
    def json_out(self,file):
        """ Output the variables (vars(self) of class to json file specified using json.dump"""
        with open(file,'w') as outfile:
            json.dump(vars(self), outfile, sort_keys = True, indent = 4,separators=(',',':'),ensure_ascii=False)
        print 'Output to file %s :'%file
    def json_in(self,file):
        """ Input the variables of file specified to class using json.load and self.add"""
        with open(file,'r') as infile:
            data=json.load(infile)
        for key,value in data.items():
            self.add(key,value)
        print 'Read values from file %s :'%file

def get_parse():
    """ Get specified parse values using ArgumentParser"""
    # use argparse to read in specified files to 
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-o","--outfilename", help="Output file name to write"  ,default = "./output.txt")
    parser.add_argument("-i","--infilename" , help="Input file name to read"    ,default = "./output.txt")
    #parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    args = parser.parse_args()
    return args

from gooey import Gooey,GooeyParser
@Gooey(program_name = "Shaun's test run") # add gooey decorator to main argparse function
def get_parse_gooey():
    """ Get specified parse values using ArgumentParser or GooeyParser"""
    # use argparse to read in specified files to 
    #use gooeyParser instead of ArgumentParser to utilize the widgets
    parser = GooeyParser()
    parser.add_argument("-o","--outfilename", help="Output file name to write"  ,default="./output.txt",widget='FileChooser')
    parser.add_argument("-i","--infilename" , help="Input file name to read"    ,default="./output.txt",widget='FileChooser')
    #parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    args = parser.parse_args()
    return args

def main():
    import numpy as np
    # import parse values
    args = get_parse_gooey() # use gooey
    #args = get_parse() # don't use gooey
    # create env variables and output to json outfilename
    f=env()
    f.add('h','f')
    f.add('h1',{'h':7 , 'g':6})
    f.add('A',np.ones((4,4)).tolist())
    print 'f = ',f.dir()
    print 'f = ',f.vars()
    f.json_out(args.outfilename)
    # read in values from json infilename and print to screen
    d = env()
    d.json_in(args.infilename)
    print 'd = ',d.vars()

if __name__=="__main__":
    main()

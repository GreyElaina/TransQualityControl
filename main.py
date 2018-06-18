#!/usr/bin/python3
import src.branch_error_check.branch_main
import src.duplicate_key_check.duplicate_main
import src.format_char_check.format_main

import sys
import os

if __name__ == '__main__':
    syslist = sys.argv

    def info_w():
        branch_json = src.branch_error_check.branch_main.branch_check(PL['Project_assets'])
        duplicate_json = src.duplicate_key_check.duplicate_main.duplicate_main(PL['Project_assets'])
        format_json = src.format_char_check.format_main.format_main(PL['Project_assets'])

        if(os.path.exists("./branch.json") == True):
            os.remove("./branch.json")
        if(os.path.exists("./duplicate.json") == True):
            os.remove("./duplicate.json")
        if(os.path.exists("./format.json") == True):
            os.remove("./format.json")
        #删除文件

        branch = open(PL['OutputPath'] + "/branch.json","w")
        duplicate = open(PL['OutputPath'] + "/duplicate.json","w")
        formatjson = open(PL['OutputPath'] + "/format.json","w")
        branch.write(branch_json)
        duplicate.write(duplicate_json)
        formatjson.write(format_json)
        branch.close()
        duplicate.close()
        formatjson.close()
        #写json数据到文件

    def setProjectDir(dir):  
        PL['Project_dir'] = dir
        PL['Project_assets'] = PL['Project_dir'] + "/assets"
    
    def setOutputPath(path):
        PL['OutputPath'] = path

    def IsNeedingDefault():
        for i in PL:
            if(PL[i] == ""):
                PL[i] = DPL[i]
                print("test" + PL[i])

    mainsyslist = [
        ["--projectDir",setProjectDir],
        ["-D",setProjectDir],
        ["--output",setOutputPath],
        ["-O",setOutputPath]
    ]
    DPL = {
        "OutputPath" : ".",
        "Project_dir" : "./project",
        "Project_assets" : "./project/assets"
    }
    #PL = [OutputPath,project_dir,project_assets]
    PL = {
        'OutputPath' : '',
        "Project_dir" : "",
        "Project_assets" : ''
    }

    for i in range(len(syslist)):
        for ii in range(len(mainsyslist)):
            if (syslist[i] == mainsyslist[ii][0]):
                #传入参数处理
                mainsyslist[ii][1](syslist[i + 1])

    IsNeedingDefault()
    info_w()

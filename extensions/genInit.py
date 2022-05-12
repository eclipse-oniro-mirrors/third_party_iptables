#!/usr/bin/env python
# Copyright (c) 2022 Huawei Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import replace
from gettext import find
import os
import shutil
import sys
oriPath = os.path.dirname(os.path.abspath(__file__))
newPath = oriPath+"/gen"
isExists=os.path.exists(newPath)
# 判断结果
print (newPath)
if not isExists:
    # 如果不存在则创建目录
    os.makedirs(newPath) 
    print (newPath)
else:
    print (newPath)

newInitFileName = newPath+"/"+sys.argv[3]
os.mknod(newInitFileName)
newInitFile = open(newInitFileName, 'a', encoding='utf-8')
filelist = os.listdir(oriPath)
fileInitlist = []
for filterFile in filelist:  
    filename, extension = os.path.splitext(filterFile)
    if (sys.argv[1] in filterFile) & (extension == ".c") & (filterFile not in sys.argv[2]):
        print(filterFile)
        src = os.path.join(oriPath, filterFile)
        dst = os.path.join(newPath, filterFile)
        shutil.copy(src, dst)
        readFile = open(dst, 'r+', encoding='utf-8')
        content = readFile.read() 
        readFile.close
        replaceInitText = filterFile.rstrip("\.c") + "_init(void)"
        newContent = content.replace("_init(void)",replaceInitText)
        if "_init(void)" in content:    # 判断要替换的内容是否在文本文件中
            writeFile = open(dst, 'w', encoding='utf-8')
            writeFile.write(newContent)
            writeFile.close  
            newInitFile.write("extern " + "void  " + replaceInitText + ";\n")
            fileInitlist.append(filterFile.rstrip("\.c") + "_init" + "();\n")
newInitFile.write("void init_"+sys.argv[4]+"(void);\n")
newInitFile.write("void init_"+sys.argv[4]+"(void)\n{\n")
for fileInitName in fileInitlist:
    newInitFile.write(fileInitName)
newInitFile.write("}")
newInitFile.close
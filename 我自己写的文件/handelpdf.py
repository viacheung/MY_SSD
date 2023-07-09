import os
from glob import glob
import shutil
path="C:/Users/50537\OneDrive/学习资料/JVM/1_内存与垃圾回收篇"
newpath="C:/Users/50537/OneDrive/学习资料/JVM/jvm_pdf"
objects=os.listdir(path)
# dir_list=[] #存放目录列表
# file_list=[] #存放文件列表
def file_filter(f):
 if f[-4:] in ['.pdf']:
  return True
 else:
  return False

for obj in objects:
  # os.listdir 就是遍历的文件名称
  smal_objects = os.listdir(os.path.join(path, obj))
  for smal_obj in smal_objects:
   # 组合一下文件路径
   first = os.path.join(path, obj)
   # 过滤文件类型
   files = list(filter(file_filter, smal_objects))
   print(files)
   # list不可以join  需要在for一下
   for file in files:
    final=os.path.join(first,file)
    shutil.copy(final,newpath)



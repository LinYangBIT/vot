###################################################################################################　　
# 　　　　　   　Download the VOT2019-rgbt-thermal dataset
###################################################################################################
import json
import os
import wget,tarfile,zipfile
import pdb 
 
vot_2019_path = 'E:/0/dataset1/vot2019_rgbt_dataset/'      # object file
json_path = 'E:/0/description.json'  # vot 2019 json file
anno_vot = 'vot2019'                           # vot2019 or vot2018 or vot2017
 
 
with open(json_path,'r') as fd:
    vot_2019 = json.load(fd)
home_page = vot_2019['homepage']
 
for i,sequence in enumerate(vot_2019['sequences']):
    print('download the {} sequences'.format(i+1))
    # 
    annotations = sequence['annotations']['url']
    rgb_data_url = sequence['channels']['color']['url'].split('../')[-1]  
    ir_data_url = sequence['channels']['ir']['url'].split('../')[-1]  

 
    name = annotations.split('.')[0]
    file_name = annotations.split('.')[0] + '.zip'
 
    down_annotations = os.path.join(home_page, anno_vot,'rgbtir/meta', annotations)
    down_rgb_data_url = os.path.join(home_page, anno_vot, 'rgbtir', rgb_data_url)
    down_ir_data_url = os.path.join(home_page, anno_vot, 'rgbtir', ir_data_url)
 
 
    rgb_image_output_name = os.path.join(vot_2019_path, name, 'color', file_name)
    ir_image_output_name = os.path.join(vot_2019_path, name, 'ir', file_name)

    anno_output_name = os.path.join(vot_2019_path, name, file_name)
    out_dir = os.path.dirname(anno_output_name)
 
    if os.path.exists(out_dir) == False:
        os.mkdir(out_dir)

    # pdb.set_trace() 

    ###########################################################################
    ####            Download Annotation files 
    ###########################################################################    
    # annotations download and unzip and remove it
    wget.download(down_annotations, anno_output_name)
    print('loading {} annotation'.format(name))
    # unzip
    file_zip = zipfile.ZipFile(anno_output_name,'r')
    for file in file_zip.namelist():
        file_zip.extract(file, out_dir)
        print('extract annotation {}/{}'.format(name,file))
    file_zip.close()
    os.remove(anno_output_name)
    print('remove annotation {}.zip'.format(name))
 

    ###########################################################################
    ####            Download Color images 
    ###########################################################################    
    # image download and unzip ad remove it
    out_dir = os.path.dirname(rgb_image_output_name)
    if os.path.exists(out_dir) == False:
        os.mkdir(out_dir)

    # pdb.set_trace()
    wget.download(down_rgb_data_url, rgb_image_output_name)
    print('loading {} sequence --- rgb files ...'.format(name))
 
    file_zip = zipfile.ZipFile(rgb_image_output_name,'r')
    for file  in file_zip.namelist():
        file_zip.extract(file,out_dir)
        print('extract image {}'.format(file))
    file_zip.close()
    os.remove(rgb_image_output_name)
    print('remove image file {}.zip'.format(name))
    print('sequence  {} Completed!'.format(i+1))

    ###########################################################################
    ####            Download Infrared images 
    ###########################################################################    
    # image download and unzip ad remove it
    out_dir = os.path.dirname(ir_image_output_name)
    if os.path.exists(out_dir) == False:
        os.mkdir(out_dir)

    # pdb.set_trace()
    wget.download(down_ir_data_url, ir_image_output_name)
    print('loading {} sequence --- infrared files ...'.format(name))
    
    file_zip = zipfile.ZipFile(ir_image_output_name, 'r')
    for file  in file_zip.namelist():
        file_zip.extract(file,out_dir)
        print('extract image {}'.format(file))
    file_zip.close()
    os.remove(ir_image_output_name)
    print('remove image file {}.zip'.format(name))
    print('sequence  {} Completed!'.format(i+1))



print("=====================================================================")
print("             Great!!! All videos have been dowloaded ......")
print("=====================================================================")
import csv
import os
import shutil
from chardet.universaldetector import UniversalDetector

def get_encode_info(file):
    with open(file, 'rb') as f:
        detector = UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']

def read_file(file):
    with open(file, 'rb') as f:
        return f.read()

def write_file(content, file):
    with open(file, 'wb') as f:
        f.write(content)

def convert_encode2utf8(file, original_encode, des_encode):
    file_content = read_file(file)
    file_decode = file_content.decode(original_encode,'ignore')
    file_encode = file_decode.encode(des_encode)
    write_file(file_encode, file)

## Move *.txt to a folder
def move2txtfolder(path, txt_file_list):
    txt_folder_path = path + '\\txt'
    if not os.path.exists(txt_folder_path):
        os.makedirs(txt_folder_path)

    for file in txt_file_list:
        des_path = os.path.join(txt_folder_path, os.path.basename(file))
        shutil.move(file, des_path)

##find all txt files in the folder
def findtxt(path, txt_file_list):
    file_name_list = os.listdir(path)
    for filename in file_name_list:
        de_path = os.path.join(path, filename)
        if os.path.isfile(de_path):
            if de_path.endswith(".txt"):  # Specify to find the txt file.
                txt_file_list.append(de_path)
        else:
            findtxt(de_path, txt_file_list)

def txt2csv(txt_file):
    ##convert encoding in all file to utf-8
    encode_info = get_encode_info(txt_file)
    if encode_info != 'utf-8':
        convert_encode2utf8(txt_file, encode_info, 'utf-8')

    csv_file = os.path.splitext(txt_file)[0] + '.csv'
    with open(csv_file, 'w+', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')

        with open(txt_file, 'r', encoding='utf-8') as txtfile:
            for line in txtfile.readlines():
                line_list = line.strip('\n').split(' ')
                writer.writerow(line_list)

if __name__ == '__main__':
    folder_path = '.../astrocytes/dataset/labels/'
    
    # txt_file_list = []
    # findtxt(folder_path, txt_file_list)

    
    txt_file_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.join(folder_path, file).endswith('.txt')]

    for txt_file in txt_file_list:
        txt2csv(txt_file)
    
    move2txtfolder(folder_path, txt_file_list)

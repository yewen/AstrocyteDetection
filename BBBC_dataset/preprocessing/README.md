There are 4 steps to convert this file into the YOLOv5 PyTorch TXT format:

First, we convert those raw lable files to csv format to enable them editable;

Second, extract the valid columns including the coordinates of each box;

Third, export those extracted label files to Tensorflow Object Detection CSV format. Each line is in the form $(filename,width,height,class,xmin,ymin,xmax,ymax)$, where filename, width and height are associated with filename, width and height of the corresponding image, while xmin,ymin,xmax and ymax are associated with minimum and maximum coordinates of each bounding box;

Last, we apply online tool to convert the label files into the YOLOv5 PyTorch TXT format which is availabel on website: https://roboflow.com/convert/tensorflow-object-detection-csv-to-yolov5-pytorch-txt



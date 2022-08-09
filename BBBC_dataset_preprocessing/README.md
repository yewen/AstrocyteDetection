The label file provided with the BBBC dataset is not consistent with the YOLOv5 PyTorch TXT format since label are in the form $(class, x_1, y_1, x_2, y_2)$, where $x_{i}$ and $y_{i}$ are x and y coordinates, resp., of the upper-left and lower-right corners of the bounding box in the image. 
To convert this file into the YOLOv5 PyTorch TXT format, there are 4 steps:

First, we convert those raw lable files to csv format to enable those files are editable;

Second, extract the valid columns including the coordinates of each box;

Third, export those extracted label files to Tensorflow Object Detection CSV format. Each line is in the form $(filename,width,height,class,xmin,ymin,xmax,ymax)$, where filename, width and height are associated with filename, width and height of the corresponding image, while xmin,ymin,xmax and ymax are associated with minimum and maximum coordinates of each bounding box;

Last, we could apply online tool to convert the label files intothe YOLOv5 PyTorch TXT format which is availabel on website: https://roboflow.com/convert/tensorflow-object-detection-csv-to-yolov5-pytorch-txt



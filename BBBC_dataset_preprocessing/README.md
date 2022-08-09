The label file provided with the BBBC dataset is not consistent with the YOLOv5 PyTorch TXT format since label are in the form $(class, x_1, y_1, x_2, y_2)$, 
where $x_{i}$ and $y_{i}$ are x and y coordinates, resp., of the upper-left and lower-right corners of the bounding box in the image. 
To convert this file into the YOLOv5 PyTorch TXT format, there are 4 steps:
First, we convert those raw lable files to csv format to enable those files are editable;
Second, 

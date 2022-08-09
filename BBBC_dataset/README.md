BBBC dataset is publicly available at the  Broad Bioimage Benchmark Collection {https://bbbc.broadinstitute.org/BBBC042}, as well as the annotations.

The label file provided with the BBBC dataset is not consistent with the YOLOv5 PyTorch TXT format since label are in the form 
$(class, x_1, y_1, x_2, y_2)$, where $x_{i}$ and $y_{i}$ are x and y coordinates, resp., of the upper-left and lower-right corners of the bounding box 
in the image. To convert the file into the YOLOv5 PyTorch TXT format, we write the programming part under 'preprocessing'.

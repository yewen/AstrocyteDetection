BBBC dataset is publicly available at the  Broad Bioimage Benchmark Collection https://bbbc.broadinstitute.org/BBBC042, as well as the annotations.

The label file provided with the BBBC dataset is not consistent with the YOLOv5 PyTorch TXT format since label are in the form 
$(class, x_1, y_1, x_2, y_2)$, where $x_{i}$ and $y_{i}$ are x and y coordinates, resp., of the upper-left and lower-right corners of the bounding box 
in the image. To convert the file into the YOLOv5 PyTorch TXT format, we write the programming part under "preprocessing".

The first 783 images were used as training dataset, and the continuous 225 images were used as validation dataset. The test dataset including 31 images is selected from the rest images.

Hyperparameters were evolved with 300 generations and 10 epochs per generation with Fitness Function as (0.5, 0.5, 0, 0). We excluded hyperparameters image mosaic, image mixup and image scale by setting to 0 the correponding hyperparameters.

After hyperparameter evolve, we have training preparation manuscript to set up environment and training manuscript to launch training.

The trained model including the best weights and evolved hyperpapermeters are saved under "model".

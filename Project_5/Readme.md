
### Identifying curb ramps on sidewalks through Google Street View images

Write about why detect curb ramps and assumptions
  
### 1. The Data

#### Images extraction
Pictures of intersections using Google Street View API. Lat/long extracted from [accessmap.io](https://accessmap.io)

### 2. Choosing the Model

#### Method for identifying curb ramps on images

There are different ways of identifying a  specific class on images
Image Classification x Object Detection x Object Segmentation.

<p align="center"> <img src="post_images/image_detection.jpg" width="90%"></p>

For this project I chose the object detection method. First, because since I'm training images with custom classes, it requires drawing simple bounding boxes around the ramps, instead of polygons as in segmentation. And I believe it would be a tricky task to use the classification method on a new category. 

Second, as a path to my quest, the Tensorflow Object Detection API - realeased by Google in 2017 - facilitates the task.

#### Tensorflow Object Detection API:

The Object Detection API has been trained on Microsoft COCO dataset (a dataset of about 300,000 images of 90 commonly found objects) with different trainable detection models. The API does the fine-tuning of a pre-trained object detection model with own data set with new classes, method called "transfer learning", modifing the dense layers and the final softmax layer to output 2 categories (yellow_curb_ramp, gray_curb_ramp) instead of 90. It also includes image augmentation, such as flipping and saturation.

#### Architecture

There's a speed/accuracy trade-off when choosing the object detection model, as despicted in the image below:

<p align="center"> <img src="post_images/models_trade-off.jpg" width="70%"></p>
  
The sweet spot is the “elbow” part of the mAP (Mean Average Precision) vs GPU time graph. Based on that, I chose to use [Faster R-CNN](https://arxiv.org/pdf/1506.01497.pdf) object detection model, with [RestNet](https://arxiv.org/abs/1512.03385) feature extractor, trained on [COCO](http://cocodataset.org) dataset.

### 3. Training the Model

#### GPU

#### Training dataset and labelling

#### Installing the API

#### Convert labels to the TFRecord format

#### Implement new model with TensorFlow

### 4. Results!

### 5. Next Steps

* Learn how to get the precision and recall
* Learn how to improve image augmentation
* Train more images






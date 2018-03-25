
### Movivation

<Write about why detect curb ramps>
  
### The Data

#### Images extraction
Pictures of intersections using Google Street View API. Lat/long extracted from [accessmap.io](https://accessmap.io)

### Choosing the Model

#### Method for identifying curb ramps on images

Image Classification x Object Detection x Object Segmentation.

<add comparison image>

Chose Object Detection
* Tensorflow Object Detection API facilitates this task
* Requires drawing bounding boxes for labeling objects in you own

#### Tensorflow Object Detection API:

Released in 2017.
Does the fine-tuning of a pre-trained object detection model using own data set with new classes.


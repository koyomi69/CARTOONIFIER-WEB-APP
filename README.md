# CARTOONIFIER-WEB-APP

Our goal is to make the Real World Images look like they are genuinely from a Cartoon. This is done by applying a bilateral filter on our input image. A bilateral filter is used for smoothening images and reducing noise, while preserving edges. Because a bilateral filter smooths flat regions while keeping edges sharp, it is ideally suited to convert an RGB image into a cartoon. Unfortunately, bilateral filters are orders of magnitudes slower than other smoothing operators (e.g., Gaussian blur). Thus, for having a high performance, it is operated on a down-scaled version of the original image first and then is upscaled afterwards. 

## Original Image

![Alt text](/relative/backend/src/input.jpg?raw=true "Optional Title")


## Cartoonizer Result

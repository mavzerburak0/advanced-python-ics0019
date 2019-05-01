#### This small script is written by Kadir Burak Mavzer for Advanced Python (ICS0009) class at IT College of Taltech.

It overlays the given photo with a tri-color flag (Estonian flag for now). OpenCV and numpy libraries are used to achieve the desired results. Therefore, it accepts both .jpg and .png files.

There are some test images in original_img/ folder.

First, the script splits the given image into 3 and creates a new image with the same size but filled with only one color. Then, it transparently overlays these two images. After all this is done, it stitches the three images that have been overlaid with a certain color back together and saves the output into final_image/ folder.

To run, navigate to the project folder in your terminal and run:

    python3 flag_overlay.py
 
When run, it will ask for a path. Make sure you include the correct path, otherwise an error indicating that the file was not found will be thrown. If you enter a correct path to an image, it will apply the overlay effect and save the output as "output.jpg" to final_image/ folder.
import cv2
import numpy as np


def crop_images(image_, x, height_, y, width_):
    """
    Crops an image by given coordinates, height and width
    :param image_: image to be crop
    :param x: x coordinate to crop from
    :param height_: height to crop from
    :param y: y coordinate to crop from
    :param width_: width to crop from
    :return: copy of the cropped image for the flag piece to be created
    """
    crop = image_[x:height_, y:width_].copy()
    output = crop.copy()
    return output


def create_flag_piece(height_, width_, red_, green_, blue_):
    """
    Creates a one-color image
    :param height_: height of the blank image to be created
    :param width_: width of the blank image to be created
    :param red_: number between 0-255 representing intensity of the color
    :param green_: number between 0-255 representing intensity of the color
    :param blue_: number between 0-255 representing intensity of the color
    :return: an image object with a colored background
    """
    blank_image = np.zeros((height_,width_,3), np.uint8)
    blank_image[:, 0:width_] = [blue_, green_, red_]
    return blank_image


def overlay_images(output, blank_image, path_):
    """
    Transparently overlays an image
    :param output: output image object
    :param blank_image: an image with a certain color background
    :param path_: path to save the output
    :return: transparently overlaid image
    """
    opacity = 0.2
    added_image = cv2.addWeighted(output, opacity, blank_image, 0.1, 0)
    cv2.imwrite(path_, added_image)
    return added_image


def stitch_images(height_, width_, images_, path_):
    """
    Stitches 3 transparently overlaid images back together
    :param height_: height of the final image
    :param width_: width of the final image
    :param images_: a list of images to be stitched together
    :param path_: path to save the final image
    :return: null
    """
    final_image = np.zeros((height_, width_, 3), dtype=np.uint8)
    y_ = 0
    for image in images_:
        width_ = image.shape[0]
        height_ = image.shape[1]
        # add an image to the final array and increment the y coordinate
        final_image[y_:width_ + y_, :height_, :] = image
        y_ += image.shape[0]
    cv2.imwrite(path_, final_image)


def main():
    image_path = input("Enter the image path: ")
    try:
        # Reading the image and obtaining its width and height
        image = cv2.imread(image_path)
        width, height = image.shape[1], image.shape[0]
        # Image will be cropped horizontally into 3 pieces, therefore
        # we need its height to be divided by 3
        slice_height = height / 3
        # The path for the split images to be saved
        path = "cropped_img/"

        # Splitting given image into 3 pieces horizontally
        crop1 = crop_images(image, 0, int(slice_height), 0, width)
        crop2 = crop_images(image, int(slice_height), int(height - slice_height), 0, width)
        crop3 = crop_images(image, int(height - slice_height), height, 0, width)

        # Creating flag pieces with RGB colors
        blue = create_flag_piece(int(slice_height), width, 0, 114, 207)
        black = create_flag_piece(int(slice_height), width, 0, 0, 0)
        # As it might be slightly different and cause problems, I'm getting
        # the height of the last piece.
        last_height = crop3.shape[0]
        white = create_flag_piece(int(last_height), width, 255, 255, 255)

        # Overlaying the images with the same sized flag pieces
        added_image1 = overlay_images(crop1, black, path + "cropped_img1.jpg")
        added_image2 = overlay_images(crop2, blue, path + "cropped_img2.jpg")
        added_image3 = overlay_images(crop3, white, path + "cropped_img3.jpg")
        images = [added_image1, added_image2, added_image3]

        # Finally, stitching all 3 images together
        stitch_images(height, width, images, "final_image/output.jpg")
    except:
        print("File not found.")


if __name__ == '__main__':
    main()

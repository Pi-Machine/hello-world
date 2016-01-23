"""Play with pictures using Python Image Library."""

from PIL import Image

def sunset(pixels, width, height):
    """Convert to sunset colours."""

    for x in range(width):
        for y in range(height):
            # get the RGB components of the pixel
            (r, g, b) = pixels[x, y]
            # modify the RGB components of the pixel
            # to get the sunset effect
            # need to convert new values to integers
            pixels[x, y] = (r, int(g * 0.5), int(b * 0.5))

def greyscale(pixels, width, height):
    """Convert to greyscale."""

    for x in range(width):
        for y in range(height):
            # REPLACE "pass" WITH YOUR SOLUTION
            # DO NOT FORGET TO INDENT!
            # here you want to replace each of R,G,B components
            # with the combination of the current R,G,B components
            # calculated as follows:
            # 0.3 * R + 0.59 * G + 0.11 * B
            # (i.e. the NEW values of R,G,B are all the same)
            # don't forget to convert to integers!
            pass

def flip(pixels, width, height):
    """Flip upside down."""

    for y in range(height // 2):  # NOTICE THE " // 2" HERE: it is integer division
        for x in range(width):
            # REPLACE "pass" WITH YOUR SOLUTION
            # DO NOT FORGET TO INDENT!
            # Hint: to swap values A and B in Python, you can just say
            # A, B = B, A
            # think carefully about which pixels you want to swap!
            pass

def mirror(pixels, width, height):
    """Flip horizontally (make a mirror image)."""

    for x in range(width // 2): # NOTICE THE " // 2" HERE: it is integer division
        for y in range(height):
            # REPLACE "pass" WITH YOUR SOLUTION
            # DO NOT FORGET TO INDENT!
            # Hint: to swap values A and B in Python, you can just say
            # A, B = B, A
            # think carefully about which pixels you want to swap!
            pass

def spacecraft(pixels, width, height):
    """Insert a spacecraft at top left corner."""

    # open the image of a spacecraft with a black background
    spacecraft = Image.open("spacecraft.jpg")

    # get pixels of the spacecraft image as a 2D list
    space_pixels = spacecraft.load()

    # get the width and the height of the spacecraft image
    space_width, space_height = spacecraft.size

    for x in range(space_width):
        for y in range(space_height):
            # REPLACE "pass" WITH YOUR SOLUTION
            # DO NOT FORGET TO INDENT!
            # to check if the pixel is black, use an if-statement:
            # if (r, g, b) = (0, 0, 0):
            # to check if the pixel is NOT black, use an if-statement:
            # if (r, g, b) != (0, 0, 0):
            pass

def blur(pixels, width, height):
    """Blur the picture."""

    # how much to blur
    blurring = 5

    for y in range(height):
        # for x in [0, blurring, 2*blurring, 3*blurring, ... width - blurring), do:
        for x in range(0, width - blurring, blurring):
            # REPLACE "pass" WITH YOUR SOLUTION
            # DO NOT FORGET TO INDENT!
            # Hint: you want another loop here
            pass

def posterize(pixels, width, height):
    """Change colours so that the image looks like a poster."""

    for x in range(width):
        for y in range(height):
            # REPLACE pass WITH YOUR SOLUTION
            # DO NOT FORGET TO INDENT!
            # here you want to replace each of the R, G, B components
            # as follows:
            #   if the colour is in [0, 7], replace it with 4
            #   if the colour is in [8, 15], replace it with 12
            #   ...
            #   if the colour is in [248, 255], replace it with 252
            # think about a concise way of writing these instructions!
            # experiment with ranges of length other than 8 and see
            # what effect they have on the resulting picture
            pass

def reduce_noise(pixels, width, height):
    """Reduce the noise in the picture.
    Warning: takes a long time!"""

    hood = 5  # how many pixels in the neighbourhood to examine
    threshold = 1000  # how similar do pixels have to be in order to
                      # be used for computing the average

    # for x in [hood, hood + 1, hood + 2, ..., width - hood - 1]
    for x in range(hood, width - hood, 1):
        # for y in [hood, hood + 1, hood + 2, ..., height - hood - 1]
        for y in range(hood, height - hood, 1):

           # Examine all pixels around the current one up to a
           # distance of 'hood' in each direction.
           # Compute the average R, G, and B values of all 
           # pixels in this neighbourhood, considering only those pixels,
           # for which the square of the Euclidean distance to the current
           # pixel is less than threshold.
           # The square of the Euclidean distance between the pixels
           # (r1, g1, b1) and (r2, g2, b2) is
           # (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2
           # Replace the R, G, B values of the current pixel with the
           # average value.
           # When you are done with the implementation, experiment with
           # different values for 'hood' and 'threshold' to see what
           # effect they have on the noise reduction.
           pass    


def find_edges(pixels, width, height):
    """Find the edges in the picture."""

    pass


def find_lines(pixels, width, height):
    """Find the lines in the picture."""

    pass


def main(modify_func, picture):
    
    # get the image of Toronto skyline from file
    image = Image.open(picture)

    # make a copy of the image
    new_image = image.copy()

    # get pixels of the image as a 2D list
    new_pixels = new_image.load()
    
    # get width and height of the image
    width, height = new_image.size

    # modify the image by applying modify_func
    modify_func(new_pixels, width, height)
    
    # create a new image that contains the original and
    # the modified images, side by side
    both = Image.new(image.mode, (2 * width, height))
    both.paste(image, (0, 0))
    both.paste(new_image, (width, 0))
    both.save('result.jpg')
    both.show()

if __name__ == '__main__':

    main(sunset, "skyline.jpg")
    #main(greyscale, "skyline.jpg")
    #main(posterize, "skyline.jpg")
    #main(flip, "skyline.jpg")
    #main(mirror, "skyline.jpg")
    #main(spacecraft, "skyline.jpg")
    #main(blur, "skyline.jpg")
    #main(reduce_noise, "noise.jpg")

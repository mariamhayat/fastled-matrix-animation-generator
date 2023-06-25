from PIL import Image, ImageFilter

# Open image file
im = Image.open('image.gif')

#variable to hold frame rate/speed of animation
delay = 350
print("\n** Analysing image **\n")

# Display image format, size, colour mode
print("Format:", im.format, "\nWidth:", im.width, "\nHeight:", im.height, "\nMode:", im.mode)

# Check if GIF is animated
frames = im.n_frames
print("Number of frames: " + str(frames))


print("\n** Converting image **\n")

file1 = open("FastLED_Anim_Code.txt", "w")


# Iterate through frames and pixels, top row first
for z in range(frames):
    # Convert to RGB
    rgb_im = im.convert('RGB')
    i = 0
  # Go to frame
    im.seek(z)
    print("Frame: ", im.tell())

    for y in range(im.width):
        for x in range(im.height):

            # Get RGB values of each pixel
            r, g, b = rgb_im.getpixel((x, y))
            if(i<128):
                file1.write("leds["+str(i)+"] = CRGB(" + str(r) + "," + str(g) + "," + str(b) +  ")" + ";\n")
                i+=1

    file1.write("calibrate();\nFastLED.show();\ndelay(" + delay + ");\n")
    #calibrate() is a fn on the Arduino side at the moment that checks for layout pattern of the LED Strip. More details in README file.
    #calibrate() snippet is added as a separate file under calibrate folder 
file1.close()
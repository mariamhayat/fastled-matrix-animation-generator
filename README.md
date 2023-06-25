# FastLED 2D Matrix Animation Code Generator
This project allows you to generate code for the FastLED library from gif files that you can create in any program of your choice. 


## How To Use

To get started with this we need a gif file that should ideally be the same resolution as the panel. The code iterates through every pixel of the every frame of the image and assigns that to the corresponding LED on the panel. To understand this, it is important to understand how FastLED library renders color to the LEDs, for which I recommend going through [this](https://github.com/FastLED/FastLED/wiki/Controlling-leds+).

The program is pretty crude at the moment(but the core functionality works), so it needs some initial values to get started. Let's look at them.

```python
# Open image file
im = Image.open('image.gif')

#variable to hold frame rate/speed of animation
delay = 350

#number of LEDs in panel
NUM_LEDS = 128
```

Firstly, we need a GIF file to work with. Like mentioned above, it should ideally be the same resolution as the frame. The code has measures in place to check for that though but still.


![cat-export](https://github.com/suramyadas01/fastled-matrix-animation-generator/assets/41816183/71282ce9-4f1b-4208-a9c8-13627591488d)

"delay" is the framerate the of the animation. Higher the number, slower the animation. 
"NUM_LEDS" is the number of the LEDs in the strip. 

It is important to understand and compare the layout of the panel and the GIF. The panel should ideally have the first LED on the top left corner. 

![image](https://github.com/suramyadas01/fastled-matrix-animation-generator/assets/41816183/68db09ac-0e12-48ba-a6aa-f8553086e671)

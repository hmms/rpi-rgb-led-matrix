#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
from datetime import datetime
import math

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        pos = offscreen_canvas.width
        my_text = self.args.text
	frequency = .1
	i = 0
        while True:
	    if(i < 32):
	        i = i + 1
	    else:
		i = 0
	    red   = math.sin(frequency*i + 0) * 63 + 110
            green = math.sin(frequency*i + 2) * 63 + 110
            blue  = math.sin(frequency*i + 4) * 63 + 110

	    textColor = graphics.Color(red, green, blue)
            now = datetime.now()
	    my_text = now.strftime("%H:%M:%S")
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 32, textColor, my_text)
            pos = 4

	    time.sleep(0.5)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()

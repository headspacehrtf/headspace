#!/usr/python

# HeadSpace HRTF Library
# Graphical Filter Interface

# Author: Christopher Rabl
# Modified: April 22, 2012

from pyo import *
from headspace import *

s = Server().boot()
s.start()

ui = HeadSpaceUI("Barbershop")

shaverWav = SfPlayer("testfiles/shaver.wav", loop=True)
shaver = HeadSpace(shaverWav, 0, 0)
ui.add("Shaver", shaver)

backgroundWav = SfPlayer("testfiles/VictorOrchestra-BlackWhiteRagtime.wav", loop=True)
background = HeadSpace(backgroundWav, 100, 30)

dooropenWav = SfPlayer("testfiles/dooropen.wav", loop=True)
dooropen = HeadSpace(dooropenWav, -20, -10)

phoneringWav = SfPlayer("testfiles/phonering.wav", loop=True)
phonering = HeadSpace(phoneringWav, -150, -20)

ui.show()

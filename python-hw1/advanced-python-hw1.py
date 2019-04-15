"""
    
    This is a small GUI application that converts WGS84 to L-EST97 and vice versa.
    Written by Kadir Burak Mavzer for Advanced Python (ICS0019) course at IT College
    of TalTech.

    * Written in Python3.x
    * PySimpleGUI was used to create the GUI and pyproj to do the conversion.

    Results can be confirmed via https://epsg.io/transform#s_srs=4326&t_srs=3301&x=0.0000000&y=0.0000000

    Program can be run on any computer which has python3 installed.
    Go to your terminal of choice and type:
        python3 advanced-python-hw1.py

    GUI should be displayed and you can enter coordinates in their respective input boxes.
    Then, click on the respective button to do the conversion.


"""

from pyproj import Proj, transform
import PySimpleGUI as sg

lestProj = Proj(init="epsg:3301")
wgsProj = Proj(init="epsg:4326")

def lestToWgs(x1, y1):
    lest_tuple = transform(lestProj, wgsProj, y1, x1)
    return round(lest_tuple[0], 6), round(lest_tuple[1], 6)

def wgsToLest(x1, y1):
    wgs_tuple = transform(wgsProj, lestProj, x1, y1)
    return round(wgs_tuple[0], 2), round(wgs_tuple[1], 2)

# Creating the GUI
layout = [[sg.Text('Enter coordinates in either wgs84 or l-est97 format', size=(15,1))], 
[sg.Text('x-coordinate', size=(15,1)), sg.In(key='x')], 
[sg.Text('y-coordinate', size=(15,1)), sg.In(key='y')],     
[sg.Button('wgs84 to l-est97'), sg.Button('l-est97 to wgs84'), sg.Quit()]
        ]
window = sg.Window('Test', default_element_size=(40,1)).Layout(layout)


event, values = window.Read()


# Using GUI pop-ups to display results
if (event != 'Quit'):

    # Converting values to float is necessary since they are in string format
    x = float(values['x'])
    y = float(values['y'])

    if (event == 'wgs84 to l-est97'):    
        sg.Popup('WGS84 to L-EST97: ', wgsToLest(x, y))

    elif(event == 'l-est97 to wgs84'):
        sg.Popup('L-EST97 to WGS84: ', lestToWgs(y, x))




# Unit Tests
# NB: L-EST97 latitude and longitudes are reversed
# L-EST97 to WGS84
assert(lestToWgs(3597461.93, 4461755.88) == (59.395319, 24.66419))
assert(lestToWgs(3649000.08, 840285.73) == (27.380583, 33.631839))
assert(lestToWgs(3985016.93, -2376018.53) == (-4.289303, 31.396239))


# WGS84 to L-EST97
assert(wgsToLest(59.445756, 24.819039) == (4456851.38, 3617596.88))
assert(wgsToLest(60.165226, 24.925954) == (4522285.16, 3672183.63))
assert(wgsToLest(56.918474, 22.532240) == (4338233.37, 3212315.17))


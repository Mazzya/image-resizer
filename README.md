# Image Resizer
![Image Resizer](https://img.freepik.com/vecteurs-libre/beau-colibri-volant-element-conception-pour-bannieres-affiches-depliants-brochures_1262-13457.jpg?size=338&ext=jpg)<br>
**Version 1.0.0** - [Change log](CHANGELOG.md)

Image Resizer it is a script that allows you to quickly resize images of all kinds and without installing practically anything.
This script uses the pillow library which is a fork of the famous Python Image Library project to do all the magic!
### How to resize images ?
To run this script you need to install Python and the PIL library (Python Image Library) :
* [Python](https://www.python.org/downloads/)
```
pip install PIL
```
To run the script, type this command in the console :
```
python resizer.py
```
When the script runs, it will ask you for the path of the image you want to resize
```
Image path : 
```
It will also ask for the width
```
width: 
```
It will also ask for the height
```
height: 
```
If you want to keep the aspect ratio, answer with 'y' else answer with 'n'
```
Do you want keep aspect ratio ?[y/n]: 
```
The extension of the new image is necessary, choose from the following with the number that represents it
```
1 => jpg
2 => png
3 => gif
4 => tiff
5 => psd
6 => bmp

Please choose an extension for the image: 
```
Finally, write the name you want to give the new image
```
Image name:
```
The resized images are stored in a directory called images that is automatically created in the same directory where the script is located.
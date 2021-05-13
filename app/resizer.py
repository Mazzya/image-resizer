from PIL import Image
import os

BANNER = """                                                   
                         &&&&%%                                                 
                      &&&%%%&&&%%#                                              
                        (&&&&%%&&&%%                                            
                      &&%%. &&&&%%@@%%                                          
                        &&&&&%%%%&@%&@%%                           ,/(          
       /#######(/((((       &&&&&%%%&@%@%#                   .,/.               
            */((((#####/(((&&&%%%%&%%%%@@&#        ///%@(((((                   
         ###(#(((((((((/((###%(/%&&%%@@%%((##    ////(((((((                    
               /((((((((((((###%.,/(*%%&&#(###* /((.////((((                    
            ####(((((((((###((((/,%(,../(##(((#(///(,(*/((((                    
                 /////(((((((((((##*..*.*/,,*#(#/////*,*/(((                    
               (#((((/(((((/((((((((/*/%#.**,*///*///(((/(((                    
                  ###(((((/(((/(((((((/*#%*#%.,%(///,/(/((((                    
                       /##((((*((((((((((*#,*/***(//////(((/                    
                           ,##(,/(((/(((((((**/(////((((/(((                    
                                  #( #(((#(#(////(/((((*((*(                    
                                        ( #///////////(((((                     
                                         ****//(/*(/(/(((/                      
                                        **/*///((/////((.                       
                                       */*/////*/(//((                          
                                      .*/(##(*(/(#(                             
                                      //%###(((% (/                             
                                    (((###%# %.#                                
                                   (((##                                            
                                 ((/((((   Developed by Mazzya                                      
                               /##/((((   Version 1.0.0                                      
                              #(#/((#(   Github: https://github.com/Mazzya                                     
                             #/#//(#/   mazzya.tk                                      
                             */ (/ */                                           
                               #/  .
"""


def Menu():
    print(BANNER)
    try:
        """ Full path of the image if it is not in the same directory as the script """
        img = input("Image path: ")

        """ Image width """
        width = int(input("Width: "))

        """ Image height """
        height = int(input("Height: "))

        """ Ask the user if they want to keep the aspect ratio for a better image. """
        choice = input("Do you want keep aspect ratio ?[y/n]: ")

        if choice.lower() == 'y':
              """ If the user want keep aspect ratio """
              extension = imageExtension()
              if verifyExtension(extension):    
                resizeImageAR(img, width, height, extension)

        elif choice.lower() == 'n':
              """ If the user doesnt want keep aspect ratio """
              extension = imageExtension()
              if verifyExtension(extension):    
                resizeImage(img, width, height, extension)
        else:
            """ If the user enters another value than y/n  """
            print("Try again please, remember only y or n")

    except ValueError:
        """ If the user enters something other than a number """
        print("Something is wrong, try again")

    except FileNotFoundError:
        """ If the image does not exist """
        print("Oops! check image path")

    except AttributeError:
        print("Please check the values you have entered and try again.")
    except OSError:
      print("Try again please")


def resizeImage(img, width, height, extension):
      """ This function resizes an image """
      image = Image.open(img)
      newImage = image.resize((width, height))
      image_name = imageName()
      verifyDirectory()
      final_image = image_name + '.' + extension
      newImage = newImage.save(f"images/{final_image}")

def resizeImageAR(img, width, height, extension):
      """ This function resizes an image while maintaining the aspect ratio """
      image = Image.open(img)
      newImage = image.thumbnail((width, height))
      image_name = imageName()
      verifyDirectory()
      final_image = image_name + '.' + extension
      newImage = image.save(f"images/{final_image}")

def imageExtension():
      """ This function allows user to choose an extension for the new image """
      extensions = {1:'jpg', 2:'png', 3:'gif', 4:'tiff', 5:'psd', 6:'bmp'}
      options = """
      1 => jpg
      2 => png
      3 => gif
      4 => tiff
      5 => psd
      6 => bmp
      """
      print(options)
      choice = int(input("Please choose an extension for the image: "))
      if choice in extensions:
            extension = extensions[choice]
            return extension
      else:
            print("The extension is not valid, choose an extension from the list")

def verifyExtension(ext):
      """ This function verifys if the extension is not empty """
      isValid = False
      if ext is not None:
            isValid = True
            return isValid

def imageName():
      """ This function asks the user the image name """
      image_name = input("Image name: ")
      if image_name == "":
            image_name = "new_image"
      return image_name

def verifyDirectory():
      if os.path.exists("images") == False:
            os.mkdir("images")

if __name__ == "__main__":
    Menu()

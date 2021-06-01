from PIL import Image
import os

__version__ = 'v1.1.1'
BANNER = f"""                                                   
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
                               /##/((((   {__version__}                                      
                              #(#/((#(   Github: https://github.com/Mazzya                                     
                             #/#//(#/   mazzya.tk                                      
                             */ (/ */                                           
                               #/  .
"""


def menu():
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
            extension = image_extension()
            if verify_extension(extension):
                resize_image_ar(img, width, height, extension)

        elif choice.lower() == 'n':
            """ If the user doesnt want keep aspect ratio """
            extension = image_extension()
            if verify_extension(extension):
                resize_image(img, width, height, extension)
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


def resize_image(img: str, width: int, height: int, extension: str):
    """ This function resizes an image """
    image = Image.open(img)
    new_image = image.resize((width, height))
    img_name = image_name()
    verify_directory()
    final_image = img_name + '.' + extension
    new_image.save(f"images/{final_image}")
    path = os.path.join(os.getcwd(), "images", final_image)
    print(f"""
      The image has been successfully resized.
      Image path : {path}
      """)


def resize_image_ar(img: str, width: int, height: int, extension: str):
    """ This function resizes an image while maintaining the aspect ratio """
    image = Image.open(img)
    image.thumbnail((width, height))
    img_name = image_name()
    verify_directory()
    final_image = img_name + '.' + extension
    image.save(f"images/{final_image}")
    path = os.path.join(os.getcwd(), "images", final_image)
    print(f"""
      The image has been successfully resized.
      Image path : {path}
      """)


def image_extension() -> str:
    """ This function allows user to choose an extension for the new image """
    extensions = {1: 'jpg', 2: 'png', 3: 'gif', 4: 'tiff', 5: 'psd', 6: 'bmp'}
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


def verify_extension(ext: str) -> bool:
    """ This function verify if the extension is not empty """
    is_valid = False
    if ext is not None:
        is_valid = True
    return is_valid


def image_name() -> str:
    """ This function asks the user the image name """
    img_name = input("Image name: ")
    if img_name == "":
        img_name = "new_image"
    return img_name


def verify_directory():
    if not os.path.exists("images"):
        os.mkdir("images")


if __name__ == "__main__":
    menu()

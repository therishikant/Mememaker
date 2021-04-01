import os
import instaloader
from instaloader import Post
from FW import makeMemeWebImage



def deleteALlTXT():
    directory = "postIG"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if (file.endswith(".txt"))]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)
    filtered_files_zip = [file for file in files_in_directory if (file.endswith(".xz"))]
    for file in filtered_files_zip:
        path_to_file_zip = os.path.join(directory, file)
        os.remove(path_to_file_zip)

def saveImageFromIG(url, templateName):
    shortedUrl = url.split('/')[4]
    print(shortedUrl)
    print(os.getcwd())
    i = instaloader.Instaloader()
    print(os.getcwd())
    post = Post.from_shortcode(i.context, shortedUrl)
    os.chdir('E:/Animatedtimes/Meme Maker Automation/V2')
    i.download_post(post, target='postIG')
    deleteALlTXT()
    os.chdir('postIG')
    webImage = os.listdir()
    for i in range(len(webImage)):
        os.chdir('../postIG')
        makeMemeWebImage(webImage[i], templateName)
        os.chdir('../postIG')
        os.remove(webImage[i])


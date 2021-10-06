#Module 12 Class Activity 5
#Robert Bayer
#The Program will open all of my social medias in one click
import webbrowser as wb

def main():
    chromelocation = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    socialmedias = ["facebook.com", "instagram.com", "myspace.com", "snapchat.com", "linkedin.com", "twitter.com", "tiktok.com"]

    for media in socialmedias:
        wb.get(chromelocation).open_new_tab(media)

main()
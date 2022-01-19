from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube  import YouTube
import re
import urllib.request as urllib2


def checkUrl():
    global correctUrl
    correctUrl =0

    ytUrl = 'https://www.youtube.com'

    urlcompile = re.compile('^https://www.youtube.com/watch?')
    url = getUrl.get().strip()
    
    if url is None or url == '' or not url :
        messagebox.showerror ("Error", "Enter url ")
        return None

    try:
        urllib2.urlopen(ytUrl, timeout=2)

    except urllib2.URLError: 
        messagebox.showerror ("Error", "No Internet connection! ")
        return None     

    if urlcompile.match(url) is not None :
        correctUrl = 1
        return correctUrl

    else :
        messagebox.showerror("Error", "It is not the youtube url format. ")    


# ------------------------------------------------------------------------------------------------
def clickDownload():

    select = listbox.curselection()
 
    if select == ():
        messagebox.showerror("Error", "Select one quality or press Video/Audio button to see the available qualities ")
        return None
            

    save = getLocation.get().strip()

    if save is None or save == '' or not save :
        messagebox.showerror("Error", "Select the directory ")
        return None    

    quality = qlistbox[select[0]]
    quality.download(save)
    messagebox.showinfo("Result", "Your file has been downloaded sucessfully! ")


# ------------------------------------------------------------------------------------------------
def clickVideo():
    url = getUrl.get()
    cUrl = checkUrl()

    if cUrl ==1:   
        global yt
        yt = YouTube(url)
        # print(yt.title)

        listbox.delete(0,END)
    
        global qlistbox
        qlistbox = yt.streams.filter(progressive=True)

        count = 1
        for v in qlistbox:
            listbox.insert(END, str(count)+") "+str(v)+"\n\n")
            count += 1


# ------------------------------------------------------------------------------------------------
def clickAudio():
    url = getUrl.get()
    cUrl = checkUrl()

    if cUrl ==1: 
        global yt
        yt = YouTube(url)
        # print(yt.title)

        listbox.delete(0,END)

        global qlistbox
        qlistbox = yt.streams.filter(only_audio=True)

        count = 1
        for a in qlistbox:
            listbox.insert(END, str(count)+") "+str(a)+"\n\n")
            count += 1


# ------------------------------------------------------------------------------------------------
def clickBrowse():
    location_of_download = filedialog.askdirectory()
    getLocation.set(location_of_download)


# ------------------------------------------------------------------------------------------------
def clickReset():
    getUrl.set("")
    getLocation.set("")
    listbox.delete(0,END)


# ------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    root = Tk()
    root.title("YouTube Video and Audio Dowloader")
    root.iconbitmap("youtube.ico")
    root.geometry("933x658")
    root.configure(bg='#322E41')
    root.resizable(False, False)

    img = PhotoImage(file = r"img.png")
    imageLabel      = Label(root, image = img).grid(row=0, column=0, padx=10, pady=10)

    nameLabel       = Label(root, text="YouTube Video and Audio Downloader", bg='#322E41' , fg = "#E10000" , font=("Century Gothic",23,"bold")).grid(row=0, column=1, padx=10, pady=10)
    urlLabel        = Label(root, text="Url"                               , bg='#322E41' , fg = "#F0F0F0" , font=("Century Gothic",14,"bold")).grid(row=1, column=0, padx=10, pady=10)
    qualityLabel    = Label(root, text="Select Quality"                    , bg='#322E41' , fg = "#F0F0F0" , font=("Century Gothic",14,"bold")).grid(row=3, column=0, padx=10, pady=10 , sticky=NW)
    locationLabel   = Label(root, text="Location"                          , bg='#322E41' , fg = "#F0F0F0" , font=("Century Gothic",14,"bold")).grid(row=4, column=0, padx=10, pady=10)


    getUrl = StringVar()
    getLocation = StringVar()


    urlEntry      = Entry(root, font=("Century Gothic",14,"bold"), textvariable = getUrl     , width = 53, bd=3, relief=SOLID, borderwidth=0 , bg='#F0F0F0').grid(row=1,column=1, padx=10, pady=10)
    locationEntry = Entry(root, font=("Century Gothic",14,"bold"), textvariable = getLocation, width = 53, bd=3, relief=SOLID, borderwidth=0 , bg='#F0F0F0').grid(row=4,column=1, padx=10, pady=10)

    xScroll = Scrollbar(root, orient=HORIZONTAL)
    xScroll.grid(row=3, column=1 ,padx=10, sticky=E+W+S)

    listbox  = Listbox(root, font=("Century Gothic",14,"bold"), width =53, height = 14 , bd=3, relief=SOLID, borderwidth=0 , bg='#F0F0F0')
    listbox.grid(row=3,column=1, padx=10, pady=10)

    xScroll.config(command = listbox.xview)

    videoButton     = Button(root, text = "Video"        , bg='#F0F0F0' , font=("Century Gothic",14,"bold"), width=12, relief=SOLID, borderwidth=0, command=clickVideo   ).grid(row=1, column=2, padx=10, pady=10)
    audioButton     = Button(root, text = "Audio"        , bg='#F0F0F0' , font=("Century Gothic",14,"bold"), width=12, relief=SOLID, borderwidth=0, command=clickAudio   ).grid(row=2, column=2, padx=10, pady=10)
    browseButton    = Button(root, text = "..."          , bg='#F0F0F0' , font=("Century Gothic",14,"bold"), width=12, relief=SOLID, borderwidth=0, command=clickBrowse  ).grid(row=4, column=2, padx=10, pady=10)
    downloadButton  = Button(root, text = "Download"     , bg='#F0F0F0' , font=("Century Gothic",14,"bold"), width=12, relief=SOLID, borderwidth=0, command=clickDownload).grid(row=5, column=1, padx=10, pady=10)
    resetButton     = Button(root, text = "Clear fields" , bg='#F0F0F0' , font=("Century Gothic",14,"bold"), width=12, relief=SOLID, borderwidth=0, command=clickReset   ).grid(row=5, column=2, padx=10, pady=10)




    root.mainloop()


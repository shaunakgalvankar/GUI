#this is one from the series of learning making GUI's using tkinter
import tkinter 

root=tkinter.Tk()
#intitiating the tkinter object


#this defines the function for the process to be executed after clicking on b1
def alert():
	print("Oh no You cannot click on the master")


#this creates a button with the text from the arguements
b1=tkinter.Button(root,text="Shaunak Galvankar",command = alert )



b1.pack()
root.mainloop()
#this keeps the GUI running till we click the quit button

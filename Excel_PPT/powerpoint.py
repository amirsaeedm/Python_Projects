import win32com.client

PPTApp = win32com.client.Dispatch("PowerPoint.Application")
#Below command will work if instace is already open,this runs faster
#PPTApp = win32com.client.GetActiveObject("PowerPoint.Application")

print(PPTApp)
print(PPTApp.OperatingSystem)
print(PPTApp.Path)
print(PPTApp.ProductCode)

#PPTPres = PPTApp.Presentations.Open(r"D:\Python_Projects\Excel_PPT\Test.pptx")
#PPTPres = PPTApp.Presentations(1)  #Index 1 and so on will refer to already open ppts in order they were opened
PPTPres = PPTApp.Presentations("Test.pptx")  # refer to alreay open pptName.pptx

print(PPTPres.Name)
print(PPTPres.Path)

# Methods for PPTPres Opbject
# PPTPres.Save()

# Working with font collection in the selected ppt
for font in PPTPres.Fonts:
	print(font.Name)
	print(font.Size)
	print(font.Italic)

# Create a reference to a Slide
PPTSlide1 = PPTPres.Slides(1)
PPTSlide2 = PPTPres.Slides(2)
print(PPTSlide1.Name)
print(PPTSlide2.Name)


# Loop through all slides in a presentation
for PPTSlide in PPTPres.Slides:
	print(PPTSlide.Name)
	print(PPTSlide.Shapes.Count)
	print(PPTSlide.SlideID)

# Create Reference to a Shape
PPTShape1 = PPTSlide1.Shapes(1)
PPTShape2 = PPTSlide2.Shapes(1)
print(PPTShape1.Name)
print(PPTShape2.Name)

# Manipulate shape in a Slide
# Select desired shape and then put in shape range object
PPTShape2.Select()  # For this method to work, ppt should be open and this slide should be selected
ShpRng = PPTApp.ActiveWindow.Selection.ShapeRange
print(ShpRng)

# Set Dimentions of shape range
ShpRng.Height = 200
ShpRng.Width = 400
ShpRng.Top = 600
ShpRng.Left = 200
ShpRng.Align(1,1) 
ShpRng.Align(4,1) 
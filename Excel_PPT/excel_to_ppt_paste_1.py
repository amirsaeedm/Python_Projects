import win32com.client

# Create new sinstance of Excel
ExcelApp = win32com.client.Dispatch("Excel.Application")
ExcelApp.Visible = True

# Open Excel Workbook
workbook = ExcelApp.Workbooks.Open(r"D:\Python_Projects\Excel_PPT\Test_sheet.xlsx")

# Loop through all names Ranges in ExcelWorkbook and save in a Dictionary
RangeDict = {}
for namedRng in workbook.Names:
	rngIndex = namedRng.Index
	rngName = namedRng.Name
	RangeDict[rngIndex] = rngName

print(RangeDict)

# Create a New instance of PowerPoint
PPTApp = win32com.client.Dispatch("PowerPoint.Application")
PPTApp.Visible = True

# Create new Presenation
PPTPresentation = PPTApp.Presentations.Open(r"D:\Python_Projects\Excel_PPT\Test.pptx")

# Loop Through each item in dictionary, add as slide, copy range and paste in slide
for key, value in RangeDict.items():
	#PPTSlide = PPTPresentation.Slides.Add(Index = (key+1) ,Layout = 1) # 12 is blank layout
	PPTSlide = PPTPresentation.Slides(key+1) # Create Reference to a Slide

	ExcelApp.Range(value).Copy()
	# Paste in slide as Linked OLEObject
	PPTSlide.Shapes.PasteSpecial(DataType = 10, Link = True) # 10 is OLEObject

	ShpRng = PPTApp.Selection.ShapeRange
	ShpRng.Height = 200
	ShpRng.Width = 400
	ShpRng.Top = 600
	ShpRng.Left = 200
import pandas



def MapExcelData(file):

    """
        Import data from Excel Or CSV Files
    """

    # xl = pandas.ExcelFile(data)
    # print(xl.sheet_names)
    # tmp = xl.parse('Sheet1')

    # CSV Files
    # csv = pandas.read_csv(data, header=None, sep=' ', dtype={0:float, 1:float})

    # Excel Files
    data = pandas.read_excel(file, header=None, dtype={0: float, 1: float})

    data.to_excel('aaa.xlsm')


    DataList = data.get_values()

    print("Data Imported")
    return DataList




data = MapExcelData("Untitled.xlsx")



print(data)

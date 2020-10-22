class IOOperations:
    
    
    '''
    For managing operations from JSON to CSV/Excel etc...

    '''
    pass
    

    def __init__(self, json):
        self.wb = Workbook()
        self.sheet1 = self.wb.add_sheet('Sheet 1')
        self.json = json
        self.key_order = ['title', 'company', 'salary', 'location', 'description']
        self.current_row = 1
   
   
    
    def json_to_excel(self, json):
        pass
    
    
    def add_column(self, arr):
        '''
        Adds column to excel file
        '''
        
        for i in range(len(arr)):
            self.sheet1.write(0, i, arr[i])
        
        
    def add_row(self, arr):
        for i in range(len(arr)):
            self.sheet1.write(self.current_row, i, arr[i])
            
        self.current_row += 1
        
    
    
    
    def add_rows(self, arr_2d):
        for arr in arr_2d:
            self.add_row(arr)
        
    def save(self, path = None):
        if path == None:
            self.wb.save('test.xls')

        else:
            self.wb.save(path)


       
       
    def json_to_list(self,):
       
        data = []
       
        def dict_to_list(dictionary):
            return [dictionary[key] for key in self.key_order]
       
       
        for dic in self.json:
            data.append(dict_to_list(dic))
       
        
        return data

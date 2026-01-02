import json

class LogAnalyzer:
    """
    Class has 2 things:
    data members (Variables) & member functions (functions)
    """

    def __init__(self, file_name, output_file):
        self.log_count ={
        "INFO": 0,
        "WARNING": 0,
        "ERROR" :0
    }
        self.file_name = file_name
        self.output_file = output_file

        

    def read_logs(self):
        with open(self.file_name,"r") as file:
            return file.readlines()
    
    def analyzer(self): 
    #pdb.set_trace()
        lines = self.read_logs()
        for line in lines:
            if "INFO" in line:
                self.log_count.update({"INFO" : self.log_count["INFO"] + 1})
            elif "WARNING" in line:
                self.log_count.update({"WARNING" :  self.log_count["WARNING"] + 1 })
            elif "ERROR" in line:
                self.log_count.update({"ERROR" : self.log_count["ERROR"]+1})
            else:
                pass
        return self.log_count
    
    def write_json(self,counts):
        with open(self.output_file, "w") as json_file:
            json.dump(counts, json_file)


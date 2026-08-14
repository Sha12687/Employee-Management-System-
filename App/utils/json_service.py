import json 

class JsonService:
    
    @staticmethod
    def read_file(file_path):
        with open(file_path,"r") as file:
            data=json.load(file)
            return data
        
    @staticmethod
    def write_file(file_path,data):
        with open(file_path,"w") as file:
            json.dump(data,file,indent=4)
   
        
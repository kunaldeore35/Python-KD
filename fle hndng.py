

class File_operations():
    def __init__(self,fname,data,adata):
        self.fname= fname
        self.data= data
        self.adata = adata
    def create(self):
        f = open(self.fname, "w")
        f.close()
    def write(self):
        f = open(self.fname, "w+")
        date_time = self.cur_time()
        f.write("{},{}".format(date_time,self.adata))
        f.close()
    def append(self):
        f = open(self.fname, "a")
        f.write(self.adata)
        f.close()
    def cur_time(self):
        from datetime import datetime
        times = datetime.now()
        current_time = times.strftime("%H:%M:%S")
        current_date = times.date()
        return f"{current_time}  {current_date}"

    def read(self):
        f = open(self.fname, "r")
        r = f.read()
        f.close()
        return r

c = File_operations("File2.txt","Hi this is File One", "This is appended data")

print(c.write())
class Reportable:
    def to_report_line(self):
        try:
            with open("file.txt","w") as file:
                file.write(self)
        except:
            raise "Not curect"

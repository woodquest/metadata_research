class Dataset:
    def __init__(self):
        self.datasets = ["df1", "df2", "df3", "df4"]

    def printdatasets(self):
        print("printing the datasets for this class")
        for dataset in self.datasets:
            print("\t%s " % dataset)

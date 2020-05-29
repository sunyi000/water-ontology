import configparser
import pandas as pd

def main():

    data = pd.read_csv("C:/Users/ysun/Documents/griffith/water-data/data-all-clean-011-train.csv")
    eventlbl = []

    oldTurb = 0
    for i,row in data.iterrows():
        turb = row["turbidity"]

        if float(turb)>float(oldTurb):
            inc = True
        else:
            inc = False

        if (row["pHFlag"] == "low" and row["turbFlag"] == "high" and row["condFlag"] == "high") or \
                (row["pHFlag"] == "low" and row["turbFlag"] == "high" and row["doFlag"] == "high" and row["tempFlag"]=="high") or \
        (row["pHFlag"] == "low" and row["doFlag"] == "high" and row["condFlag"] == "high") or \
            (row["pHFlag"] == "high" and row["doFlag"] == "high" and row["condFlag"] == "high" and inc == True):

            eventlbl.append('IndustryDischarge')
        elif (row["tempFlag"] == "low" and row["doFlag"] == "high" and row["condFlag"] == "low") or \
                (row["tempFlag"] == "low" and row["turbFlag"] == "high" and row["condFlag"] == "low"):
            eventlbl.append('HeavyRainfall')
        else:
            eventlbl.append('NormalEvent')

        oldTurb = turb



    data['event']=eventlbl

    iddata = data.loc[data['event'] == "IndustryDischarge"]
    print (iddata)
    iddata.to_csv('id-event.csv')

if __name__ == "__main__":
    main()
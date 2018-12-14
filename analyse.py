import pandas as pd
import operator
import matplotlib.pyplot as plt
import json

xy = {}
length = {}

def linegraph(length, years, region, fmt):
    avgl = []
    for year in years:
        avgl.append(sum(length[region+str(year)])/len(length[region+str(year)]))
    return plt.plot(years, avgl, fmt, label=region)

def coordinate(team, reg_year):
    for kill in team:
        if isinstance(kill[4], int) and isinstance(kill[5], int):
            if reg_year+' before 20 minutes' not in xy:
                xy[reg_year+' before 20 minutes'] = []
            if reg_year+' after 20 minutes' not in xy:
                xy[reg_year+' after 20 minutes'] = []
            if kill[0] <= 20:
                xy[reg_year+' before 20 minutes'].append((kill[4], kill[5]))
            else:
                xy[reg_year+' after 20 minutes'].append((kill[4], kill[5]))

def main():
    url = r'C:\Users\USER\Documents\GitHub\League-of-Legends-Death-Point\LeagueofLegends.csv'
    #you can change location to be your location in your computers
    #or use(not recommend if you have poor internet) ===> url = 'https://github.com/biogolf/League-of-Legends-Death-Point/raw/master/LeagueofLegends.csv'
    df = pd.read_csv(url)

    for index, row in df.iterrows():
        row1b = json.loads(row['bKills'].replace("'",'"'))
        row1r = json.loads(row['rKills'].replace("'",'"'))
        reg_year = row['League']+str(row['Year'])
        coordinate(row1b, reg_year)
        coordinate(row1r, reg_year)

        if reg_year not in length:
            length[reg_year] = []
        length[reg_year].append(row['gamelength'])

    xlength_years = [2015,2016,2017,2018]
    print(sorted(length.keys()))
    fmt = '-o'
    plt.style.use('ggplot')
    plt.xlabel('Year')
    plt.ylabel('Time(minutes)')
    plt.title('Average Game Length')
    linegraph(length, [2016, 2017, 2018], "CBLoL", fmt)
    linegraph(length, [2015, 2016, 2017, 2018], "EULCS", fmt)
    linegraph(length, [2015, 2016, 2017, 2018], "LCK", fmt)
    linegraph(length, [2015, 2016, 2017, 2018], "LMS", fmt)
    linegraph(length, [2015, 2016, 2017, 2018], "NALCS", fmt)
    linegraph(length, [2016, 2017, 2018], "OPL", fmt)
    linegraph(length, [2015, 2016, 2017, 2018], "TCL", fmt)
    linegraph(length, [2015, 2016, 2017], "WC", '--x')
    plt.legend()
    plt.show()

    lyears = sorted(xy.keys())
    lyears.remove("WC2014 before 20 minutes")
    lyears.remove("WC2014 after 20 minutes")
    for year in lyears:
        total = len(xy[year])
        plt.scatter([coor[0] for coor in xy[year]], [coor[1] for coor in xy[year]], label="test", color="k", s=0.8)
        plt.title("League-of-Legends-Death-Point %s\nTotal Kills = %d" %(str(year), total))
        plt.show()

main()

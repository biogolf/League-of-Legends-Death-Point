import pandas as pd
import operator
import matplotlib.pyplot as plt
import json

xy = {} #dictionary that collect death points of each region and each year
length = {} #dictionary that collect all games length of each region and each year

def linegraph(length, years, region, fmt):
    """To plot a line of each Region and each Year
    length = data of lenght of all games
    years = list of years that each region has
    region = each region
    fmt = format line graph"""
    avgl = []
    for year in years:
        avgl.append(sum(length[region+str(year)])/len(length[region+str(year)]))
    return plt.plot(years, avgl, fmt, label=region)

def coordinate(team, reg_year):
    """To separate the death points of each regions and each years by 20 minutes
    team = kill of each team in each matches
    reg_year = each regions and each years"""
    bf = ' before 20 minutes'
    af = ' after 20 minute'
    for kill in team:
        if isinstance(kill[4], int) and isinstance(kill[5], int):
            if reg_year+bf not in xy:
                xy[reg_year+bf] = []
            if reg_year+af not in xy:
                xy[reg_year+af] = []
            if kill[0] <= 20:
                xy[reg_year+bf].append((kill[4], kill[5]))
            else:
                xy[reg_year+af].append((kill[4], kill[5]))

def main():
    url = r'C:\Users\USER\Documents\GitHub\League-of-Legends-Death-Point\LeagueofLegends.csv'
    #you can change location to be your location in your computers
    #or use(not recommend if you have poor internet) ===> url = 'https://github.com/biogolf/League-of-Legends-Death-Point/raw/master/LeagueofLegends.csv'
    df = pd.read_csv(url)

    for index, row in df.iterrows():
        row1b = json.loads(row['bKills'].replace("'",'"'))
        row1r = json.loads(row['rKills'].replace("'",'"'))
        reg_year = row['League']+str(row['Year'])
        if row['Year'] == 2014 or row['League'] == "CLS" or row['League'] == "IEM" or row['League'] == "LCL" or\
        row['League'] == "LJL" or row['League'] == "LLN" or row['League'] == "MSI" or row['League'] == "RR":
            pass #To avoid the data of small regions, some matches of 2014
        else:
            coordinate(row1b, reg_year)
            coordinate(row1r, reg_year)

        if reg_year not in length:
            length[reg_year] = []
        length[reg_year].append(row['gamelength'])

    #plot game average in line graph
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

    #plot death point in scatter graph
    lyears = sorted(xy.keys())
    for year in lyears:
        total = len(xy[year])
        plt.scatter([coor[0] for coor in xy[year]], [coor[1] for coor in xy[year]], color="k", s=1)
        plt.title("League-of-Legends-Death-Point %s\nTotal Kills = %d" %(str(year), total))
        plt.show()

main()

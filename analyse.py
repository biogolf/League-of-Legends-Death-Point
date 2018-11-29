import pandas as pd
import operator
import matplotlib.pyplot as plt
def main():
    url = 'https://github.com/biogolf/League-of-Legends-Death-Point/raw/master/kills.csv'
    #url = r'C:\Users\USER\Documents\GitHub\League-of-Legends-Death-Point\kills.csv'
    url2 = r'C:\Users\USER\Documents\GitHub\League-of-Legends-Death-Point\matchinfo.csv'
    df = pd.read_csv(url)
    x = list(df['x_pos'])
    y = list(df['y_pos'])
    x_pos = []
    y_pos = []
    killer = {}

    #Saving the (x,y) in the xy_pos
    for i in range(len(x)):
        if not isinstance(x[i], str):
            x[i] = str(x[i])
        if not isinstance(y[i], str):
            y[i] = str(y[i])
        if x[i].isdigit() and y[i].isdigit():
            x_pos.append(int(x[i]))
            y_pos.append(int(y[i]))

    #Counting kills of the players and saving in dict killer
    for j in list(df['Killer']):
        if j not in killer:
            killer[j] = 1
        else:
            killer[j] += 1

    sorted_killer = sorted(killer.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_killer[0:5]) #Test print

    plt.scatter(x_pos, y_pos, label="test", color="k", s=0.002)
    plt.title("League-of-Legends-Death-Point")

    plt.show()
main()

def main():
    import pandas as pd #this is how I usually import pandas
    import operator
    url = 'https://github.com/biogolf/League-of-Legends-Death-Point/raw/master/kills.csv'
    df = pd.read_csv(url)
    x = list(df['x_pos'])
    y = list(df['y_pos'])
    xy_pos = []
    killer = {}
    for i in range(len(x)):
        if not isinstance(x[i], str):
            x[i] = str(x[i])
        if not isinstance(y[i], str):
            y[i] = str(y[i])
        if x[i].isdigit() and y[i].isdigit():
            xy_pos.append((x[i], y[i]))
    print(xy_pos[0:5])

    for j in list(df['Killer']):
        if j not in killer:
            killer[j] = 1
        else:
            killer[j] += 1

    sorted_killer = sorted(killer.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_killer[0:5])
main()

def main()
    import pandas as pd #this is how I usually import pandas
    import operator
    url = r'https://github.com/biogolf/League-of-Legends-Death-Point/raw/master/kills.csv'
    df = pd.read_csv(url)
    x = list(df['x_pos'])
    x_pos = []
    killer = {}
    for i in x:
        if not isinstance(i, str):
            i = str(i)
        if i.isdigit():
            x_pos.append(i)
    print(x_pos[0:5])

    for j in list(df['Killer']):
        if j not in z:
            killer[j] = 1
        else:
            killer[j] += 1

    sorted_killer = sorted(killer.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_killer[0:5])
main()

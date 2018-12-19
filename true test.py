
import csv

filename = 'YGO_Cards_v2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)



    card_names = []
    defense_stats = []
    attack_stats = []
    ad_above_2k = []
    d_above_2k = []
    d_below_2k = []
    ad_below_2k = []
    a_above_2k = []
    a_below_2k = []
    unknown_stats = []
    num = 0

    for row in reader:
        try:
            card_names.append(row[0])
            defense_stats.append(row[3])
            attack_stats.append(row[1])
        except:
            print("Fatal Error")
    while num <= 5948:
        print(card_names[num], attack_stats[num], defense_stats[num])
        try:
            if card_names[num].startswith('A'):
                if int(defense_stats[num]) >= 2000:
                    try:
                        if int(attack_stats[num]) >= 2000:
                            ad_above_2k.append(card_names[num])
                        elif int(attack_stats[num]) <= 2000:
                            d_above_2k.append(card_names[num])
                    except:
                        d_above_2k.append(card_names[num])
                else:
                    try:
                        if int(attack_stats[num]) >= 2000:
                            d_below_2k.append(card_names[num])
                        elif int(attack_stats[num]) <= 2000:
                            ad_below_2k.append(card_names[num])
                    except:
                        d_below_2k.append(card_names[num])
        except:
            try:
                if int(attack_stats[num]) >= 2000:
                    a_above_2k.append(card_names[num])
                elif int(attack_stats[num]) <= 2000:
                    a_below_2k.append(card_names[num])
            except:
                unknown_stats.append(card_names[num])
        num += 1
    print(ad_above_2k)
    print(d_above_2k)
    print(d_below_2k)
    print(ad_below_2k)
    print(a_above_2k)
    print(a_below_2k)
    print(unknown_stats)
import pandas as pd

# Updating name of the source from url to domain name
def mani(s):
    if 'facebook' in s:
        return 'facebook'
    elif 'google' in s:
        return 'google'
    elif 'instagram' in s:
        return 'instagram'
    else:
        return s

# Reading google analytics data
d = pd.read_csv('ga_daily.csv')

lis = d.values.tolist()
date = ['Dates']
sour = ['Sources']
sessions = [0]
dateSor = [0]
ordquant = [0]
users = [0]
trans = [0]
rev = [0]
tpu = [0]
cur = 0

# Extracting different required info from google analytics
for i in range(len(lis)):
    a = str(lis[i][0]) + '+' + mani(str(lis[i][2]))
    if a not in dateSor:
        date.append(str(lis[i][0]))
        sour.append(mani(str(lis[i][2])))
        dateSor.append(a)
        sessions.append(int(lis[i][4]))
        ordquant.append(int(lis[i][11]))
        users.append(int(lis[i][6]))
        trans.append(int(lis[i][7]))
        rev.append(int(lis[i][10]))
        tpu.append(int(lis[i][-1]))
        cur += 1      
    else:
        ind = dateSor.index(a)
        sessions[ind] += int(lis[i][4])
        ordquant[ind] += int(lis[i][11])
        users[ind] += int(lis[i][6])
        trans[ind] += int(lis[i][7])
        rev[ind] += int(lis[i][10])
        tpu[ind] += int(lis[i][-1])

# Extracting required info from fb publisher platform data
pub = pd.read_csv('fb_daily_publisher_platform.csv')
adDate = list(pub['date_start'])
sp = list(pub['spend'])
plat = list(pub['publisher_platform'])
for i in range(len(plat)):
    if plat[i] == 'audience_network':
        plat[i] = 'facebook'
spend = [0] * (len(dateSor))
for i in range(len(plat)):
    if plat[i] == 'facebook' or plat[i] == 'instagram':
        b = adDate[i]+"+"+plat[i]
        idx = dateSor.index(b)
        print(idx)
        spend[idx] += sp[i]


# Finally merging the extracted data into a Data Frame
c = pd.DataFrame()
c['Sources'] = sour[1:]
c['Date'] = date[1:]
c['Sessions'] = sessions[1:]
c['Users'] = users[1:]
c['Transactions'] = trans[1:]
c['Revenue'] = rev[1:]
c['Order Quantity'] = ordquant[1:]
c['Transactions Per User'] = tpu[1:]
c['Amount Spent'] = spend[1:]


# Inserting the data frome into a csv
c.to_csv('task1Ans.csv')

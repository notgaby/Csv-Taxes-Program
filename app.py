import pandas as pd
import os
pd.set_option('display.expand_frame_repr', False)

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
year = '2019'

#Each month = one position
net = [0] * 12
sale = [0] * 12
ads = [0] * 12
fees_and_taxes = [0] * 12


#vals for each month
net_month = 0
sale_month = 0
fees_and_taxes_month = 0
ads_month = 0
month_counter = 0


def total(values):
    total_values = 0
    for i in values:
        total_values+=i

    return total_values

for month in months:
    targetFile = pd.read_csv(os.path.expanduser('~/Desktop/Etsy/'+year+'/'+month+'_'+year+'.csv'))

    for index, row in targetFile.iterrows():
        if(row['Type'] == 'Sale'):
            amount_temp = float(row['Amount'].replace('$',''))
            net_temp = float(row['Net'].replace('$',''))

            sale_month+= amount_temp
            net_month+= net_temp


        elif(row['Type'] != 'Deposit'):

            if(row['Type'] == )
            fees_temp = float(row['Fees & Taxes'].replace('\U00002013', '-').replace('$',''))

            fees_and_taxes_month+= fees_temp
            net_month+= fees_temp

    net[month_counter] = net_month
    sale[month_counter] = sale_month
    fees_and_taxes[month_counter] = fees_and_taxes_month

    net_month = 0
    sale_month = 0
    fees_and_taxes_month = 0
    month_counter+=1


#calculating for the whole year

total_sales = round(total(sale),2)
total_net = round(total(net),2)
total_fees_and_taxes = round(total(fees_and_taxes),2)

print(total_net)
print(total_sales)
print(total_fees_and_taxes)

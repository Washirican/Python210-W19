#!/usr/bin/env python3
# ---------------------------------------------------------------- #
# Title: The Mailroom Part 1
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-01-28, Initial release
# ---------------------------------------------------------------- #

# -- Data -- #
# Read donor data from csv file
objDonations = open('Donations_List.csv', 'r')
lstDonations = []
for donation in objDonations:
    lstDonations.append(list((donation.replace('\n', '').split(',')[0],
                              donation.replace('\n', '').split(',')[1],
                              float(donation.replace('\n', '').split(',')[2]),
                              int(1))))
lstDonations.sort()
objDonations.close()


# -- Processing -- #
def last_donation(donor_name):
    lstDonations.sort(key = lambda x: x[1], reverse = True)
    
    for donor in lstDonations:
        # print(donor)
        if donor[0] == donor_name:
            return str(donor[2])
            
            
def thank_you():
    response = input('\nWho do you want to send it to?\n'
                     'Type donor Full Name to send note. Type "list" to display a list of all donor names. ')
    
    # Create list of unique donor names
    lst_unique_donors = []
    for donor in lstDonations:
        if donor[0] not in lst_unique_donors:
            lst_unique_donors.append(donor[0])
    
    # List all existing donors?
    if response.lower() == 'list':
        print('\nThese are all existing donors: ')
        for donor in lst_unique_donors:
            print('*', donor)
        
    else:
        # Check if donor exists ins Donations List
        if response in lst_unique_donors:
            str_last_donation = last_donation(response)
            str_thank_you_note = input('\n' + response + ' is already a donor.\nDo you want to send a "Thank You" note'
                                                  ' for his latest donation of $' + str_last_donation + '? '
                                                  'Type "yes" or "no": ')
            if str_thank_you_note == 'yes':
                print('\n\nDear ', response.title(), ',\n\nThank you for your generous donation of $', '{:.2f}'.format(float(str_last_donation)),
                      '!\n\nSincerely,\nBill Gates\n\n', sep='')
        
        # Add new donation
        else:
            print('\nAdding donation from', response.title(), 'to Donations List.')
            str_new_name = response.title()
            str_date = input('Enter donation date (m/d/yyy): ')
            flt_donation = input('Enter donation amount ($): ')
            lstDonations.append(list((str_new_name, str_date, float(flt_donation), int(1))))
    return 0


def donor_report():
    lstDonations.sort()
    lstDonationsSummary = []
    bolExistingDonor = False
    
    for donor in lstDonations:
        if len(lstDonationsSummary) == 0:
            lstDonationsSummary.append(list((donor[0], donor[2], 1, 0)))
        else:
            for y in range(len(lstDonationsSummary)):
                bolExistingDonor = False
                if donor[0] == lstDonationsSummary[y][0]:
                    lstDonationsSummary[y][1] += float(donor[2])
                    lstDonationsSummary[y][2] += 1
                    
                    bolExistingDonor = True
            if not bolExistingDonor:
                lstDonationsSummary.append(list((donor[0], donor[2], donor[3], 0)))
    
    # Calculate averages
    for donor in lstDonationsSummary:
        donor[3] = donor[1] / donor[2]
    
    print('=============================================================================================================')
    print('Donation Summary Table')
    print('--------------------------------------------------------------------------------------------------------------')
    print('{:25}{:20}{:10}{:20}'.format('Name', 'Donation', 'Count', 'Avg'))
    for donorSummary in lstDonationsSummary:
        print('{:20}'.format(donorSummary[0]), '${:20,.2f}'.format(donorSummary[1]), '{:8}'.format(donorSummary[2]),
              '${:,.2f}'.format(donorSummary[3]))
    print('=============================================================================================================')


# -- Presentation (Input/Output) -- #
response = ''
if __name__ == '__main__':
    while response != 'q':
        response = input('\nWhat would you like to do?\n'
                         'Type "1" to send a "Thank You" note; Type "2" to Create a Report or "q" to quit: ')
        if response == '1':
            thank_you()
        elif response == '2':
            donor_report()
           
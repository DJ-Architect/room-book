#!/usr/bin/env python3
from datetime import datetime
from datetime import timedelta
import requests


#Room Booking Codes
room264 = "11208"
room266 = "10438"
room267 = "10437"
room268 = "10436"
room269 = "10435"

#Room booking applicants (2hrs per applicant per day)
anders = ["firstname", "lastname","youremail@algonquinlive.com"]
matt = ["firstname", "lastname", "youremail@algonquinlive.com"]
jules = ["firstname", "lastname", 'youremail@algonquinlive.com']
kevin = ["firstname", "lastname", "youremail@algonquinlive.com"]



#Clock times
nine = "+9:00"
eleven = "+11:00"
twelve = "+12:00"
thirteen = "+13:00"
fourteen = "+14:00"
three = "+15:00"
sixteen = "+16:00"
seventeen = "+17:00"
eighteen = "+18:00"
nineteen = "+19:00"

#Generate the URL parameter to interface with the booking system
def generate_param(applicant, test, start, end):
    first = 'formData[fname]='
    last = '&formData[lname]='
    email = '&formData[email]='
    id = '&bookings[0][id]=1'
    eid = '&bookings[0][eid]=11208'
    gid = '&bookings[0][gid]=2744'
    lid = '&bookings[0][lid]=1534'
    start_param = '&bookings[0][start]='
    end_param = '&bookings[0][end]='
    start_time = start.split(':', 1)
    end_time = end.split(':', 1)
    email_param = applicant[2].split('@', 1)
    parameter = first + applicant[0] + last + applicant[1] + email + email_param[0] + '@'+email_param[1] + id + eid + gid \
                + lid + start_param + test + start_time[0] + ":" + start_time[1] + end_param + test +\
                end_time[0] + ':' + end_time[1]
    print("Parameter generated! " + applicant[0])

    return parameter


#Post the generated parameters to the algonquin booking system
def post(parameters):
    URL = 'https://algonquincollege.libcal.com/ajax/space/book'
    headers ={'Host': 'algonquincollege.libcal.com',
              'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
              'Referer': 'https://algonquincollege.libcal.com/reserve/meeting-rooms',
              'Accept': 'application / json, text / javascript, * / *; q = 0.01',
              'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
              'X-Requested-With': 'XMLHttpRequest',
              'TE': 'Trailers',
              'Content-Type': 'application/x-www-form-urlencoded'}

    for params in parameters:
        res = requests.post(url=URL, data=params, headers=headers)
        print(res.status_code, res.reason, res.content)


def monday(applicant_one, applicant_two, applicant_three, applicant_four,  date):
    print('Generating monday parameters...')
    para_four = generate_param(applicant_four, date,nine, eleven)
    param_one = generate_param(applicant_one, date, eleven, thirteen)
    param_two = generate_param(applicant_two, date, fourteen, sixteen, )
    param_three = generate_param(applicant_three, date, sixteen, eighteen)
    parameters = [param_one, param_two, param_three, para_four]
    for param in parameters:
        print(param)
    post(parameters)


def tuesday(applicant_one,applicant_two, date):
    print('Generating parameters...')
    param_one = generate_param(applicant_one, date, eleven, thirteen)
    param_two = generate_param(applicant_two, date, thirteen, three)
    parameters = [param_one, param_two]
    post(parameters)


def wednesday(applicant_one, applicant_two, applicant_three, date):
    print('Generating parameters...')
    param_one = generate_param(applicant_one, date, eleven, thirteen)
    param_two = generate_param(applicant_two, date, thirteen, three)
    param_three = generate_param(applicant_three, date, three, sixteen)
    parameters = [param_one, param_two, param_three]
    post(parameters)


def thursday(applicant_one, applicant_two, applicant_three, applicant_four, date):
    print('Generating parameters...')
    param_one = generate_param(applicant_one, date, eleven, thirteen)
    param_two = generate_param(applicant_two, date, thirteen, three)
    param_three = generate_param(applicant_three, date, three, seventeen)
    param_four = generate_param(applicant_four, date, seventeen, nineteen)
    parameters = [param_one, param_two, param_three, param_four]
    post(parameters)


def friday(applicant_one, applicant_two, date):
    print('Generating parameters...')
    param_one = generate_param(applicant_one, date, twelve, fourteen)
    param_two = generate_param(applicant_two, date, fourteen, sixteen)
    parameters = [param_one, param_two]
    post(parameters)


if __name__=='__main__':
    currentDT = datetime.now()
    nextDay = currentDT + timedelta(minutes=1)

    #Booking days are 15 days in advance
    fifteen = currentDT + timedelta(days=16)
    date = fifteen.strftime("%Y-%m-%d")

    #Poll till clock strikes the next day
    while currentDT.minute != nextDay.minute:
        currentDT = datetime.now()
    if fifteen.strftime("%A") == 'Monday':
        monday(anders, jules, matt,kevin, date)
    elif fifteen.strftime("%A") == 'Tuesday':
        tuesday(anders, jules, date)
    elif fifteen.strftime("%A") == 'Wednesday':
        wednesday(matt, anders, jules, date)
    elif fifteen.strftime("%A") == 'Thursday':
        thursday(jules, matt, anders, kevin, date)
    elif fifteen.strftime("%A") == 'Friday':
        friday(anders, jules, date)





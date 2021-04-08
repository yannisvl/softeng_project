import click
from click.testing import CliRunner
from energy_group044 import *

#unit tests

def test_login(user, password):
    runner=CliRunner()
    result=runner.invoke(Login, ['--username', user, '--passw', password])
    if len(result.output)>0:
        return "login successful as "+user
    else:
        return "login test failed"

def test_logout():
    runner=CliRunner()
    result=runner.invoke(Logout, [])
    if len(result.output)>0:
        return "logout successful"
    else:
        return "logout test failed"

def test_create_user(name, password, email, quota):
    runner=CliRunner()
    result=runner.invoke(Admin, ['--newuser', name, '--passw', password, '--quota', quota, '--email', email])
    print("When trying to signup with username:"+name+" password:"+password+" quota:"+quota+" email:"+email)
    print(result.output)
    print()


def test_show_user(name):
    runner=CliRunner()
    result=runner.invoke(Admin, ['--userstatus', name])
    if '{"username": "giorgos",' in result.output:
        print("existing user\n"+result.output)
    else:
        print("show user test failed")
        print(result.output)

def test_modify_user(name, password, quota, email):
    runner=CliRunner()
    result=runner.invoke(Admin, ['--moduser', name, '--passw', password, '--quota', quota, '--email', email])
    if 'Successfully Modified' in result.output:
        print ("modify user test successful")
    else:
        print("Trying to modify "+name)
        print(result.output)
        print()

def test_datasets(dataset, area, timeres, date_field, date):
    runner=CliRunner()
    result=runner.invoke(ActualTotalLoad, ['--area', area, '--timeres', timeres, date_field, date, '--format', 'csv'])
    print(result.output)
    print()


def test_aggr(dataset, area, timeres, date_field, date):
    runner=CliRunner()
    result==runner.invoke(DayAheadTotalLoadForecast, ['--area', area, '--timeres', timeres, date_field, date, '--format', 'csv'])
    print(result.output)
    print()


def test_prodtype(area, timeres, date_field, date, prodtype):
    runner=CliRunner()
    if prodtype=='':
        result1=runner.invoke(AggregatedGenerationPerType, ['--area', area, '--timeres', timeres, date_field, date, '--format', 'csv', '--productiontype', 'AllTypes'])
        print(result1.output)
    else:
        result2=runner.invoke(AggregatedGenerationPerType, ['--area', area, '--timeres', timeres, date_field, date, '--format', 'csv', '--productiontype', prodtype])
        print(result2.output)
    print()

print(test_login('admin', 'jack12345'))
print(test_create_user('mpampis', 'mpampis', 'kati@gmail.com', '100'))
print(test_create_user('mpampis', 'stergioy123', 'stergioy123@gmail.com', '100'))
print(test_create_user('mpampis',  'nonos1', 'stergiou123@gmail.com', '100'))
print(test_create_user('mpampis',  'nonostoypaidiou', 'stergiou123@gmail.com', '100'))
print(test_create_user('mpampis',  'nonos35xronwn', 'stergiou123@gmail.com', 'string_quota'))
print(test_logout())
print(test_login('mark', 'xolargos10'))
print(test_create_user('mpampis', 'kalos_kwdikos12', 'katigiamail@gmail.com', '100'))
print(test_logout())
print(test_login('admin', 'jack12345'))

print(test_show_user('giorgos'))
print(test_logout())
print(test_login('mark', 'xolargos10'))

print(test_modify_user('giorgos', 'thrulos7!','200','some_mail@gmail.com'))
print(test_logout())
print(test_login('admin', 'jack12345'))
print(test_show_user('giorgos_den_uparxei'))

print(test_datasets('ActualTotalLoad', 'Moggolia', 'PT60M', '--year', '2018'))
print(test_datasets('ActualTotalLoad', 'Greece', 'PT60M', '--month', '2000-13'))
print(test_datasets('ActualTotalLoad', 'Greece', 'PT60M', '--date', '2018-13-56'))

print(test_prodtype('Moggolia', 'PT60M', '--year', '2018', ''))
print(test_prodtype('Greece', 'PT60M', '--month', '2000-13', ''))
print(test_prodtype('Greece', 'PT60M', '--date', '2018-13-56', ''))

print(test_prodtype('Moggolia', 'PT60M', '--year', '2018', 'Fossil_Gas'))
print(test_prodtype('Greece', 'PT60M', '--month', '2000-13', 'Fossil_Gas'))
print(test_prodtype('Greece', 'PT60M', '--date', '2018-13-56', 'Fossil_Gas'))

#print(test_aggr('DayAheadTotalLoadForecast', 'Moggolia', 'PT60M', '--year', '2018'))
#print(test_aggr('DayAheadTotalLoadForecast', 'Greece', 'PT60M', '--month', '2000-13'))
#print(test_aggr('DayAheadTotalLoadForecast', 'Greece', 'PT60M', '--date', '2018-13-56'))

#correct queries

print(test_datasets('ActualTotalLoad', 'Greece', 'PT60M', '--year', '2018'))
print(test_datasets('ActualTotalLoad', 'Greece', 'PT60M', '--month', '2018-01'))
print(test_datasets('ActualTotalLoad', 'Greece', 'PT60M', '--date', '2018-01-04'))

print(test_prodtype('Greece', 'PT60M', '--year', '2018', ''))
print(test_prodtype('Greece', 'PT60M', '--month', '2018-01', ''))
print(test_prodtype('Greece', 'PT60M', '--date', '2018-01-04', ''))

print(test_prodtype('Greece', 'PT60M', '--year', '2018', 'Fossil_Gas'))
print(test_prodtype('Greece', 'PT60M', '--month', '2018-01', 'Fossil_Gas'))
print(test_prodtype('Greece', 'PT60M', '--date', '2018-01-04', 'Fossil_Gas'))

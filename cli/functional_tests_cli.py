import click
from click.testing import CliRunner
from energy_group044 import *

#functional tests

def test_create_user():
    runner=CliRunner()
    result=runner.invoke(Admin, ['--newuser', 'giorgos', '--passw', 'minos_paok4', '--quota', '100', '--email', 'salonikh@gmail.com'])
    if 'User created successfully' in result.output:
        return "sign-up test successful"
    else:
        return "sign-up test failed"

def test_create_user1():
    runner=CliRunner()
    result=runner.invoke(Admin, ['--newuser', 'mark', '--passw', 'xolargos10', '--quota', '100', '--email', 'softeng@gmail.com'])
    if 'User created successfully' in result.output:
        return "sign-up test successful"
    else:
        return "sign-up test failed"

def test_modify_user():
    runner=CliRunner()
    result=runner.invoke(Admin, ['--moduser', 'giorgos', '--passw', 'thrulos7!', '--quota', '200', '--email', 'some_mail@gmail.com'])
    if 'Successfully Modified' in result.output:
        return "modify user test successful"
    else:
        return "modify user test failed"


def change_quota():
    runner=CliRunner()
    result=runner.invoke(Admin, ['--moduser', 'giorgos', '--passw', 'thrulos7!', '--quota', '0', '--email', 'some_mail@gmail.com'])
    if 'Successfully Modified' in result.output:
        return "change quota test successful"
    else:
        return "change quota test failed"


def test_show_user():
    runner=CliRunner()
    result=runner.invoke(Admin, ['--userstatus', 'giorgos'])
    if '"username": "giorgos"' in result.output:
        return "show user test successful"
    else:
        return "show user test failed"

def test_login():
    runner=CliRunner()
    result=runner.invoke(Login, ['--username', 'admin', '--passw', 'jack12345'])
    if len(result.output)>0:
        return "login test successful"
    else:
        return "login test failed"


def test_login_user():
    runner=CliRunner()
    result=runner.invoke(Login, ['--username', 'giorgos', '--passw', 'thrulos7!'])
    if len(result.output)>0:
        return "login user test successful"
    else:
        return "login user test failed"


def test_logout():
    runner=CliRunner()
    result=runner.invoke(Logout, [])
    if len(result.output)>0:
        return "logout test successful"
    else:
        return "logout test failed"

def test_actual_total_load():
    runner=CliRunner()
    result=runner.invoke(ActualTotalLoad, ['--area', 'Greece', '--timeres', 'PT60M', '--year', '2018', '--format', 'csv'])
    if 'entso-e,ActualTotalLoad,Greece,CTY,GR,PT60M,2018,1,1308759.35' in result.output:
        return "actual total load ok"
    else:
        return "actual total load not ok"

def test_reset():
    runner=CliRunner()
    result=runner.invoke(Reset, [])
    if '{"status": "OK"}' in result.output:
    	return "reset database ok"
    else: 
        return "reset database not ok"

def test_health_check():
    runner=CliRunner()
    result=runner.invoke(HealthCheck, [])
    if '{"status": "OK"}' in result.output:
    	return "health check ok"
    else: 
        return "health check not ok"

def test_say_in_cli():
    runner=CliRunner()
    result=runner.invoke(say, ['--text', 'something'])
    assert 'You said something' in result.output
    assert result.exit_code==0
    return "test test ok"

def test_upload():
    runner=CliRunner()
    result=runner.invoke(Admin, ['--newdata', 'ActualTotalLoad', '--source', 'atl.csv'])
    if '401: Not authorized' in result.output:
        return "indeed, common user not authorized"
    else:
        return "file uploaded"

def test_no_quota_query():
    runner=CliRunner()
    result=runner.invoke(ActualTotalLoad, ['--area', 'Greece', '--timeres', 'PT60M', '--year', '2018', '--format', 'csv'])
    if '402: Out of quota' in result.output:
        return "indeed no quota left"
    else:
        return "query done"

print(test_login())
print(test_actual_total_load())
print(test_create_user())
print(test_create_user1())
print(test_modify_user())
print(test_show_user())
print(change_quota())
print(test_logout())
print(test_login_user())
print(test_upload())
print(test_no_quota_query())
#print(test_reset())
print(test_health_check())
#print(test_say_in_cli())

import os

class FailedTest(Exception):
    pass

#four functional tests are also here to help the flow of unit testing
def T03_Admin_Successful_Login():
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > t3.txt");
        f = open("t3.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm t3.txt");
        os.system(curl_bin + ' -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "csrfmiddlewaretoken='+token+'&username=admin&password=jack12345" -X POST '+login_url+'/ > t3.txt');
        if os.stat("t3.txt").st_size > 0:
            raise FailedTest
        os.system("rm t3.txt");
        print('OK')
    except FailedTest:
        os.system("rm t3.txt");
        print('NOT OK')
        

def T05_User_Successful_Login():
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > t5.txt");
        f = open("t5.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm t5.txt");
        os.system(curl_bin + ' -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "csrfmiddlewaretoken='+token+'&username=user2&password=jack12345" -X POST '+login_url+'/ > t5.txt');
        if os.stat("t5.txt").st_size > 0:
            raise FailedTest
        os.system("rm t5.txt");
        print('OK')
    except FailedTest:
        os.system("rm t5.txt");
        print('NOT OK')  
        

def T09_Admin_Logs_Out():
    try:
        cookies = "softeng19bAPI.token"
        open(cookies,"r")
        os.system("rm "+cookies)
        print('OK')
    except IOError:
        print('Admin is not logged in, NOT OK')
    except:
        print('NOT OK')


def T11_User_Logs_out():
    try:
        cookies = "softeng19bAPI.token"
        open(cookies,"r")
        os.system("rm "+cookies)
        print('OK')
    except IOError:
        print('User is not logged in, NOT OK')
    except:
        print('NOT OK')        

def U01_Login_GET_Failure():
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        os.system(curl_bin + ' -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "csrfmiddlewaretoken='+token+'&username=admin&password=jack12345" -X GET '+login_url+'/ > u.txt');
        if os.stat("u.txt").st_size == 0:
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U02_Signup_GET_Failure(username,password,email,quota):
    #assume adiminstrator is logged in
    #assuming that admin is already logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+str(username)+'&password1='+str(password)+'&password2='+str(password)+'&email='+str(email)+'&quota='+str(quota)+'" -X GET http://localhost:8765/energy/api/admin/users > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        if (line[0] != '4' or line[1] != '0' or line[2] != '0'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U03_Signup_Same_Username_Password(username,password,email,quota):
    #assume adiminstrator is logged in
    #assuming that admin is already logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+str(username)+'&password1='+str(password)+'&password2='+str(password)+'&email='+str(email)+'&quota='+str(quota)+'" -X POST http://localhost:8765/energy/api/admin/users > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        if (line[0] != '4' or line[1] != '0' or line[2] != '0'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U04_Signup_Same_Email_Password(username,password,email,quota):
    #assume adiminstrator is logged in
    #assuming that admin is already logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+str(username)+'&password1='+str(password)+'&password2='+str(password)+'&email='+str(email)+'&quota='+str(quota)+'" -X POST http://localhost:8765/energy/api/admin/users > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        if (line[0] != '4' or line[1] != '0' or line[2] != '0'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U05_Signup_Password_Under_8_Characters(username,password,email,quota):
    #assume adiminstrator is logged in
    #assuming that admin is already logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+str(username)+'&password1='+str(password)+'&password2='+str(password)+'&email='+str(email)+'&quota='+str(quota)+'" -X POST http://localhost:8765/energy/api/admin/users > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        if (line[0] != '4' or line[1] != '0' or line[2] != '0'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')

def U06_Signup_Quota_String(username,password,email,quota):
    #assume adiminstrator is logged in
    #assuming that admin is already logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+str(username)+'&password1='+str(password)+'&password2='+str(password)+'&email='+str(email)+'&quota='+str(quota)+'" -X POST http://localhost:8765/energy/api/admin/users > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        if (line[0] != '4' or line[1] != '0' or line[2] != '0'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U07_Signup_Unsupervised(username,password,email,quota):
    #assume non-admin is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+str(username)+'&password1='+str(password)+'&password2='+str(password)+'&email='+str(email)+'&quota='+str(quota)+'" -X POST http://localhost:8765/energy/api/admin/users > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        if (line[0] != '4' or line[1] != '0' or line[2] != '1'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U08_Signup_Missing_Fields(username,password,email,quota):
    #assume adiminstrator is logged in
    #assuming that admin is already logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+str(username)+'&password1='+str(password)+'&password2='+str(password)+'&email='+str(email)+'" -X POST http://localhost:8765/energy/api/admin/users > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        if (line[0] != '4' or line[1] != '0' or line[2] != '0'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')

def U09_Admin_Creates_New_User(username,password,email,quota):
    #assuming that admin is already logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+str(username)+'&password1='+str(password)+'&password2='+str(password)+'&email='+str(email)+'&quota='+str(quota)+'" -X POST http://localhost:8765/energy/api/admin/users > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        if (line != "User created successfully"):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U10_Modify_Unsupervised(argument):
    #assuming user2 is already logged in, who is not admin
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username=user2&passw=jack12345&email=user2@gmail.com&quota='+str(argument)+'" -X PUT http://localhost:8765/energy/api/admin/users/user2 > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '4' or line[1] != '0' or line[2] != '1'):
            raise FailedTest
        os.system("rm u.txt")
        print('OK')
    except FailedTest:
        os.system("rm u.txt")
        print('NOT OK')
        
def U11_Modify_Without_A_Field():
    #assuming admin is already logged in
    #attempts to run modify information about user2 without email
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username=user2&passw=jack12345&quota='+str(5)+'" -X PUT http://localhost:8765/energy/api/admin/users/user2 > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '3' or line[5]!='9'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U12_Modify_With_POST():
    #assuming admin is already logged in
    #attempts to run modify with POST instead of PUT
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username=user2&passw=jack12345&email=user2@gmail.com&quota='+str(5)+'" -X POST http://localhost:8765/energy/api/admin/users/user2 > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '4' or line[1] != '0' or line[2] != '0'):
            raise FailedTest
        os.system("rm u.txt")
        print('OK')
    except FailedTest:
        os.system("rm u.txt")
        print('NOT OK')
        
def U13_Modify_With_GET():
    #assuming admin is already logged in
    #attempts to run modify with GET
    #information for the user is obtained
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/admin/users/user2 > u.txt'
        os.system(command);
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '{' or line[1]!='"'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U14_Query1A_Wrong_Argument():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/date/he-01-04 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '<' or line[1]!='!'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U15_Query1A_No_Data():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/date/2021-03-29 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '4' or line[1]!='0' or line[2]!='3'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U16_Query1B_Wrong_Argument():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/month/he-01 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '<' or line[1]!='!'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U17_Query1B_No_Data():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/month/2021-03 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '4' or line[1]!='0' or line[2]!='3'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U18_Query1C_Wrong_Argument():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/year/he > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '<' or line[1]!='!'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U19_Query1C_No_Data():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/year/2021 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '4' or line[1]!='0' or line[2]!='3'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
#queries type 2 and 3 are considered the same as type 1, so they are not checked again
        
def U20_Query4A_Wrong_Argument():
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualvsForecast/Greece/PT60M/date/he-01-04 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '<' or line[1]!='!'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U21_Query4A_No_Data():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualvsForecast/Greece/PT60M/date/2021-03-29 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] != '4' or line[1]!='0' or line[2]!='3'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
#queries type 4b and 4c are considered analogous for 4a as queries 1b and 1c were for type 1a, so they are not checked again
        
#correct queries follow
        
def U22_Query1A_Correct():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/date/2018-01-05 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] == '4'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U23_Query1B_Correct():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/month/2018-01 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] == '4'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U24_Query1C_Correct():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/year/2018 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] == '4'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')
        
def U25_Query4A_Correct():
    #assuming admin / user with adequate quota is logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > u.txt");
        f = open("u.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm u.txt")
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualvsForecast/Greece/PT60M/date/2018-01-05 > u.txt'
        os.system(command)
        f = open("u.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line[0] == '4'):
            raise FailedTest
        print('OK')
    except FailedTest:
        print('NOT OK')

print("Logging in with GET failing... " ,end='')
U01_Login_GET_Failure()
print("Administrator logging in... ", end='')
T03_Admin_Successful_Login()
print("Using signup with GET, it must throw certain response... ", end='')
U02_Signup_GET_Failure('value1','latin2493','field3@gmail.com','40')
print("Using signup with same username and password, it must throw certain response... ", end='')
U03_Signup_Same_Username_Password('james3394','james3394','mark@gmail.com','40')
print("Using signup with same email and password, it must throw certain response... ", end='')
U04_Signup_Same_Email_Password('james3394','mark383409','mark383409@gmail.com','40')
print("Using signup with password under 8 characters, it must throw certain response... ", end='')
U05_Signup_Password_Under_8_Characters('james3394','ekrt','mark3982@gmail.com','40')
print("Using signup with quota as a string instead of a number, it must throw certain response... ", end='')
U06_Signup_Quota_String('james3392','ektji48503','ganebr@gmail.com','hello')
print("Administrator logging out... ", end='')
T09_Admin_Logs_Out()
print("User who is not a supervisor logs in... ", end='')
T05_User_Successful_Login()
print("User, who is not a supervisor, tries to use signup, it must throw certain response... ", end='')
U07_Signup_Unsupervised('user39','latin2493','user39@gmail.com','40')
print("User, who is not a supervisor, tries to use modify, it must throw certain response... ", end='')
U10_Modify_Unsupervised('40')
print("User who is not a supervisor logging out... ", end='')
T11_User_Logs_out()
print("Administrator logging in... ", end='')
T03_Admin_Successful_Login()
print("Using signup with some fields missing, it must throw certain response... ", end='')
U08_Signup_Missing_Fields('user40','latin2494','user40@gmail.com','40')
print("Using signup successfully... (this will throw NOT OK if user already exists)... ", end='')
U09_Admin_Creates_New_User('user41','latin2495','user41@gmail.com','40')
print("Using modify with some fields missing, it must throw certain response... ", end='')
U11_Modify_Without_A_Field()
print("Using modify with POST instead of PUT, it must throw certain response... ", end='')
U12_Modify_With_POST()
print("Visiting the user page with GET, it must throw the information about the user... ", end='')
U13_Modify_With_GET()
print("Trying to make Query 1A with a wrong argument, it must throw certain response... ", end='')
U14_Query1A_Wrong_Argument()
print("Trying to make Query 1A and it returning wrong data, it must throw certain response... ", end='')
U15_Query1A_No_Data()
print("Trying to make Query 1B with a wrong argument, it must throw certain response... ", end='')
U16_Query1B_Wrong_Argument()
print("Trying to make Query 1B and it returning wrong data, it must throw certain response... ", end='')
U17_Query1B_No_Data()
print("Trying to make Query 1C with a wrong argument, it must throw certain response... ", end='')
U18_Query1C_Wrong_Argument()
print("Trying to make Query 1C and it returning wrong data, it must throw certain response... ", end='')
U19_Query1C_No_Data()
print("Trying to make Query 4A with a wrong argument, it must throw certain response... ", end='')
U20_Query4A_Wrong_Argument()
print("Trying to make Query 4A and it returning wrong data, it must throw certain response... ", end='')
U21_Query4A_No_Data()
print("Trying to make a correct version of Query 1A... ", end='')
U22_Query1A_Correct()
print("Trying to make a correct version of Query 1B... ", end='')
U23_Query1B_Correct()
print("Trying to make a correct version of Query 1C... ", end='')
U24_Query1C_Correct()
print("Trying to make a correct version of Query 4A... ", end='')
U25_Query4A_Correct()

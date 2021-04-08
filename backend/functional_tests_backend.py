#from models import MyUser
import os

class FailedTest(Exception):
    pass

'''
should be ran only in shell, because of extra permissions requested

def T01_Health_Status_OK():
    try:
        MyUser.objects.filter(username='admin');
        print('OK')
    except:
        print('NOT OK')
    #self.assertIs(AuthUser.objects.filter(username='admin'), True)
    
def T02_Successful_Reset():
    try:
        
    #try:
    #except:
'''
        
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
        
def T04_Admin_Creates_New_User(username,password,email,quota):
    #assuming that admin is already logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > t4.txt");
        f = open("t4.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm t4.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+str(username)+'&password1='+str(password)+'&password2='+str(password)+'&email='+str(email)+'&quota='+str(quota)+'" -X POST http://localhost:8765/energy/api/admin/users > t4.txt'
        os.system(command);
        f = open("t4.txt","r")
        line = f.readline()[:-1]
        f.close()
        os.system("rm t4.txt")
        if (line != "User created successfully"):
            raise FailedTest
        print('OK')
    except FailedTest:
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
        
def T06_User_Retrieves_ActualTotalLoad_For_2018_01_05():
    #user is already logged in. quota diminishment for user is also checked
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > t6.txt");
        f = open("t6.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm t6.txt");
        os.system(curl_bin + ' -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/date/2018-01-05 > t6.txt');
        f = open("t6.txt","r")
        line = f.readline()[:-1]
        if (line[0] != '[' or line[1]!='{'):
            raise FailedTest
        os.system("rm t6.txt")
        print('OK')
    except FailedTest:
        os.system("rm t6.txt");
        print('NOT OK')            
        
def T07_Admin_Limits_Quota_Of_User2_To_Argument(argument):
    #assuming admin is already logged in
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > t7.txt");
        f = open("t7.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm t7.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username=user2&passw=jack12345&email=user2@gmail.com&quota='+str(argument)+'" -X PUT http://localhost:8765/energy/api/admin/users/user2 > t7.txt'
        os.system(command);
        f = open("t7.txt","r")
        line = f.readline()[:-1]
        f.close()
        if (line != "Successfully Modified"):
            raise FailedTest
        os.system("rm t7.txt")
        print('OK')
    except FailedTest:
        os.system("rm t7.txt")
        print('NOT OK')
        
def T08_User2_Cannot_Retrieve_Tuple_Out_Of_Quota():
    #assuming user2 is already logged in and has quota 0
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > t8.txt");
        f = open("t8.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm t8.txt");
        os.system(curl_bin + ' -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET http://localhost:8765/energy/api/ActualTotalLoad/Greece/PT60M/date/2018-01-05 > t8.txt');
        f = open("t8.txt","r")
        line = f.readline()[:-1]
        if (line[0] != '4' or line[1]!='0' or line[2]!='2'):
            raise FailedTest
        os.system("rm t8.txt")
        print('OK')
    except FailedTest:
        os.system("rm t8.txt");
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
        
def T10_User_Tries_To_Upload_ActualTotalLoad_Dataset_in_Argument(argument):
    #assuming user is logged in. user should not be able to upload it, they are not authorized
    try:
        cookies = "softeng19bAPI.token"
        login_url = "http://localhost:8765/energy/api/login"
        curl_bin = "curl -s -c "+cookies+" -b "+cookies+" -e "+login_url
        os.system(curl_bin+"/ "+login_url+"/ > /dev/null");
        os.system("grep csrftoken " +cookies+ " | sed 's/^.*csrftoken\s*//' > t10.txt");
        f = open("t10.txt","r")
        token = f.readline()[:-1]
        f.close()
        os.system("rm t10.txt");
        command = curl_bin + '/ -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X POST -F title=blueberry -F file=@'+argument+' http://localhost:8765/energy/api/admin/ActualTotalLoad > t10.txt'
        os.system(command);
        f = open("t10.txt","r")
        line = f.readline()[:-1]
        if (line[0] != '4' or line[1]!='0' or line[2]!='1'):
            raise FailedTest
        os.system("rm t10.txt")
        print('OK')
    except FailedTest:
        os.system("rm t10.txt")
        print('NOT OK')
    except:
        print('File not found')
        
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
        
print("Admin logging in... ", end='')
T03_Admin_Successful_Login()
print("Admin creating new user... (this will throw NOT OK if user already exists)... ", end='')
T04_Admin_Creates_New_User('user2','jack12345','arthur249@gmail.com','38')
print("Admin logging out... ", end='')
T09_Admin_Logs_Out()
print("User logging in... ", end='')
T05_User_Successful_Login()
print("User (with adequate quota) tries to retrieve ActualTotalLoad for a day with data... ", end='')
T06_User_Retrieves_ActualTotalLoad_For_2018_01_05()
print("User logging out... ", end='')
T11_User_Logs_out()
print("Admin logging in... ", end='')
T03_Admin_Successful_Login()
print("Admin limits quota of user 2 to 1 available query... ", end='')
T07_Admin_Limits_Quota_Of_User2_To_Argument(1)
print("Admin logging out... ", end='')
T09_Admin_Logs_Out()
print("User logging in... ", end='')
T05_User_Successful_Login()
print("User (with adequate quota equal to 1) tries to retrieve ActualTotalLoad for a day with data... ", end='')
T06_User_Retrieves_ActualTotalLoad_For_2018_01_05()
print("User (with zero quota) tries to retrieve ActualTotalLoad. OK means that an exception occured here... ", end='')
T08_User2_Cannot_Retrieve_Tuple_Out_Of_Quota()
print("User tries to upload a testfile with no authorization... ", end='')
T10_User_Tries_To_Upload_ActualTotalLoad_Dataset_in_Argument('/home/giann_vlax/eurogroup_cli/ActualTotalLoad-10days.csv')
print("User logging out... ", end='')
T11_User_Logs_out()

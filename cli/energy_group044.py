import click
import os

@click.group()

def cli():
    pass

CK = "softeng19bAPI.token"
LU = "http://localhost:8765/energy/api/login"

@cli.command()
@click.option('--area', type=str)
@click.option('--timeres', type=str)
@click.option('--date', type=str)
@click.option('--month',type=str)
@click.option('--year',type=str)
@click.option('--format', type=str)
def ActualTotalLoad(area, timeres, date, month, year, format):
    os.system("grep csrftoken " +CK+ " | sed 's/^.*csrftoken\s*//' > a.txt")
    f=open("a.txt", "r")
    token=f.readline()[:-1]
    f.close()
    os.system("rm a.txt")
    command = "curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+" http://localhost:8765/energy/api/ActualTotalLoad/"+area+'/'+timeres
    if date != None:
        command+='/date/' + date
    elif month != None: 
        command+='/month/' + month
    elif year!=None:
        command+='/year/' + year
    if format=='csv':
        command+='?format=csv'
    os.system(command + ' > out.txt')
    f = open("out.txt", "r")
    s=f.read()
    if format!='csv':
        s1=""
        for c in s:
            if c=='{' or c==",":
                s1+=c+'\n'
            else:
                s1+=c
        s=s1
    click.echo(s)
    print()
    
@cli.command()
def Test():
    os.system("grep csrftoken " +CK+ " | sed 's/^.*csrftoken\s*//' > a.txt")
    f=open("a.txt", "r")
    token=f.readline()[:-1]
    f.close()
    os.system("rm a.txt")
    command = "curl -c "+CK+" -b "+CK+' -e '+LU+' -H "X-OBSERVATORY-AUTH: '+token+'" '+" http://localhost:8765/energy/api/test"
    print(command)
    os.system(command)

@cli.command()
@click.option('--area', type=str)
@click.option('--timeres', type=str)
@click.option('--productiontype', type=str)
@click.option('--date', type=str)
@click.option('--month',type=str)
@click.option('--year',type=str)
@click.option('--format', type=str)
def AggregatedGenerationPerType(area, timeres, productiontype, date, month, year, format):
    os.system("grep csrftoken " +CK+ " | sed 's/^.*csrftoken\s*//' > a.txt")
    f=open("a.txt", "r")
    token=f.readline()[:-1]
    f.close()
    os.system("rm a.txt")
    if productiontype==None:
        p="AllTypes"
    else :
        p=productiontype
        p="%20".join( p.split("_") )
    if date != None:
        command="curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+" http://localhost:8765/energy/api/AggregatedGenerationPerType/"+area+'/'+p+'/' +timeres+'/date/' + date
    elif month != None: 
        command="curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+" http://localhost:8765/energy/api/AggregatedGenerationPerType/"+area+'/'+p+'/' +timeres+'/month/' + month
    elif year!=None:
        command="curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+" http://localhost:8765/energy/api/AggregatedGenerationPerType/"+area+'/'+p+'/' +timeres+'/year/' + year
    if format=='csv':
        command+='?format=csv'
    os.system(command + ' > out.txt')
    f = open("out.txt", "r")
    s=f.read()
    if format!='csv':
        s1=""
        for c in s:
            if c=='{' or c==",":
                s1+=c+'\n'
            else:
                s1+=c
        s=s1
    click.echo(s)

@cli.command()
@click.option('--area', type=str)
@click.option('--timeres', type=str)
@click.option('--date', type=str)
@click.option('--month',type=str)
@click.option('--year',type=str)
@click.option('--format', type=str)
def DayAheadTotalLoadForecast(area, timeres, date, month, year, format):
    os.system("grep csrftoken " +CK+ " | sed 's/^.*csrftoken\s*//' > a.txt")
    f=open("a.txt", "r")
    token=f.readline()[:-1]
    f.close()
    os.system("rm a.txt")
    command = "curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+" http://localhost:8765/energy/api/DayAheadTotalLoadForecast/"+area+'/'+timeres
    if date != None:
        command+='/date/' + date
    elif month != None: 
        command+='/month/' + month
    elif year!=None:
        command+='/year/' + year
    if format=='csv':
        command+='?format=csv'
    os.system(command + ' > out.txt')
    f = open("out.txt", "r")
    s=f.read()
    if format!='csv':
        s1=""
        for c in s:
            if c=='{' or c==",":
                s1+=c+'\n'
            else:
                s1+=c
        s=s1
    click.echo(s)

@cli.command()
@click.option('--area', type=str)
@click.option('--timeres', type=str)
@click.option('--date', type=str)
@click.option('--month',type=str)
@click.option('--year',type=str)
@click.option('--format', type=str)
def ActualvsForecast(area, timeres, date, month, year, format):
    os.system("grep csrftoken " +CK+ " | sed 's/^.*csrftoken\s*//' > a.txt")
    f=open("a.txt", "r")
    token=f.readline()[:-1]
    f.close()
    os.system("rm a.txt")
    command = "curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+" http://localhost:8765/energy/api/ActualvsForecast/"+area+'/'+timeres
    
    if date != None:
        command+='/date/' + date
    elif month != None: 
        command+='/month/' + month
    elif year!=None:
        command+='/year/' + year
    if format=='csv':
        command+='?format=csv'
    print(command)
    os.system(command + ' > out.txt')
    f = open("out.txt", "r")
    s=f.read()
    if format!='csv':
        s1=""
        for c in s:
            if c=='{' or c==",":
                s1+=c+'\n'
            else:
                s1+=c
        s=s1
    click.echo(s)

@cli.command()
def HealthCheck():
    command = "curl http://localhost:8765/energy/api/HealthCheck > out.txt"
    os.system(command + ' > out.txt');
    f = open("out.txt", "r")
    s=f.read()
    click.echo(s)
    
   


@cli.command()
def Reset():
    command = "curl -X POST http://localhost:8765/energy/api/Reset"
    os.system(command + ' > out.txt')
    f = open("out.txt", "r")
    s=f.read()
    click.echo(s)


@cli.command()
@click.option('--username', type=str)
@click.option('--passw', type=str)
def Login(username, passw):
    os.system("./login.sh "+username+" "+passw + ' > out.txt')
    f = open("out.txt", "r")
    s=f.read()
    click.echo(s)


@cli.command()
def Logout():
    os.system("rm softeng19bAPI.token" + ' > out.txt')
    f = open("out.txt", "r")
    s=f.read()
    click.echo(s)


@cli.command()
@click.option('--newuser', type=str)
@click.option('--passw', type=str)
@click.option('--email', type=str)
@click.option('--quota', type=str)
@click.option('--moduser', type=str)
@click.option('--userstatus', type=str)
@click.option('--newdata', type=str)
@click.option('--source', type=str)
def Admin(newuser, passw, email, quota, moduser, userstatus, newdata, source):
    os.system("grep csrftoken " +CK+ " | sed 's/^.*csrftoken\s*//' > a.txt")
    f=open("a.txt", "r")
    token=f.readline()[:-1]
    f.close()
    os.system("rm a.txt")
    url="http://localhost:8765/energy/api/admin"
    if newuser!=None:
        command="curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+' -d "username='+newuser+'&password1='+passw+'&password2='+passw+'&email='+email+'&quota='+quota+'" -X POST '
        url+="/users"
        #print(command)
        os.system(command+url + ' > out.txt')
        f = open("out.txt", "r")
        s=f.read()
        click.echo(s)
    elif moduser!=None:
        command="curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X PUT -d "username='+str(newuser)+'&passw='+str(passw)+'&email='+str(email)+'&quota='+str(quota)+'" '
        url+="/users/"+moduser
        os.system(command+url + ' > out.txt')
        f = open("out.txt", "r")
        s=f.read()
        click.echo(s)
    elif userstatus!=None:
        command="curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+' -X GET '
        os.system(command+url+'/users/'+userstatus + ' > out.txt')
        f = open("out.txt", "r")
        s=f.read()
        click.echo(s)
    elif newdata!=None:
        url = url+'/'+newdata
        command="curl -c "+CK+" -b "+CK+" -e "+LU+' -H "X-OBSERVATORY-AUTH: '+token+'"'+" -X POST -F title=blueberry -F file=@"+source+" "
        
        os.system(command+url + ' > out.txt')
        f = open("out.txt", "r")
        s=f.read()
        click.echo(s)


@cli.command()
@click.option('--text')
def say(text):
    click.echo('You said {}'.format(text))

    

# Softeng_Project

EUROgroup Energy App: Application created on Django Framework in the context of the Software Engineering course in the Electrical Engineering and Computer Science Department in NTUA.

The user has the possibility to perform the following actions:
- To find data about the total electrical energy load, for a specific region and energy type, for a specific time period (day, month, year).
- To find data about the total electrical energy consumption, for a specific region, energy type and time analysis, for a specific time period (day, month, year).
- To find data about the predictions of the total electrical energy load, for a specific region and energy type, for a specific time period (day, month, year).

The data above can be both read in a JSON and a CSV form.

## Tools:

The application supports a RESTful Application Programming Interface (REST API). It was implemented using the tools below:

1.  **DJANGO Framework**, RESTful API tool in Python. Our database was implemented in Sql and contains a table for each of the above functions. The Sql database has to be connected with the api before the application is used.

2.  **Click CLI**, Command Line Interface, through which queris can be performed.

3.  **cURL**, Connection tool between the Command Line Interface and the application server (localhost:8765).

## Execution:

Server activation:

```
python3 manage.py runserver 8765
```

Three types of queries:

**Total load**:
```
energy_group044 actualtotalload --area <DesiredArea> --timeres <DesiredResolution> [--date <YYYY-MM-DD> | --month <YYYY-MM> | --year <YYYY>] [ | --format csv | --format json]
```

**Total consumption**:
```
energy_group044 aggregatedgenerationpertype --area <DesiredArea> --timeres <DesiredResolution> [ | --productiontype <DesiredProductionType>] [--date <YYYY-MM-DD> | --month <YYYY-MM> | --year <YYYY>] [ | --format csv | --format json]
```

**Load prediction**:
```
energy_group044 dayaheadtotalloadforecast --area <DesiredArea> --timeres <DesiredResolution> [--date <YYYY-MM-DD> | --month <YYYY-MM> | --year <YYYY>] [ | --format csv | --format json]
```

**Load and prediction comparison**:
```
energy_group044 actualvsforecast --area <DesiredArea> --timeres <DesiredResolution> [--date <YYYY-MM-DD> | --month <YYYY-MM> | --year <YYYY>] [ | --format csv | --format json]
```

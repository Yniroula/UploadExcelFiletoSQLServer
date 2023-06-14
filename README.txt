# This application simply does two things:
    1. Uploads excel file to SQL SERVER databse table.
        a. Excel File must contain all Column fields or else will display an error message.
    2. Runs a SELECT query from SQL SERVER table.


# Follow the instrustions below to Deploy Flask Application on IIS server using wfastcgi:

    1. Install Python in the system at "C:\Python" folder.
    2. Add “C:\Python\” and “C:\Python\Scripts” to system environment variables.
    3. Install listed python libraries in requirements.txt folder which includes necessry libraries to run the file like Flask, wfastcgi, etc.
    4. Turn on Windows Features - Internet Information Services and make sure World Wide Web Services/Application Development Features/CGI is checked on. 
    5. Enable the FastCGI module from “C:\Python\Scripts\wfastcgi-enable.exe”
    6. Open IIS Server and under SERVER-NAME/Sites Click on Add Website
    7. Give a Site Name, "UploadExcelFiletoSQLServer" and under Physical path download all Python files from Github and add under C:\inetpub\wwwroot\UploadExcelFiletoSQLServer
    8. Give it a different port number i.e. 85, if Port 80 is assigned to another website. If not leave as it is. 
    9. Add Handler Mapping as following:
        a. Request Path: *
        b. Module: FastCgiModule
        c. Executable(optional): C:\Python\python.exe|C:\inetpub\wwwroot\FlaskApp\wfastcgi.py
        d. Name: UploadExcelFiletoSQLServerHandler
    10. Click on “Request Restrictions” and uncheck “Invoke handler only if request is mapped to:” checkbox and select OK followed by another OK. Select “Yes” if prompted by this warning.
    11. Now Update the FastCGI Application by going to:
        IIS Manager-->Click on IISSERVER--> Under IIS go to, "FastCGI Settings"--> Right Click on newly created setting under Full Path--> 
        Click Edit--> Under, "Edit FastCGI Application/FastCGI Properties/Environment Variables" click on 3 dots(...)
    12. Under, "EnvironmentVariables Collection Editor" add 2 entries:
        0.  Name: PYTHONPATH
            Value: C:\inetpub\wwwroot\FlaskApp ONPATH
        1.  Name: WSGI_HANDLER
            Value: app.app
        NOTE: Value name is app.pp since our application name is app.py. If your application name is different write youapplicationname followed by “.app” like youapplicationname.app
    12. Now access your application by going to IIS Manager > Sites > UploadExcelFiletoSQLServer > Under, "Browse Website" > click on “Browse*:85(http)”
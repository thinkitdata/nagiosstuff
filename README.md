# nagiosstuff
Nagios enhancements

<b>tacscrape.py</b> uses <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a> to grep out the hostHeader, serviceHeader and healthBar data from Nagios "Tactical Overview" (nagios/cgi-bin/tac.cgi) for use w/<a href="http://www.chartjs.org">chart.js</a> for displaying a visual summary of the systems being monitored.

<b>For the containers w/out vi:</b>
<li>apt-get update
<li>apt-get install apt-file
<li>apt-file update
<li>apt-get install vim

<b>File Locations:</b>
  <br>*<i>Can be modified just update the definitions in tacscrape.py and main.php</i>
  <br>tacscrape.py - /opt/nagios/etc/objects
  <br>data1.js - /opt/nagios/share/js
  <br>Chart.bundle.js - /opt/nagios/share/js
  
 <b>Include the below into localhost.cfg to run tacscrape.py as a service.</b>
 
# Service check to update data for chart.js
define command{
    command_name    tacscrape
    command_line    /opt/nagios/etc/objects/tacscrape.py
    }

define service{
    use                 generic-service
    host_name           localhost
    service_description TACSCRAPE
    check_command       tacscrape
    }

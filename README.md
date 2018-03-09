# nagiosstuff
Nagios enhancements

Quick steps:
<br>1) cp /opt/nagios/share/main.php /opt/nagios/share/main.php.bak
<br>2) Copy tacscrape.py, Chart.bundle.js, main.php to the locations listed below
<br>3) Edit /opt/nagios/etc/objects/localhost.cfg to include the definitions below
<br>4) Restart Nagios

<b>tacscrape.py</b> uses <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a> to grep out the hostHeader, serviceHeader and healthBar data from Nagios "Tactical Overview" (nagios/cgi-bin/tac.cgi) for use w/<a href="http://www.chartjs.org">chart.js</a> for displaying a visual summary of the systems being monitored.

<b>For the containers w/out vi:</b>
<li>apt-get update
<li>apt-get install apt-file
<li>apt-file update
<li>apt-get install vim

<b>File Locations:</b>
  <br>*<i>Can be modified just update the definitions in tacscrape.py and main.php</i>
  <br>tacscrape.py - /opt/nagios/etc/objects
  <br>Chart.bundle.js - /opt/nagios/share/js
  <br>main.php - /opt/nagios/share
  
 <b>Include the below in localhost.cfg to run tacscrape.py as a service:</b>
<br>define command{
<br>command_name    tacscrape
<br>command_line    /opt/nagios/etc/objects/tacscrape.py
<br>}

<br>define service{
<br>use                 generic-service
<br>host_name           localhost
<br>service_description TACSCRAPE
<br>check_command       tacscrape
<br>}

#Screenshots
<img src="http://github.com/thinkitdata/nagiosstuff/main.php-1.png">

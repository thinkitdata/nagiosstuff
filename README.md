# nagiosstuff
Nagios enhancements.  While Nagios is awesome there are always times I wish it would do a little more.  This repo will be a collection of bits to help Nagios do more.  Hopefully they'll be usefull to you too.  This was put up quickly and will be better organized, neatened up and made more intuitive as additional features are added.  This first enhancement is simply using the awesome <a href="http://www.chartjs.org">Chart.js</a> javascript library to add some summary charts to the homepage.  Additional goals are enhancing the map cgi (via d3.js).  If you have ideas or want to contribute please don't hesitate to ping me!

# Placing a host and service summary dashboard on the main page
Quick steps:
<br>1) cp /opt/nagios/share/main.php /opt/nagios/share/main.php.bak
<br>2) Copy tacscrape.py, Chart.bundle.js, main.php to the locations listed below
<br>3) Edit /opt/nagios/etc/objects/localhost.cfg to include the definitions below
<br>4) Restart Nagios

<b>tacscrape.py</b> uses <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a> (if not installed apt-get install python-bs4) to grep out the hostHeader, serviceHeader and healthBar data from Nagios "Tactical Overview" (nagios/cgi-bin/tac.cgi) along with <a href="http://www.chartjs.org">chart.js</a> for easily build dashboards.

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

# To edit configuration files locally you may or may not need to install vim
<b>For the containers w/out vi:</b>
<li>apt-get update
<li>apt-get install apt-file
<li>apt-file update
<li>apt-get install vim

# Screenshots
![main.php](https://github.com/thinkitdata/nagiosstuff/blob/master/main.php-1.png)
![TACSCRAPE service](https://github.com/thinkitdata/nagiosstuff/blob/master/TACSCRAPE-service.png)
<p>
  Remember we're all in this together so <a href="https://youtu.be/cJtWY6-MF-M">don't hate, just chill</a>. :-)

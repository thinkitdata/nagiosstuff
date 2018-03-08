# nagiosstuff
Nagios enhancements

<b>tacscrape.py</b> uses <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a> to grep out the hostHeader, serviceHeader and healthBar data from Nagios "Tactical Overview" (nagios/cgi-bin/tac.cgi) for use w/<a href="http://www.chartjs.org">chart.js</a> for displaying a visual summary of the systems being monitored.

<b>For the containers w/out vi:</b>
<li>apt-get update
<li>apt-get install apt-file
<li>apt-file update
<li>apt-get install vim

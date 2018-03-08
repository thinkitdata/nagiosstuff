# nagiosstuff
Nagios enhancements

<b>tacscrape.py</b> uses <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a> to grep out the hostHeader, serviceHeader and healthBar data from the "Tactical Overview" (nagios/cgi-bin/tac.cgi) and write it to data1.js for use w/<a href="http://www.chartjs.org">chart.js</a> in a table in main.php.

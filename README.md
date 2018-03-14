# nagiosstuff
Nagios enhancements.  While Nagios Core is awesome there are always times I wish it would do a little more.  This repo will be a collection of bits to help Nagios Core do more.  Hopefully they'll be usefull to you too.  This was put up quickly and will be better organized, neatened up and made more intuitive as additional features are added.  This first enhancement is simply using the awesome <a href="http://www.chartjs.org">Chart.js</a> javascript library to add some summary charts to the homepage.  Additional goals are enhancing the navigation (i.e. side.php) and status map.  The status map looks to be using D3's dendogram layout which unfortunately lacks the ability to have multiple parents.  If you have ideas or want to contribute please don't hesitate to ping me!

# To edit configuration files locally you may or may not need to install vim
<b>For the containers w/out vi:</b>
<li>apt-get update
<li>apt-get install apt-file
<li>apt-file update
<li>apt-get install vim

# Cisco UCS Manager Plugin for Nagios
[Cisco UCS Manager Plugin Release 0.9(4) for Nagios](https://communities.cisco.com/docs/DOC-52697)

The solution provides end-user with two components.
* The first is the Nagios monitoring plugin script (cisco_ucs_nagios) which will provide end-user with the capability of monitoring the components like blade servers, rack servers, fabric interconnects, chassis, IO Modules, fabric extenders in one or more UCS domains.
* The second is an add-on to the Nagios, which will provide end-user with the capability to auto discover UCS domain and create the host definitions in Nagios . It also creates the service definitions for the services defined in the configuration file. By default, the addon is shipped with basic service definitions for each UCS component (aka host in Nagios) which use the cisco_ucs_nagios script to monitor their health. Refer to the user guide section 5.1 for the list of services defined by the addon. For components/hosts which are not healthy, it gives the associated faults and their details. For components/hosts which are healthy, it gives the inventory details.
Supported Nagios Versions: 
This plugin is supported on Nagios Core version 3.2 and higher versions. 

Supported Cisco UCS Manager Releases: 
This plugin is supported on Cisco UCS Manager Releases 2.1, 2.2 and 3.0. 

# Software Requirements for Release 0.9(4): 
### This release of the plugin requires Python SDK 0.8.3.  It's included in this repo for your convenience.

New Features in Release 0.9(4): 
Plugin Enhancements: 
Capabilities to generate performance statistics of different UCS components. 
Check and display faults based on power state of the UCS servers. 
"onlyFaults" flag has been changed to "faultDetails", this flag shows detailed fault info when run with inHierarchical flag. 
Short options for parameters "--inHierarchical" i.e. “–R” , "--useSharedSession" i.e. “–S” and "--faultDetails" i.e. “-F” have been added. 

Auto-Discovery Add-On Enhancements: 
IP range can now be provided while discovering UCS domains. 
Auto-Discovery script gets CLI arguments to provide UCS details. 
Capabilities for user to create custom services for all classes or DN. 
Option to keep previously discovered UCS domains when re-running Auto-Discovery. 
UCS blades and racks are now getting discovered and named using service profile attached to it. 
Flag to discover only the blades and rack servers which has a service profile associated with it. 
CLI flag which provides option to disable the default host-group creation. 
CLI flag which provides option to disable multiple host creation and in-turn create a single domain host. 
Short options for multiple CLI parameters. 

Important Note regarding Backward Compatibility: 
If you are using the add-on and upgrading from an older release of plugin to release 0.9.4 , you must re-discover all the domains using the new add-on to create new service definition files as the 'onlyFaults' flag in 'cisco_ucs_nagios' script is changed to 'faultDetails'. 

Upgrading from Release 0.9.2 to Release 0.9.3 or above: 
Run the attached migrate.py to migrate from 0.9.2 release structure to the new structure. 
Follow the installation procedure mention in the user guide to upgrade to release 0.9.3 or above. 

New Features in Release 0.9(3): 
Support for UCS Mini and UCS Manager Release 3.0(1) 
Installer script for easy installation and uninstallation of the solution (plugin and add-on). 
New Features in Release 0.9(2): 
Multiple services for the same UCS domain can share a single session by using --useSharedSession option in CLI. 
Better scale numbers: Upto 600 services per UCS domain 
Optimized queries for faster response from UCS domain. 
Better error handling and reporting in debug mode. 
Updated wildcard filter for filtering class based services. 

For any queries/feedback on Cisco UCSM Plugin for Nagios 3.x, please add a discussion to the Cisco Developed Integrations sub-space on Cisco UCS Communities. 

# Screenshots
Nagios Map View
![Nagios Map view](https://github.com/thinkitdata/nagiosstuff/blob/master/UCS-plugin/Nagios%20UCS%20plug-in.jpg)

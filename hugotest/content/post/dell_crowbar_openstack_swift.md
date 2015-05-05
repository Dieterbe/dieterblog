+++
title = "Dell crowbar openstack swift"
date = "2012-05-02T11:50:11-04:00"
tags = ["devops", "openstack"]
+++
<!--more-->

<p>

It provides a central management interface which leverages chef, but extends it to a broader scope: it takes care of configuring the bios and raid firmware, BMC/IPMI, doing a PXE autoinstall and setting up chef, which of course does everything else you might need.

<br/>The crowbar admin machine also runs Nagios and Ganglia and the configuration is automatically kept in sync with the roles you apply to your nodes. (adding support for a different monitoring/alerting solution is probably not too hard.  I'm thinking about graphite support or even integrating with an existing graphite setup)

<br/>It uses a plugin system called barclamps and it's vendor-agnostic.  (minus the barclamps that deal with your hardware)

It can even suggest roles for your nodes based on best practices (like: for an X-node openstack cluster we recommend Y proxy's and Z foobars) and hardware properties it discovers (storage vs cpu power vs ram etc)

<br/>Next step would be automating purchase orders, delivery handling and physical installation in racks.

</p>

<p>I think this tool deserves more attention and should be added to your devops toolchain for the cloud (<i>triple buzzword bonus!!!</i>)</p>

<p>

I've currently been using it to easily setup an <a href="https://github.com/dellcloudedge/crowbar/wiki/Swift--barclamp">openstack swift</a> test cluster on <a href="https://github.com/dellcloudedge/crowbar/wiki/Running-Crowbar-in-VirtualBox-VMs">a virtualbox infrastructure</a> (even the latter is easily automated with a shell script), and I'm looking forward to use it on physical hardware and have it take care of the bios and raid settings, I'm expecting it will even set the LCD's on the frontpanel to something interesting automatically. (btw the <a href="http://www.dell.com/poweredge">12G poweredge servers</a> have some neat new features)

</p>

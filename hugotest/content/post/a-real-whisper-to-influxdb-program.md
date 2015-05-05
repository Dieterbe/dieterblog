+++
title = "A real whisper-to-InfluxDB program."
date = "2014-09-30T08:37:48-04:00"
tags = ["devops", "monitoring", "golang"]
+++
I hinted that one could write a Go program using the unofficial <a href="https://github.com/kisielk/whisper-go">whisper-go</a> bindings and the <a href="https://github.com/influxdb/influxdb/tree/master/client">influxdb Go client library</a>.

That's what I did now, it's at <a href="https://github.com/vimeo/whisper-to-influxdb">github.com/vimeo/whisper-to-influxdb</a>.

It uses configurable amounts of workers for both whisper fetches and InfluxDB commits,

but it's still a bit naive in the sense that it commits to InfluxDB one serie at a time, irrespective of how many records are in it.

My series, and hence my commits have at most 60k records, and presumably InfluxDB could handle a lot more per commit, so we might leverage better batching later.  Either way, this way I can consistently commit about 100k series every 2.5 hours (or 10/s), where each serie has a few thousand points on average, with peaks up to 60k points. I usually play with 1 to 30 InfluxDB workers. 

Even though I've hit a few <a href="https://github.com/influxdb/influxdb/issues/985">InfluxDB</a> <a href="https://github.com/influxdb/influxdb/issues/970">issues</a>, this tool has enabled me to fill in gaps after outages and to do a restore from whisper after a complete database wipe.



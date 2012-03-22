#
# Regular cron jobs for the hellotestdeb package
#
0 4	* * *	root	[ -x /usr/bin/hellotestdeb_maintenance ] && /usr/bin/hellotestdeb_maintenance

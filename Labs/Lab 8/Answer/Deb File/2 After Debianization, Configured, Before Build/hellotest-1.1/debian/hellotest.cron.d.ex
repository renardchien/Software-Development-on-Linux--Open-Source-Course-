#
# Regular cron jobs for the hellotest package
#
0 4	* * *	root	[ -x /usr/bin/hellotest_maintenance ] && /usr/bin/hellotest_maintenance

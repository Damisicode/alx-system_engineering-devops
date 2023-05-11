# Use Strace to find why apache is returning a 500 error
exec { 'fix-apache':
	command => "sed -i 's/phpp/php/g' /var/www/html/wp-setting.php",
	path 	=> ['/usr/bin', '/usr/sbin', '/bin']
}

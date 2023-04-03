# This manifest mods a server conf file to include custom header

package {'nginx':
	ensure => present,
} ->
file {'/etc/nginx/conf.d/cus_headers.conf':
	owner => 'root',
	group => 'root',
	mode => '0644',
	content => 'add_header X-Served-By $hostname;',
} ->
service {'nginx':
	ensure => 'running',
	require => File['/etc/nginx/conf.d/cus_headers.conf'],
}

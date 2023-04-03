# This manifest mods a server conf file to include custom header

package {'nginx':
	ensure => present,
} ->
file {'/etc/nginx/conf.d/cus_headers.conf':
	content => 'add_header X-Served-By $hostname;',
	owner => 'root',
	group => 'root',
	mode => '0644',
} ->
service {'nginx':
	ensure => 'running',
	require => File['/etc/nginx/conf.d/cus_headers.conf'],
}

# This manifest increases the number of concurrent worker processes

exec { 'worker processes fix':
  command => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/nginx.conf",
  path    => '/bin/',
  notify  => Exec['nginx restart']
}

exec { 'nginx restart':
  command => 'nginx stop && nginx start',
  path    => '/etc/init.d'
}

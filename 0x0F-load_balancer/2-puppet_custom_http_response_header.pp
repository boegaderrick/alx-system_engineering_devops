# This manifest mods a server conf file to include custom header

exec {'install_nginx':
  command => 'sudo apt-get update && sudo apt-get install nginx -y',
  path    => '/usr/bin/:/bin/',
}
-> exec {'create_file':
  command => 'echo "add_header X-Served-By \$hostname;" >> cus_headers.conf',
  path    => '/usr/bin/:/bin/',
}
-> exec {'move_file':
  command => 'sudo mv cus_headers.conf /etc/nginx/conf.d/',
  peth    => '/usr/bin/:/bin/',
}

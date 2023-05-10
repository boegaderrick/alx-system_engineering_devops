# This manifest fixes a bug causing a server error

exec { 'replace php bug':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin/'
}

# This manifest configures user limits

exec { 'mute-it':
  command => 'sed -i "s/holberton/# holberton/g" /etc/security/limits.conf',
  path    => '/bin'
}

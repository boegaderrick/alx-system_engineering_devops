#This script modifies ssh_config
file { 'Password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file { 'Identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}

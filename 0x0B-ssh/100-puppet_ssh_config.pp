#This script modifies ssh_config
file_line { 'PasswordAuthentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

new_line { 'IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}

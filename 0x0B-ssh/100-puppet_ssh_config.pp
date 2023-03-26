#This script modifies ssh_config
file_line { 'PasswordAuthentication':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'IdentityFile':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => '    IdentityFile ~/.ssh/school',
}

#This script modifies ssh_config
file_line { 'PasswordAuthentication':
  path   => '/etc/ssh/ssh_config',
  pw   => 'PasswordAuthentication no',
}

file_line { 'IdentityFile':
  path   => '/etc/ssh/ssh_config',
  file   => 'IdentityFile ~/.ssh/school',
}

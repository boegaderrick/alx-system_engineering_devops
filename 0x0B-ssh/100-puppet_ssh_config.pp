#This script modifies ssh_config

file_line {'IdentityFile':
	path => '/etc/ssh/ssh_config',
	line => IdentityFile '~/.ssh/school',
	}

file_line {'PasswordAuthentication':
	path => '/etc/ssh/ssh_config',
	line => 'PasswordAuthentication no',
	}

#This script modifies ssh_config
file_line {'PasswordAuthentication':
	path => '/etc/ssh/ssh_config',
	line => 'PasswordAuthentication no',
	}

file_line {'IdentifyFile':
	path => '/etc/ssh/ssh_config',
	line => '~/.ssh/school',
	}

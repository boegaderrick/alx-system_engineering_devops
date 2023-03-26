#This script modifies the ssh_config
file {'/etc/ssh/ssh_config':
	PasswordAuthentication => no,
	IdentifyFile => ~/.ssh/school,
	}
file {'~/.ssh/config':
	PasswordAuthentication => no,
	IdentifyFile => ~/.ssh/school,
	}

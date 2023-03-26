#This script modifies the ssh_config
file {'/etc/ssh/ssh_config':
	PasswordAuthentication => no,
	IdentityFile => ~/.ssh/school,
	}
file {'~/.ssh/config':
	PasswordAuthentication => no,
	IdentityFile => ~/.ssh/school,
	}

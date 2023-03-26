#This script modifies the ssh_config
file {'~/.ssh/config':
	PasswordAuthentication => no,
	IdentityFile => ~/.ssh/school,
	}

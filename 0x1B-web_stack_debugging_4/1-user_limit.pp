# Puppet manifest to change OS configuration for the holberton user

exec { 'set_soft_file_limit_for_user':
  path    => ['/bin', '/usr/bin'],
  command => 'sed -i "s/^holberton soft .*/holberton soft nofile 2048/" /etc/security/limits.conf',
}

exec { 'set_hard_file_limit_for_user':
  path    => ['/bin', '/usr/bin'],
  command => 'sed -i "s/^holberton hard .*/holberton hard nofile 2048/" /etc/security/limits.conf',
}

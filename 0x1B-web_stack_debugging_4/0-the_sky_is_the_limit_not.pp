# Puppet manifest to adjust Nginx configuration and restart the Nginx service

exec { 'change upper limit':
  path    => '/bin',
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
}

exec { 'nginx restart':
  path    => '/etc/init.d',
  command => 'nginx restart',
}

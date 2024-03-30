# Puppet manifest to install and configure Nginx server

# Update packages
exec { 'Update packages':
  command => 'sudo apt-get update',
  path    => '/usr/bin/'
}

# Install Nginx package
package { 'nginx':
  ensure   => 'installed',
  name     => 'nginx',
  provider => 'apt',
  require  => Exec['Update packages']
}

# Add custom header to Nginx configuration
file_line { 'Custom header':
  path    => '/etc/nginx/sites-available/default',
  line    => "\tadd_header X-Served-By ${hostname};",
  after   => 'listen 80 default_server;',
  require => Package['nginx']
}

# Restart Nginx service
exec { 'restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin/',
  require => File_line['Custom header']
}

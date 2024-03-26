# Puppet manifest to install and configure Nginx server

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Set up custom index page
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Package['nginx'],
}

# Set up custom 404 page
file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
  require => Package['nginx'],
}

# Enable site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Redirect /redirect_me with a 301 status
nginx::resource::location { 'redirect_me':
  ensure   => present,
  location => '/redirect_me',
  www_root => '/var/www/html',
  file     => 'redirect_me',
}

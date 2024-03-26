# Puppet manifest to install and configure Nginx server

# Update system package lists
exec { 'Update packages':
    command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
    ensure  => 'installed',
    require => exec['update system'],
}

# Set up custom index page
file { '/var/www/html/index.html':
    content => 'Hello World!',
}

# Configure 301 redirect for /redirect_me
exec { '301 redirect':
    command  => '/bin/sed -i "/^server {/a \\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
    provider => 'shell',
    require  => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}

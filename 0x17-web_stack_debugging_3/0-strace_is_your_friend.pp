# Puppet manifest to fix permissions and ownership for Apache 500 error

exec { 'fix_permissions_and_ownership':
  command => 'sed -i "s/.phpp/.php/g"  /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

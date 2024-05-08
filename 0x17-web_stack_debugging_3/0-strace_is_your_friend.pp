# Puppet manifest to fix permissions and ownership for Apache 500 error

exec { 'fix_permissions_and_ownership':
  command => 'chmod -R 755 /var/www/html && chown -R www-data:www-data /var/www/html',
  unless  => 'find /var/www/html -type d -not -perm 755 -or -not -user www-data -or -not -group www-data',
  path    => ['/bin', '/usr/bin'],
}

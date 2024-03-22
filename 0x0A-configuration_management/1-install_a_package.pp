# Puppet manifest to install Flask package

package { 'flask':
  ensure   => '2.1.1',
  provider => 'pip3',
}

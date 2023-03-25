# This is a file containing puppet code to create a file
file { '/tmp/School':
  ensure => file,
  path => '/tmp/School'
  mode => '0744'
  owner => 'www-data',
  group => 'www-data',
  content => 'I love puppet'
}

# This is a file containing puppet code to create a file
# File path is /tmp/school
# File permission is 0744
# File owner is www-data
# File group is www-data
# File contains I love Puppet
file { '/tmp/School':
     ensure => file,
     path => '/tmp/School'
     mode => '0744'
     owner => 'www-data',
     group => 'www-data',
     content => 'I love puppet'
}
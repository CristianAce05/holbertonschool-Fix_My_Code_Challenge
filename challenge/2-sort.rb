#!/usr/bin/ruby
puts ARGV.select { |x| x.match(/\A-?[0-9]+\z/) }.map(&:to_i).sort

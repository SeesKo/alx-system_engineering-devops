#!/usr/bin/env ruby

input_string = ARGV[0]

# Using the regular expression /School/ to scan all occurrences
matches = input_string.scan(/School/)

# Printing the concatenated result or an empty string if no match
puts matches.empty? ? '' : matches.join

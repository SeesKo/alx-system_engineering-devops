#!/usr/bin/env ruby

input_string = ARGV[0]

# Using the regular expression /School/ to match the word "School"
match_result = input_string.match(/School/)

# Printing the match result or an empty string if no match
puts match_result ? match_result[0] : ''

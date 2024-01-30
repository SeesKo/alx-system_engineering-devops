#!/usr/bin/env ruby

input_string = ARGV[0]

# Using the regular expression /hbt*n/ to match the test strings
matches = input_string.scan(/hbt*n/)

# Printing the match results
puts matches.join("\n")

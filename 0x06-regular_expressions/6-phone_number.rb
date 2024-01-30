#!/usr/bin/env ruby

def match_phone_number(input_string)
  # Use the regular expression /^\d{10}$/ to match a 10-digit phone number
  matches = input_string.scan(/^\d{10}$/)
  
  # Print the match results
  puts matches.join("\n")
end

# Accept one argument from the command line
input_string = ARGV[0]

# Call the matching method with the provided argument
match_phone_number(input_string)


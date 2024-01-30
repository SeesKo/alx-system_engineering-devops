#!/usr/bin/env ruby

def match_capital_letters(input_string)
  # Use the regular expression /[A-Z]/ to match capital letters
  matches = input_string.scan(/[A-Z]/)
  
  # Print the match results joined as a string
  puts matches.join
end

# Accept one argument from the command line
input_string = ARGV[0]

# Call the matching method with the provided argument
match_capital_letters(input_string)

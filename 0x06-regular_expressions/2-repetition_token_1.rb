#!/usr/bin/env ruby

def match_repetition_token(input_string)
  # Use the regular expression /hb+t*n/ to match the test strings
  matches = input_string.scan(/hb+t*n/)
  
  # Print the match results
  puts matches.join("\n")
end

# Accept one argument from the command line
input_string = ARGV[0]

# Call the matching method with the provided argument
match_repetition_token(input_string)

#!/usr/bin/env ruby
#File.open("text_messages.log", "r").each_line do |log|
#  from = log.scan(/from:([^\]]+)/).join
#  to = log.scan(/to:([^\]]+)/).join
#  flags = log.scan(/flags:([^\]]+)/).join
#  puts from + "," + to + "," + flags + "\n"
#end

puts ARGV[0].scan(/^.+from:([^\]]+)|to:([^\]]+)|flags:([^\]]+)/).flatten.compact.join(",")

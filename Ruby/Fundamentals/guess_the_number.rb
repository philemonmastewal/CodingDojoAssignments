def guess_number guess
  number = 21

  if guess == number
    return "Correct! The number was 21."
  elsif guess > number
    return  "Nope, your guess was too high!"
  else
    return "Nope, your guess was too low!"
  end
end

puts guess_number 25
puts guess_number 10
puts guess_number 21

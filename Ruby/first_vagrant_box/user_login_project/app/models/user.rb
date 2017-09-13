class User < ApplicationRecord
  validates :first_name, :last_name, :email_address, :age, presence: true
  validates :age, numericality: { greater_than_or_equal_to: 10, less_than: 150 }
  validates :first_name, :last_name, length: { minimum: 2 }
end


# class User < ActiveRecord::Base<--older version 
#   validates :first_name, :last_name, :email_address, :age, presence: true
#   #above will check to make sure these spots are not blank
#   validates :age, numericality: { greater_than_or_equal_to: 10, less_than: 150 }
#   #above requires that input is a number... and that number is >=(at least) 10 and (below) <150
#   validates :first_name, :last_name, length: { minimum: 2 }
#   #makes sure these inputs are at least 2 characters long
# end

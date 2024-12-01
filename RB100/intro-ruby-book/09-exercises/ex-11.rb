# Given the following data structures, write a program that copies the information
# from the array into the empty hash that applies to the correct person.

contact_data = [
  ["joe@email.com", "123 Main st.", "555-123-4567"],
  ["sally@email.com", "404 Not Found Dr.", "123-234-3454"]
]

contacts = {"Joe Smith" => {}, "Sally Johnson" => {}}

# Expected output:
#  {
#    "Joe Smith"=>{:email=>"joe@email.com", :address=>"123 Main st.", :phone=>"555-123-4567"},
#    "Sally Johnson"=>{:email=>"sally@email.com", :address=>"404 Not Found Dr.",  :phone=>"123-234-3454"}
#  }

fields = [:email, :address, :phone]

contacts.each_with_index do |(name, details), index|
  fields.each_with_index do |field, i|
    details[field] = contact_data[index][i]
  end
end

p contacts
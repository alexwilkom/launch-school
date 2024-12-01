# What will the following program print to the screen? What will it return?
def execute(&block)
  block
end

execute { puts "Hello from inside the execute method!" }

# Nothing. Because the method did not call the block. Should be: block.call 
# A Proc object is returned
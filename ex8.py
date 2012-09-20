formatter = "%r %r %r %r"

print (formatter %(1,2,3,4))
print (formatter %("one","two","three","four"))
print (formatter %(formatter,formatter,formatter,formatter))
#括号缩进位置无所谓
print (formatter %(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I sai goodnight."
)
 )


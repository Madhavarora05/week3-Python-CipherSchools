#{1:1,2:4,3:9} using dict comprehensions
square={num:num**2 for num in range(1,6)}
print(square)


name="Madhav Arora"
word={c:name.count(c) for c in name}
print(word)
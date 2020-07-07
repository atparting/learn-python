# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
basket = {'apple', 'orange', 'apple', 'pear', 'orange'}
print("basket =", basket)
# size
print("len(basket) =", len(basket))
# contains
print("apple in basket =", "apple" in basket)
print()

# add
basket.add("banana")
print("after add, basket =", basket)

# remove
basket.remove("banana")  # 如果元素不存在，会发生错误
print("after remove, basket =", basket)
basket.discard("banana")  # 如果元素不存在，不会发生错误

basket.clear()
print("after clear, basket =", basket)

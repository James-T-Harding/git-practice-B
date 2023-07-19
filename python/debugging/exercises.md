### E1
```Python
user_funds = 10.31
item_price = price["Burger"]

if item_price < user_funds:
    Print("You have enough money!")
if item_price = user_funds:
    print("You have the precise amount of money")
if item_price < user_funds:
    print(Sorry you don't have enough money)
```
 - line 2: price was not specified.
 - line 5: print was capitalised.
 - line 6: == instead of =
 - line 9: string must be enclosed in ""

### E2
```Python
def product(n):
    total == 1
    for n in n:
        total *= i
return total

print(product([4,4,5]))
```
- line 1 = instead of ==
- line 2 i in n instead of n in n
- line 4 indenting on return


### E3
```Python
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n = 0:
                return False
            return True
```
- line 6: == instead of = 
- line7: move indenting of return back


### E4
```Python
item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(item_list[i])

print item_list[5]

```
- line 6: just i, not item_list[i]
- line 7: n += 1 inside while block
- line 8: print must be followed by brackets

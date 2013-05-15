max = 4000000
a = 1
b = 1
sum = 0
while true do
  a, b = a + b, a
  if a % 2 == 0 then
    sum = sum + a
  end
  if a >= max then
    break
  end
end
print(sum)

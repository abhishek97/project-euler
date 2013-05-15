function is_multi(n)
  return n % 3 == 0 or n % 5 == 0
end

sum = 0
for i = 0, 999 do
  if is_multi(i) then
    sum = sum + i
  end
end

print(sum)

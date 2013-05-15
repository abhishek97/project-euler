function is_prime(n)
  if n < 2 then
    return false
  elseif n == 2 then
    return true
  elseif n % 2 == 0 then
    return false
  end
  max = math.floor(math.sqrt(n))
  i = 3
  while i < max do
    if n % i == 0 then
      return false
    end
    i = i + 2
  end
  return true
end

num = 600851475143
for j = math.floor(math.sqrt(num)), 3, -1 do
  if num % j ==0 and is_prime(j) then
    print(j)
    break
  end
end

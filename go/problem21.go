package main

import (
    "fmt"
    "math"
)

func divisor_sum(n int) int {
    sum := 1 // all numbers are divisible by 1
    nsqrt := int(math.Ceil(math.Sqrt(float64(n))))
    for i := 2; i <= nsqrt; i++ {
        if n % i == 0 {
            sum += i
            if i != nsqrt {
                sum += n / i
            }
        }
    }
    return sum
}

const COUNT = 10000

func main() {
    total := 0
    for i := 1; i < COUNT; i++ {
        di := divisor_sum(i)
        if di != i && i == divisor_sum(di) {
            total += i
        }
    }
    fmt.Printf("%v\n", total)
}

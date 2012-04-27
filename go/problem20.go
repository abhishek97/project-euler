package main

import (
    "fmt"
    "math/big"
)

func main() {
    n := new(big.Int)
    n.MulRange(1, 100)
    sum := 0
    for _, d := range(n.String()) {
        sum += int(d) - int('0')
    }
    fmt.Printf("%v\n", sum)
}

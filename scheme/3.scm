(define (is-factor? a b)
  (= (modulo b a) 0))
(define (is-prime? n)
  (define (num-iter i mx)
    (if (<= i mx)
      (if (is-factor? i n)
        #t
        (num-iter (+ i 2) mx))
      #f))
  (if (num-iter 3 (sqrt n))
    #f
    (not (is-factor? 2 n))))

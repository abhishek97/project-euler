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
(define (find-factor n)
  (define (find-iter i)
    (if (is-factor? i n)
      (if (is-prime? i)
        i
        (find-iter (- i 2)))
      (find-iter (- i 2))))
  (if (is-factor? 2 (floor (sqrt n)))
    (find-iter (+ (floor (sqrt n)) 1))
    (find-iter (floor (sqrt n)))))

(find-factor 600851475143)

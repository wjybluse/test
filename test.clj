(defn factorial [f n]
    (if (= n 1)
        f
        (recur (* f n) (dec n))))

 (factorial 1 10000000000)

; During our CS archealogy quest we stumbled across this partially corrupted magnetic tape that seems to contain some code of the ancients:

(defun &(n)(if(< n |)n(+ (&(- n 1))(&(- n |)))))(&(*(let((% |)(@ $))(* % @))(let((^ |)(! $))(+ ^ !))))

; Appearently during the read-out two numbers have been replaced with the non-excuting characters '|'' and '$'. Which integers do these two need to become to make the code return the value 832040?"
; Write the answer as flag{a,b} where a is the integer representing '|' and b is the integer representing '$'.
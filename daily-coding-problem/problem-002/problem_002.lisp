(defun solution (numbers)
  (let ((product (reduce #'* numbers))
	(result ()))
    (dotimes (i (length numbers))
      (if (/= (elt numbers i) 0)
	  (push (/ product (elt numbers i)) result)
	  (push
	   (* (reduce #'* (subseq numbers 0 i))
	      (reduce #'* (subseq numbers (+ i 1))))
	   numbers)))
    (nreverse result)))

(defun recursive-solution (numbers &optional (factor 1))
  (cond ((= (length numbers) 1)
	 (list factor))
	(t
	 (let* ((half (truncate (/ (length numbers) 2)))
	       (left (subseq numbers 0 half))
	       (right (subseq numbers half)))
	   (append
	    (recursive-solution left (* factor (reduce #'* right)))
	    (recursive-solution right (* factor (reduce #'* left))))))))

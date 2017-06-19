all : c_quick_sort quick_sort merge_sort insert_sort

c_quick_sort :
	@echo "c quick sort..."
	@gcc -o quick quick.c
	@time ./quick < input.txt > /dev/null

quick_sort :
	@echo "python quick sort..."
	@time python3 quick.py < input.txt > /dev/null

insert_sort :
	@echo "python insert sort..."
	@time python3 insert.py < input.txt > /dev/null

merge_sort :
	@echo "python merge sort..."
	@time python3 merge.py < input.txt > /dev/null

test :
	# quicksort unit test.
	@python3 -m unittest

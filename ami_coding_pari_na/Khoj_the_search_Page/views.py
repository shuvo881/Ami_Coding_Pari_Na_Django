from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import InputData
# Create your views here.

# binary search function for item searching, time complexity: O(log n)
def binary_search(nums, item) -> bool:
    left_index = 0
    right_index = len(nums) - 1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if nums[mid_index] == item:
            return True
        elif nums[mid_index] > item:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return False

# using bubble sort algorithm, time complexity: O(n^2)
def descending_order_sort(arr) -> None:
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Compare in descending order
                # Swap arr[j] and arr[j+1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



@login_required
def search_page(request):
    if request.method == 'POST':

        input_values = request.POST.get('input_values')
        search_value = int(request.POST.get('search_value'))

        input_values_list = [int(x.strip()) for x in input_values.split(',')]
        # sort descending order by descending_order_sort function
        descending_order_sort(input_values_list)

        InputData.objects.create(user=request.user, input_values=','.join(map(str, input_values_list)))

        # search value by binary_search function
        is_search_value_present = binary_search(input_values_list, search_value)
        return render(request, "Khoj_the_search_Page/search_page.html", {"is_search_value_present": is_search_value_present, "request": request})
    return render(request, "Khoj_the_search_Page/search_page.html")


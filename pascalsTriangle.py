'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

def pascals_triangle_helper(nr_rows, level, result_list):
    if level > nr_rows:
        return

    if level == 1 or level == 2:
        if level == 1:
            result_list.append([1])

        elif level == 2:
            result_list.append([1, 1])

        pascals_triangle_helper(nr_rows, level+1, result_list)
        return

    ans_list=[0] * level # ans_list=[1, 0, 0, 1]
    ans_list[0]=1

    ans_list[level-1]=1

    prev_level_result = result_list[level-2] #[1, 2, 1]

    idx=1
    for i in range(0, len(prev_level_result) - 1):
        ans_list[idx] = prev_level_result[i] + prev_level_result[i+1]
        idx+=1

    result_list.append(ans_list)
    pascals_triangle_helper(nr_rows, level+1, result_list)


def pascals_triangle(nr_rows):
    result_list=[]
    level=1
    pascals_triangle_helper(nr_rows, level, result_list)

    tmp_level=nr_rows+1
    for item in result_list:
        print ' '*nr_rows + str(item)
        nr_rows-=1

pascals_triangle(5)

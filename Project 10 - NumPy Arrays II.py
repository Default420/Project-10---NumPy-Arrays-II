# -*- coding: utf-8 -*-
"""Copy of AT - Lesson 10 - Project_Question Copy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fb-5DJUGSAEI5YdOs4rqoPx_T9zHTMYL

### Instructions

#### Goal of the Project

This project is designed for you to practice and solve the activities that are based on the concepts covered in the following lessons:

1. Python Lists

2. List Comprehension

3. NumPy Arrays

---

#### Getting Started:

1. Follow the next 3 steps to create a copy of this colab file and start working on the project.
2. Create a duplicate copy of the Colab file as described below.

  - Click on the **File menu**. A new drop-down list will appear.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/lesson-0/0_file_menu.png' width=500>

  - Click on the **Save a copy in Drive** option. A duplicate copy will get created. It will open up in the new tab on your web browser.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/lesson-0/1_create_colab_duplicate_copy.png' width=500>

3. After creating the duplicate copy of the notebook, please rename it in the **YYYY-MM-DD_StudentName_Project10** format.

4. Now, write your code in the prescribed code cells.

---

#### Activity 1: Create and update a null NumPy array

Create a null NumPy array of size 10 and update the sixth value to 11.

A null array is basically an array with all elements as `0`.

Follow the steps given below to achieve the desired result:

- **Step 1:** Import the Numpy module as `np`.

- **Step 2**: Create a null array by passing the size i.e. `10` inside the `np.zeros()` function and store it in a variable `null_arr`.

- **Step 3**: Print the null array.

- **Step 4**: Now update the sixth element of the array by using **list indexing** method. As you need to update the sixth element, the index must be `5`.

- **Step 5**: Print the updated array in the output.
"""

# Write a program to create Null array of size 10 and update the sixth value to 11.
import numpy as np

# Step 2
null_arr = np.zeros(10)

# Step 3
print("Null array:", null_arr)

# Step 4
null_arr[5] = 11

# Step 5
print("Updated array:", null_arr)

"""---

#### Activity 2: Populate a number list

Write a program that populates a list by numbers that lie in the range of 0 to 49 and are also divisible by 5. Use the **List Comprehension** method.

**Output**: `[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]`
"""

# Write a program to populate a number list divisible by 5 in a range of 0 - 49
divisible_by_5 = [num for num in range(50) if num % 5 == 0]
print(divisible_by_5)

"""---

#### Activity 3: Convert a list into an array

Write a program to convert a list of numeric values into a one-dimensional NumPy array.

**For Example:**

**Input**: `lst = [12.23, 13.32, 100, 36.32]`

Data type of `lst` = `list`

**Output**: `numpy_array = [12.23, 13.32, 100, 36.32]`

Data type of `numpy_array` = `numpy.ndarray`
"""

# Write a program to convert a list into one dimensional NumPy array
import numpy as np

lst = [12.23, 13.32, 100, 36.32]

numpy_array = np.array(lst)

print("List:", lst)
print("Numpy Array:", numpy_array)
print("Data type of lst:", type(lst))
print("Data type of numpy_array:", type(numpy_array))

"""---

### Submitting the Project:

1. After finishing the project, click on the **Share** button on the top right corner of the notebook. A new dialog box will appear.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/2_share_button.png' width=500>

2. In the dialog box, make sure that '**Anyone on the Internet with this link can view**' option is selected and then click on the **Copy link** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/3_copy_link.png' width=500>

3. The link of the duplicate copy (named as **YYYY-MM-DD_StudentName_Project10**) of the notebook will get copied

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/4_copy_link_confirmation.png' width=500>

4. Go to your dashboard and click on the **My Projects** option.
   
   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/5_student_dashboard.png' width=800>

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/6_my_projects.png' width=800>

5. Click on the **View Project** button for the project you want to submit.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/7_view_project.png' width=800>

6. Click on the **Submit Project Here** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/8_submit_project.png' width=800>

7. Paste the link to the project file named as **YYYY-MM-DD_StudentName_Project10** in the URL box and then click on the **Submit** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/9_enter_project_url.png' width=800>

---
"""
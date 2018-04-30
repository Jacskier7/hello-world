nums1 = [0,1,1,2,3,4,6,7,10]
nums2 = [2,3,5,7,8,9,12,13]

left1,left2 = 0,0
arr1 = nums1
arr2 = nums2
right1= len(arr1)-1
right2= len(arr2)-1

if nums1[left1] > nums2[right2]:
    arr1 = nums2
    arr2 = nums1

right1= len(arr1)-1
right2= len(arr2)-1
diff = True

while arr1[left1] < arr2[right2]: 
   step = (min(right1-left1, right2-left2)+1) // 2
   if step == 0:
        if (max(right1-left1, right2-left2)+1) // 2 == 0:
            
            print (arr1[right1]+arr2[left2])/2
            break

        if right1-left1 ==0:
            arr1 = arr2
            right2 = right2 -1 
            left1 = left2
            right1 = right2

        elif right2 - left2 == 0:
            arr2 = arr1 
            left1 = left1+1
            left2 = left1
            right2 = right1
        diff = False

   if  right1-left1 >= step and right2-left2 >= step:
        left1 = left1 + step
        right2 = right2 - step
   elif right1 - left1 >= step:
        step = right2-left2
        left1 = left1 + step
        right2 = right1
        arr2 = arr1
        left2 = left1
        diff = False
   elif right1 - left1 < step: 
        step = right1 - left1
        right2 = right2 - step
        left1 = 0
        arr1 = arr2
        right1 = right2
        diff = False

   if diff == False and left1 == right2:
       print arr1[left1]
   elif diff == False and left1+1 == right2:
       print (arr1[left1] + arr1[right2])/2 
       break   

   if arr1[left1] >= arr2[right2]:
       arr1,arr2 = arr2,arr1
       left1,left2 = left2, left1
       right1,right2 = right2, right1

   elif arr1[left1] == arr2[right2]:
       print arr1[left1]
       break
          


  
        


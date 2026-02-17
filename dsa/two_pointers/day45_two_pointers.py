# Problem 1 :

# Valid Palindrome

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
          left += 1
          continue
        
        if not s[right].isalnum():
          right -= 1
          continue


        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("A man, a plan, a canal: Panama"))

#output:
#True





# problem 2 :

# Container With Most Water

height = [1,8,6,2,5,4,8,3,7]


def container_with_most_water(height):
   left = 0
   right = len(height) - 1
   max_area = 0

   while left < right:
      area = min(height[left], height[right]) * (right - left)
     
      max_area = max(max_area, area)

      if height[left] < height[right]:
         left += 1

      else:
         right -= 1

   return max_area 

print(container_with_most_water(height))
      
      

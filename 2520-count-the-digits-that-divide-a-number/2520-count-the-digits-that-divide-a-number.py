class Solution:
    def countDigits(self, num: int) -> int:
        original = num 
        count = 0
        while num > 0 :
            digit = num % 10
            if original % digit == 0:
                count += 1
            num = num // 10
        return(count)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
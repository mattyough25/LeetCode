'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
'''
'''
class Solution:
    def floodFill(self, image: int, sr: int, sc: int, color: int) -> int:
        start = image[sr][sc]
        temp = list()
        for i in range(len(image[:][0])):
            temp.append(image[:][i].copy())

        image[sr][sc] = color
        
        # Check each row
        for iRow in range(len(image[:][sc])):
            if image[iRow][sc] == temp[sr][sc]:
                image[iRow][sc] = color
            else:
                break

        # Check each column
        for iCol in range(len(image[sr][:])):
            if image[sr][iCol] == temp[sr][sc]:
                image[sr][iCol] = color
            else:
                break

        return image
'''

class Solution:
    def floodFill(self, image: int, sr: int, sc: int, color: int) -> int:
        
        
        def visit(r, c):
            
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != a:
                return
            
            image[r][c] = color
            for x, y in [[1,0], [-1,0], [0, 1], [0,-1]]:
                visit(r+x, c+y)
        
        
        m, n, a = len(image), len(image[0]), image[sr][sc]
        if a != color:
            visit(sr, sc)
        return image

# Test Cases
s = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
#print(image[:][1])
sr = 1
sc = 1
color = 2
out = s.floodFill(image,sr,sc,color)
#print(out)
'''
s = Solution()
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0
out = s.floodFill(image,sr,sc,color)
print(out)
'''
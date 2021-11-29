import filecmp

dir1 = './computer'
dir2 = './hdd'

# filecmp.dircmp(dir1, dir2).report()

dc = filecmp.dircmp(dir1, dir2, ignore=['common_files'])

print("Computer: ", dc.left_only)
print("HDD: ", dc.right_only)